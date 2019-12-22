(ns aoc
  (:require [clojure.math.combinatorics :as combo]
            [clojure.core.async
             :as async
             :refer [go chan >!! <!!]]
            [clojure.java.io :as io])
  (:import [java.io InputStream OutputStream]))

(load-file "processor.clj")

;;; Channels as streams and standard in/out

(defn chan-instream [c]
  (proxy [InputStream] []
    (read [dst off len]
      (aset-byte dst off (<!! c))
      1)))

(defn chan-outstream [c]
  (proxy [OutputStream] []
    (write [dst off len]
      (dorun (for [i (range len)]
               (>!! c (nth dst (+ off i))))))))

(defmacro with-in-chan [c & body]
  `(with-open [c# (io/reader (chan-instream ~c))]
     (binding [*in* c#] ~@body)))

(defmacro with-out-chan [c & body]
  `(let [c# (io/writer (chan-outstream ~c))]
     (binding [*out* c#] ~@body)))

;;; Helper

(defn rotate [n coll]
  (let [m (mod n (count coll))]
    (concat (drop m coll) (take m coll))))

;;; Puzzle logic

(defn amplifier [program c-in c-out]
  (go
    (with-in-chan c-in
      (with-out-chan c-out
        (aoc/run program)))))

(defn attempt [program phases]
  (let [channels (for [_ phases] (chan))
        amplifiers (doall (map
                           #(amplifier program %1 %2)
                           channels
                           (rotate 1 channels)))]
    (dorun (for [[phase channel] (map vector phases channels)]
             (with-out-chan channel (println phase))))
    (with-out-chan (first channels) (println 0))
    (<!! (first amplifiers))
    (with-in-chan (first channels) (read-string (read-line)))))

(let [program (aoc/instructions "7.txt")]
  (apply max (map
              #(attempt program %)
              (combo/permutations (range 5 10))))) ; change to (range 5) for part 1 
