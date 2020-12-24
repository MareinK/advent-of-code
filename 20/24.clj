(def deltas
  {:e {:xs [1 1] :y 0}
   :se {:xs [1 0] :y -1}
   :sw {:xs [0 -1] :y -1}
   :w {:xs [-1 -1] :y 0}
   :nw {:xs [0 -1] :y 1}
   :ne {:xs [1 0] :y 1}})

(def flip-deltas
  (->> (clojure.string/split-lines (slurp "24.txt"))
       (map #(->> (re-seq #"e|se|sw|w|nw|ne" %)
                  (map keyword)
                  (map deltas)))))

(defn apply-delta [{x :x y :y} {dxs :xs dy :y}]
  {:x (+ x (dxs (mod y 2))) :y (+ y dy)})

(def actives
  (->> (map (partial reduce apply-delta {:x 0 :y 0}) flip-deltas)
       (frequencies)
       (filter #(= 1 (mod (val %1) 2)))
       (map first)
       (set)))

;; part 1
(println (count actives))

(defn neighbors [tile]
  (map apply-delta (repeat tile) (vals deltas)))

(defn be-active [actives tile]
  (->> (neighbors tile)
       (filter actives)
       (count)
       ((if (actives tile) #{1 2} #{2}))))

(defn step [tiles]
  (->> (set (mapcat neighbors tiles))
       (filter (partial be-active tiles))
       (set)))

;; part 2
(-> (iterate step actives)
    (nth 100)
    (count)
    (println))
