(ns aoc (:require [clojure.string :as str]))

(load-file "processor-old.clj")

(defn input []
  (partition 3 (map
                (comp read-string str)
                (str/split-lines (with-out-str (aoc/run-file "13.txt"))))))

(get (frequencies (map #(nth % 2) (input))) 2)
