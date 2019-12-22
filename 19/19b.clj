(load-file "processor-old.clj")

(def program (aoc/instructions "19.txt"))

; (def X 118)
; (def Y 100)
; (def n 1)
; (def k 50)

; (for [y (range (* Y n) (+ k (* Y n)))]
;   (do
;     (dorun
;      (for [x (range (* X n) (+ k (* X n)))]
;    (let [[send recv] (aoc/run-async program)]
;          (send x)
;          (send y)
;          (print (recv)))))
;     (println)))

; (dorun
;  (println
;   (.lastIndexOf
;    (for [x (range 100)]
;    (let [[send recv] (aoc/run-async program)]
;        (send x)
;        (send 100)
;        (recv)))
;    1)))

; (dorun
;  (println
; ;   (.lastIndexOf
;   (.indexOf
;    (for [x (range 10000)]
;      (let [[send recv] (aoc/run-async program)]
;        (send x)
;        (send 10000)
;        (recv)))
;    1)))

; upper edge slope: 0.8938 (8938/10000)
; lower edge slope: 0.7187 (1787/10000)
; average slope: 0.80625

; (def y0 914)
; (def n 100)
; (def s 0.80625)

; (for [y (range y0 (+ n y0) 99)]
;   (do
;     (dorun
;      (for [x (range (* s y0) (+ n (* s   y0)))]
;        (let [[send recv] (aoc/run-async program)]
;          (send x)
;          (send y)
;          (print (recv)))))
;     (println)))

(defn get [x y]
  (let [[send recv] (aoc/run-async program)]
    (send x)
    (send y)
    (recv)))

(loop [x 0
       y 0]
  (let [a (get x y)
        a' (get (+100 x) y)
        b (get)]))
