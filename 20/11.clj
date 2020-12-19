;; general helpers

;; (defn drop-nth [n coll]
;;   (concat
;;    (take n coll)
;;    (drop (inc n) coll)))

(defn take-while-different [coll]
  (->> coll
       ((juxt (constantly [nil]) identity))
       (apply concat)
       ((juxt identity rest))
       (apply map vector)
       (take-while (partial apply not=))
       (map second)))

;; matrix helpers

;; (defn border-matrix [el matrix]
;;   (let [el-row (repeat (count (first matrix)) el)]
;;     (->> (concat [el-row] matrix [el-row])
;;          (map #(concat [el] % [el])))))

(defn map-2d [f & colls]
  (apply map (partial map f) colls))

(defn transpose [matrix]
  (apply map vector matrix))

;; (defn partition-2d [n step matrix]
;;   (->> (partition n step matrix)
;;        (map transpose)
;;        (map (partial partition n step))
;;        (map-2d transpose)))


(defn dimensions [matrix]
  [(count matrix) (count (first matrix))])

(defn get-rows [matrix]
  matrix)

(defn get-cols [matrix]
  (apply map vector matrix))

(defn get-diags-1 [matrix]
  (let [n (->> (dimensions matrix) (apply +) (dec))]
    (for [x (range n)]
      (map-indexed #(get %2 (- x %1)) matrix))))

(defn get-diags-2 [matrix]
  (get-diags-1 (transpose (reverse matrix))))

;; puzzle helpers

(defn seat-frequencies [seats]
  (let [[width height] [(count (first seats)) (count seats)]
        rows (mapcat (partial repeat width) (get-rows seats))
        cols (apply concat (repeat height (get-cols seats)))
        diags-1 (apply concat (partition width 1 (get-diags-1 seats)))
        diags-2 (reverse (mapcat reverse (partition height 1 (get-diags-2 seats))))]
    (->> (map list rows cols diags-1 diags-2)
        ;;  (map (partial apply concat))
        ;;  (map (partial filter identity))
        ;;  (partition width)
        ;;  (map-2d frequencies)
         )))

;; (defn seat-frequencies [check-dist seats]
;;   (->> (border-matrix \. seats)
;;        (partition-2d 3 1)
;;        (map-2d flatten)
;;        (map-2d (partial drop-nth 4))
;;        (map-2d frequencies)))

(def seat-rules
  {\. (partial > 0)
   \L (partial = 0)
   \# (partial <= (+ 5 4))})

(defn change-seat [x]
  (get {\L \#, \# \L} x))

(defn step-seat [x freqs]
  (let [seat-rule (seat-rules x)
        freq (get freqs \# 0)]
    (if (seat-rule freq) (change-seat x) x)))

(defn step-seats [seats]
  (map-2d step-seat seats (seat-frequencies seats)))

;; puzzle part 1 + 2

(def input (map list* (clojure.string/split-lines (slurp "11.txt"))))
;; (def input (clojure.string/split-lines (slurp "11.txt")))

;; (-> (iterate (partial step-seats) input)
;;     (take-while-different)
;;     (last)
;;     (flatten)
;;     (frequencies)
;;     (get \#)
;;     (println))

(-> input
    (step-seats)
    (seat-frequencies)
    ;; (step-seats)
    (println))

;; (-> [[1 0 0 0]
;;      [0 0 0 0]
;;      [0 0 0 0]
;;      [0 0 0 16]
;;      [0 0 0 16]]
;;     (seat-frequencies)
;;     (println))
