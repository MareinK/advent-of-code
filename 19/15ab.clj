(load-file "processor-old.clj")

(defn invert [step]
  (get {1 2, 2 1, 3 4, 4 3} step))

(defn find-goal [send recv]
  ; returns path to goal if goal is found,
  ; otherwise all possible paths through the space.
  ; assumption: initial state is not goal
  (loop [path []
         queue [path]
         paths [path]]
    (cond
      (empty? queue)
      paths
      (= path (peek queue))
      (recur
       path
       (into
        (pop queue)
        (map
         (partial conj path)
         (disj #{1 2 3 4} (invert (peek path)))))
       paths)
      (= path (take (count path) (peek queue)))
      (let [next (vec (take (inc (count path)) (peek queue)))]
        (send (peek next))
        (case (recv)
          0 (recur path (pop queue) paths)
          1 (recur next queue (conj paths next))
          2 next))
      :else
      (do
        (send (invert (peek path)))
        (recv)
        (recur (pop path) queue paths)))))

(let [[send recv] (aoc/run-file-async "15.txt")]
  (println (count (find-goal send recv)))
  (println (apply max (map count (find-goal send recv)))))
