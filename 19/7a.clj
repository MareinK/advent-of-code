(ns aoc
  (:require [clojure.string :as str]
            [clojure.math.combinatorics :as combo]))

(load-file "processor.clj")

(defn amplifier [program phase in]
  (read-string
   (with-out-str
     (with-in-str (str/join "\n" [phase in])
       (aoc/run program)))))

(defn attempt [program phases]
  (reduce #(amplifier program %2 %1) 0 phases))

(let [program (aoc/instructions "7.txt")]
  (apply max (map
              #(attempt program %)
              (combo/permutations (range 5)))))
