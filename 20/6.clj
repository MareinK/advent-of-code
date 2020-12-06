(ns aoc (:require [clojure.set]))

(doseq [setop [clojure.set/union clojure.set/intersection]]
  (->> (clojure.string/split (slurp "6.txt") #"\n\n")
       (map #(->> (clojure.string/split % #"\n")
                  (map set)
                  (apply setop)
                  (count)))
       (reduce +)
       (println)))
