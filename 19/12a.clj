(ns aoc (:require [clojure.string :as str]))

(def NDIMS 3)

(defn input []
  (map
   #(vector (map read-string (re-seq #"-?\d+" %)) (repeat NDIMS 0))
   (str/split-lines (slurp "12.txt"))))

(defn abs [n] (max n (- n)))

(defn count-rel [moons dim op val]
  (count (filter (comp #(op % val) #(nth % dim) first) moons)))

(defn gravity-delta [moons moon]
  (for [dim (range NDIMS)]
    (-
     (count-rel moons dim > (nth (first moon) dim))
     (count-rel moons dim < (nth (first moon) dim)))))

(defn gravity [moons] (map #(assoc % 1 (map + (second %) (gravity-delta moons %))) moons))
(defn velocity [moons] (map #(assoc % 0 (map + (first %) (second %))) moons))
(defn step [moons] (velocity (gravity moons)))
(defn run [moons n] (nth (iterate step moons) n))
(defn energy [moon] (apply * (map #(apply + (map abs %)) moon)))
(defn total-energy [moons] (reduce + (map energy moons)))

(total-energy (run (input) 1000))
