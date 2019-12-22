(ns aoc
  (:require [clojure.string :as str])
  (:require [clojure.set :as set]))

(defn fst [x & _] x)

(defn input []
  (vec (map
        #(str/split % #",")
        (str/split-lines (slurp "3.txt")))))

(defn step-to-xys [step x y]
  (let [n (read-string (subs step 1))
        dx (cond
             (re-matches #"L.*" step) -1
             (re-matches #"R.*" step) 1
             :else 0)
        dy (cond
             (re-matches #"D.*" step) -1
             (re-matches #"U.*" step) 1
             :else 0)]
    (for [i (range 1 (+ n 1))]
      [(+ x (* dx i))
       (+ y (* dy i))])))

(defn path-to-xys [path x y]
  (if (empty? path)
    []
    (let [xys (step-to-xys (first path) x y)
          [nx ny] (last xys)]
      (concat
       xys
       (path-to-xys (drop 1 path) nx ny)))))

(defn manhattan [[x y]]
  (+ (Math/abs x) (Math/abs y)))

(defn solve []
  (let [[a, b] (map #(path-to-xys % 0 0) (input))]
    (apply min (map manhattan (set/intersection (set a) (set b))))))

(solve)
