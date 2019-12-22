(ns aoc
  (:require [clojure.string :as str]
            [clojure.core.async
             :refer [go chan <!! close!]]))

(load-file "piping.clj")

(defrecord OpDef [func nargs])
(defrecord OpInst [func args])
(defrecord OpResult [mem jump rba]) ; memory, jump, relative base adjustment
(defrecord Arg [value mode])
(defrecord State [mem ip rb]) ; memory, instruction pointer, relative base

(defn instructions [filename]
  (vec (map read-string (str/split (slurp filename) #","))))

(defn rd [mem rb arg]
  (case (:mode arg)
    0 (get mem (:value arg) 0)
    1 (:value arg)
    2 (get mem (+ rb (:value arg)) 0)))

(defn wr [mem rb arg v]
  (case (:mode arg)
    0 (assoc mem (:value arg) v)
    2 (assoc mem (+ rb (:value arg)) v)))

(defn op-arith [op {mem :mem rb :rb} x y z]
  (OpResult. (wr mem rb z (op (rd mem rb x) (rd mem rb y))) nil 0))

(defn op-plus [state x y z]
  (op-arith + state x y z))

(defn op-times [state x y z]
  (op-arith * state x y z))

(defn op-input [{mem :mem rb :rb} x]
  (OpResult. (wr mem rb x (read-string (read-line))) nil 0))

(defn op-output [{mem :mem rb :rb} x]
  (println (rd mem rb x))
  (OpResult. mem nil 0))

(defn op-jump-if-true [{mem :mem rb :rb} x y]
  (OpResult. mem (when-not (= 0 (rd mem rb x)) (rd mem rb y)) 0))

(defn op-jump-if-false [{mem :mem rb :rb} x y]
  (OpResult. mem (when (= 0 (rd mem rb x)) (rd mem rb y)) 0))

(defn op-comp [op {mem :mem rb :rb} x y z]
  (OpResult. (wr mem rb z (if (op (rd mem rb x) (rd mem rb y)) 1 0)) nil 0))

(defn op-less-than [state x y z]
  (op-comp < state x y z))

(defn op-equal [state x y z]
  (op-comp = state x y z))

(defn op-relative-base-offset [{mem :mem rb :rb} x]
  (OpResult. mem nil (rd mem rb x)))

(defn opcode-def [i]
  (case i
    1 (OpDef. op-plus 3)
    2 (OpDef. op-times 3)
    3 (OpDef. op-input 1)
    4 (OpDef. op-output 1)
    5 (OpDef. op-jump-if-true 2)
    6 (OpDef. op-jump-if-false 2)
    7 (OpDef. op-less-than 3)
    8 (OpDef. op-equal 3)
    9 (OpDef. op-relative-base-offset 1)
    99 (OpDef. nil 0)))

(defn parse-opcode [{mem :mem ip :ip}]
  (mod (get mem ip) 100))

(defn parse-modes [{mem :mem ip :ip} n]
  (let [modes (map
               (comp read-string str)
               (reverse (str (quot (get mem ip) 100))))]
    (concat modes (repeat (- n (count modes))  0))))

(defn parse-instruction [{mem :mem ip :ip :as state}]
  (let [{func :func nargs :nargs} (opcode-def (parse-opcode state))
        args  (for [i (range (+ ip 1) (+ ip 1 nargs))] (get mem i))
        modes (parse-modes state nargs)]
    (OpInst. func (map #(Arg. %1 %2) args modes))))

(defn process [{ip :ip rb :rb :as state}]
  (let [{func :func args :args} (parse-instruction state)]
    (when-not (nil? func)
      (let [{new-mem :mem jump :jump rba :rba} (apply func state args)]
        (recur (State.
                new-mem
                (if (nil? jump)
                  (+ ip 1 (count args))
                  jump)
                (+ rb rba)))))))

(defn run [program]
  (let [instrs (into {} (map-indexed vector program))]
    (process (State. instrs 0 0))))


; TODO: idea: make send/recv simply be the channels themselves,
; with buffer 1 and transducers for the int-str conversion
; then use alt(s)!! in implementation with c-res ('done')
; to catch completion

(defn run-async [program]
  (let [c-in (chan)
        c-out (chan)
        c-res (go
                (aoc/with-in-chan c-in
                  (aoc/with-out-chan c-out
                    (run program))))
        send #(aoc/with-out-chan c-in (println %))
        recv #(aoc/with-in-chan c-out (read-string (read-line)))
        wait #(<!! c-res)
        close #(do (close! c-res) (close! c-in) (close! c-out))]
    [send recv wait close]))

(defn run-file [filename]
  (run (instructions filename)))

(defn run-file-async [filename]
  (run-async (instructions filename)))
