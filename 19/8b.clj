(ns aoc
  (:require [clojure.string :as str]))

(defn input []
  (map (comp read-string str) (slurp "8.txt")))

(def width 25)
(def height 6)

(let [image (->> (input)
                 (partition (* width height))
                 (apply (partial map vector))
                 (map (partial remove (partial = 2)))
                 (map first)
                 (map (partial get {0 " ", 1 "█"}))
                 (partition width))]
  (println (str/join "\n" (map str/join image))))
