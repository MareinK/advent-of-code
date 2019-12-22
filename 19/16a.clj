(ns aoc (:require [clojure.core.matrix :refer [mmul]]))

(defn repeatelems [n seq]
  (mapcat (partial repeat n) seq))

(defn vabs [v]
  (map #(Math/abs %) v))

(defn vmod [m n]
  (map #(mod % n) m))

(def v (map (comp read-string str) (slurp "16.txt")))

(def p
  (for [i (range (count v))]
    (take (count v) (drop 1 (cycle (repeatelems (inc i) [0 1 0 -1]))))))

(defn phase [n]
  (if (= n 0)
    v
    (vmod (vabs (mmul p (phase (- n 1)))) 10)))

(apply str (take 8 (phase 100)))
