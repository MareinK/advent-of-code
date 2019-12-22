(ns aoc
  (:require [clojure.string :as str])
  (:require [clojure.set :as set]))

(defn make-set [line-vec]
  (assoc line-vec 1 #{(nth line-vec 1)}))

(defn input []
  (apply
   (partial merge-with set/union)
   (map
    #(into (hash-map) [(make-set (str/split % #"\)"))])
    (str/split-lines (slurp "6.txt")))))

; returns [descendants, paths] counts
(defn count-paths [graph origin]
  (apply (partial map + [0 0])
         (for [node (get graph origin)]
           (let [[d p] (count-paths graph node)]
             [(+ d 1) (+ d p 1)]))))

(defn solve []
  (second (count-paths (input) "COM")))

(solve)
