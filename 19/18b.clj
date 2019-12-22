(ns aoc (:require
         [clojure.string :refer [split-lines]]
         [clojure.set :refer [difference]]
         [clojure.data.priority-map :refer [priority-map]]))

(def enumerate (partial map-indexed vector))

(def world
  (into
   {}
   (for [[y, row] (enumerate (split-lines (slurp "18b.txt")))
         [x, val] (enumerate row)]
     [[x y] val])))

(def all-keys
  (set (filter #(Character/isLowerCase %) (map second world))))

(def dirs [[0 -1] [0 1] [-1 0] [1 0]])

(def start [(vec (map first (filter #(= (second %) \@) world)))
            #{}])

(defn goal? [[_ keys]] (= keys all-keys))

(defn succs [[poss keys]]
  (for [[i pos] (enumerate poss)
        pos' (map (comp vec (partial map + pos)) dirs)
        :when (and
               (not= \# (world pos'))
               (or
                (not (Character/isUpperCase (world pos')))
                (contains? keys (Character/toLowerCase (world pos')))))]
    [[(assoc poss i pos')
      (if (Character/isLowerCase (world pos'))
        (conj keys (world pos'))
        keys)]
     1]))

(defn heur [[_ keys]]
  (count (difference all-keys keys)))

(defn a-star [start goal? succs heur]
  (loop [queue (priority-map [start 0] 0)
         seen #{}]
    (if (empty? queue)
      nil
      (let [[[state cost] _ :as node] (first queue)]
        (when (= (mod (count queue) 5000) 0)
          (println (count queue) cost))
        ; (println "q" queue)
        ; (println "s" seen)
        ; (println "n" node)
        (cond
          (contains? seen state)
          (recur (pop queue) seen)
          (goal? state)
          cost
          :else
          (recur
           (into
            (pop queue)
            (for [[succ step] (succs state)]
              (do
                ; (println "   s" succ step)
                [[succ (+ cost step)] (+ cost step (heur succ))])))
           (conj seen state)))))))

(a-star start goal? succs heur)
