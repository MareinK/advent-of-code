(ns aoc (:require [clojure.set]))

;; (defn pass-to-rowcol [pass]
;;   (as-> pass $
;;     (clojure.string/replace $ #"[FL]" "0")
;;     (clojure.string/replace $ #"[BR]" "1")
;;     (re-seq #".{1,7}" $)
;;     (map #(Integer/parseInt % 2) $)))

;; (defn pass-to-id [pass]
;;   (let [[row col] (pass-to-rowcol pass)]
;;     (+ (* 8 row) col)))

;; (def ids (->> (clojure.string/split (slurp "5.txt") #"\n")
;;               (map pass-to-id)
;;               (set)))

(def ids (->> (clojure.string/split (slurp "5.txt") #"\n")
              (map #(clojure.string/escape % {\F 0 \L 0 \B 1 \R 1}))
              (map #(Integer/parseInt % 2))
              (set)))

(def minid (apply min ids))
(def maxid (apply max ids))

(println maxid)
(-> (range minid maxid)
    (set)
    (clojure.set/difference ids)
    (first)
    (println))
