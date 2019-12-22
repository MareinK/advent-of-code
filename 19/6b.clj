(ns aoc
  (:require [clojure.string :as str]))

(defn input []
  (into
   (hash-map)
   (map
    #(vec (reverse (str/split % #"\)")))
    (str/split-lines (slurp "6.txt")))))

(defn gparents [graph node]
  (let [parent (get graph node)]
    (if (nil? parent)
      '()
      (conj (gparents graph parent) parent))))

(defn ordered-intersect [a b]
  (filter (set b) a))

(defn solve []
  (let [graph (input)
        p1 (gparents graph "YOU")
        p2 (gparents graph "SAN")
        pc (first (ordered-intersect p1 p2))]
    (+ (.indexOf p1 pc) (.indexOf p2 pc))))

(solve)
