(load-file "processor-old.clj")

(let [program (assoc (aoc/instructions "17.txt") 0 2)
      [send recv] (aoc/run-async program)]
  (defn receive [m]
    (loop [n 1]
      (print (char (recv)))
      (when (< n m)
        (recur (inc n)))))
  (defn send_s [s]
    (dorun (for [c s] (send (int c)))))
  (receive 1981)
  (send_s "A,B,A,B,A,C,B,C,A,C\n")
  (receive 12)
  (send_s "L,10,L,12,R,6\n")
  (receive 12)
  (send_s "R,10,L,4,L,4,L,12\n")
  (receive 12)
  (send_s "L,10,R,10,R,6,L,4\n")
  (receive 23)
  (send_s "n\n")
  (receive 1976)
  (recv))

; A B A B A C B C A C

; L, 10
; L, 12I solved part 2 manually lol... not proud
; R, 6

; R, 10
; L, 4
; L, 4
; L, 12

; L, 10
; L, 12
; R, 6

; R, 10
; L, 4
; L, 4
; L, 12

; L, 10
; L, 12
; R, 6

; L, 10
; R, 10
; R, 6
; L, 4

; R, 10
; L, 4
; L, 4
; L, 12

; L, 10
; R, 10
; R, 6
; L, 4

; L, 10
; L, 12
; R, 6

; L, 10
; R, 10
; R, 6
; L, 4
