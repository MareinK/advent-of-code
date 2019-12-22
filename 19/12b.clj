(ns aoc (:require [clojure.string :as str]))

(def NDIMS 3)

(defn input []
  (map
   #(vector (map read-string (re-seq #"-?\d+" %)) (repeat NDIMS 0))
   (str/split-lines (slurp "12.txt"))))

(defn gcd [a b] (if (zero? b) a (recur b (mod a b))))
(defn lcm [& v] (reduce #(/ (* %1 %2) (gcd %1 %2)) v))

(defn count-rel [moons op val] (count (filter (comp #(op % val) first) moons)))
(defn gravity-delta [moons moon] (- (count-rel moons > (first moon)) (count-rel moons < (first moon))))
(defn gravity [moons] (map #(assoc % 1 (+ (second %) (gravity-delta moons %))) moons))
(defn velocity [moons] (map #(assoc % 0 (reduce + %)) moons))
(defn step [moons] (velocity (gravity moons)))

(defn find-repeat [moons dim]
  (let [init (for [moon moons] [(nth (first moon) dim) (nth (second moon) dim)])]
    (loop [state init, n 0]
      (if (and (> n 0) (= state init))
        n
        (recur (step state) (+ n 1))))))

(apply lcm (map (partial find-repeat (input)) (range NDIMS)))
