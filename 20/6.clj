(ns aoc (:require [clojure.set]))

(def groups (->> (clojure.string/split (slurp "6.txt") #"\n\n")
                 (map #(->> (clojure.string/split % #"\n")
                            (map set)))))

(doseq [setop [clojure.set/union clojure.set/intersection]]
  (->> groups
       (map #(apply setop %))
       (map count)
       (reduce +)
       (println)))
