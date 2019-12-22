(ns aoc
  (:require [clojure.string :as str]))

(defrecord OpDef [func nargs])
(defrecord OpInst [func args])
(defrecord OpResult [mem jump])
(defrecord Arg [value mode])

(defn instructions []
  (vec (map read-string (str/split (slurp "5.txt") #","))))

(defn rd [mem arg]
  (case (:mode arg)
    0 (nth mem (:value arg))
    1 (:value arg)))

(defn wr [mem arg v]
  (assoc mem (:value arg) v))

(defn op-arith [op mem x y z]
  (OpResult. (wr mem z (op (rd mem x) (rd mem y))) nil))

(defn op-input [mem x]
  (OpResult. (wr mem x (read-string (read-line))) nil))

(defn op-output [mem x]
  (println (rd mem x))
  (OpResult. mem nil))

(defn op-jump-if-true [mem x y]
  (OpResult. mem (when-not (= 0 (rd mem x)) (rd mem y))))

(defn op-jump-if-false [mem x y]
  (OpResult. mem (when (= 0 (rd mem x)) (rd mem y))))

(defn op-comp [op mem x y z]
  (OpResult. (wr mem z (if (op (rd mem x) (rd mem y)) 1 0)) nil))

(defn opcode-def [i]
  (case i
    1 (OpDef. (partial op-arith +) 3)
    2 (OpDef. (partial op-arith *) 3)
    3 (OpDef. op-input 1)
    4 (OpDef. op-output 1)
    5 (OpDef. op-jump-if-true 2)
    6 (OpDef. op-jump-if-false 2)
    7 (OpDef. (partial op-comp <) 3)
    8 (OpDef. (partial op-comp =) 3)
    99 (OpDef. nil 0)))

(defn parse-opcode [mem i]
  (mod (nth mem i) 100))

(defn pad-opcode [opcode n]
  (format (str/join ["%0" (+ n 2) "d"]) opcode))

(defn parse-modes [mem i n]
  (let [opcode (pad-opcode (nth mem i) n)
        opmodes (subs opcode 0 (- (count opcode) 2))]
    (reverse (map (comp read-string str) opmodes))))

(defn slice [coll start end]
  (drop start (take end coll)))

(defn parse-instruction [mem, i]
  (let [{func :func nargs :nargs} (opcode-def (parse-opcode mem i))
        args (slice mem (+ i 1) (+ i 1 nargs))
        modes (parse-modes mem i nargs)]
    (OpInst. func (map #(Arg. %1 %2) args modes))))

(defn process [mem, i]
  (let [{func :func args :args} (parse-instruction mem i)]
    (when-not (nil? func)
      (let [{new-mem :mem jump :jump} (apply (partial func mem) args)
            new-i (if (nil? jump)
                    (+ i 1 (count args))
                    jump)]
        (process new-mem new-i)))))

(defn solve []
  (process (instructions) 0))

(solve)
