(ns aoc
  (:require [clojure.string :as str]
            [clojure.core.async :refer [alt!! >!!]]))

(load-file "processor-old.clj")

(defn rotate [[x y] r]
  (case r
    0 [(- y) x]
    1 [y (- x)]))

(defn render [panels]
  (let [xs (map first (keys panels))
        ys (map second (keys panels))
        min-x (apply min xs) max-x (apply max xs)
        min-y (apply min ys) max-y (apply max ys)]
    (str/join
     "\n"
     (for [y (range max-y (- min-y 1) -1)]
       (apply str
              (for [x (range min-x (+ max-x 1))]
                (get {0 " " 1 "█"} (get panels [x y] 0))))))))

(defn paint [initial]
  (let [[send recv wait] (aoc/run-file-async "11.txt")
        result (atom nil)]
    (go
      (loop [panels initial
             pos [0 0]
             dir [0 1]]
        (reset! result panels)
        (send (get panels pos 0))
        (let [color (recv)
              heading (recv)
              new-dir (rotate dir heading)]
          (recur
           (assoc panels pos color)
           (map + pos new-dir)
           new-dir))))
    (wait)
    @result))

; (defn paint [initial]
;   (let [[c-in c-out c-res] (aoc/run-file-async "11.txt")
;         panels (atom initial)
;         pos (atom [0 0])
;         dir (atom [0 1])]
;     (loop []
;       (alt!!
;         c-out ([color]
;                (do (if (= val "input")
;                      (>!! c-in (get panels pos 0))
;                      (do
;                        (<!! c-out)
;                        (let [heading (<!! c-out)])))
;                    (recur)))
;         c-res :done))))

(println (count (paint {})))
(println (render (paint {[0 0] 1})))

; (println (paint {[0 0] 1}))
