(ns aoc (:require [clojure.set]))

(def foods
  (->> (clojure.string/split-lines (slurp "21.txt"))
       (map #(clojure.string/split % #" \(contains |\)"))
       (map (juxt
             (comp set #(clojure.string/split % #" ") first)
             (comp set #(clojure.string/split % #", ") second)))))

(def ingredients
  (mapcat first foods))

(def allergens-possible-ingredients
  (->> foods
       (mapcat #(map hash-map (second %) (repeat (first %))))
       (apply merge-with clojure.set/intersection)))

;; part 1
(->> allergens-possible-ingredients
     (vals)
     (apply clojure.set/union)
     (clojure.set/difference (set ingredients))
     (select-keys (frequencies ingredients))
     (vals)
     (reduce +)
     (println))

;; part 2
(->> (loop [possible allergens-possible-ingredients
            assigned {}]
       (if (empty? possible)
         assigned
         (let [[allergen ingredients] (first (filter #(= 1 (count (val %))) possible))
               ingredient (first ingredients)]
           (recur
            (dissoc (zipmap (keys possible) (map #(disj % ingredient) (vals possible))) allergen)
            (assoc assigned ingredient allergen)))))
     (sort-by second)
     (map first)
     (clojure.string/join ",")
     (println))