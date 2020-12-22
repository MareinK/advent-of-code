(def input
  (->> (clojure.string/split (slurp "22.txt") #"\n\n")
       (map #(->> (clojure.string/split-lines %)
                  (rest)
                  (map read-string)))))

(defn combat [decks]
  (if (= 1 (count decks))
    (first decks)
    (let [[winner & losers :as sorted-decks] (reverse (sort-by first decks))]
      (recur (cons
              (concat (rest winner) (map first sorted-decks))
              (filter seq (map rest losers)))))))

(defn recursive-combat
  ([decks]
   (:deck (recursive-combat decks #{})))
  ([[deck-1 deck-2] seen]
   (let [decks [deck-1 deck-2]
         [first-1 first-2 :as firsts] (map first decks)
         [rest-1 rest-2 :as rests] (map rest decks)]
     (cond
       (contains? seen decks) {:player 1 :deck deck-1}
       (empty? deck-1) {:player 2 :deck deck-2}
       (empty? deck-2) {:player 1 :deck deck-1}
       (every? identity (map #(<= %1 (count %2)) firsts rests))
       (let [winner (:player (recursive-combat (map #(take %1 %2) firsts rests) #{}))]
         (case winner
           1 (recur [(concat rest-1 [first-1 first-2]) rest-2] (conj seen decks))
           2 (recur [rest-1 (concat rest-2 [first-2 first-1])] (conj seen decks))))
       (> first-1 first-2) (recur [(concat rest-1 [first-1 first-2]) rest-2] (conj seen decks))
       (> first-2 first-1) (recur [rest-1 (concat rest-2 [first-2 first-1])] (conj seen decks))))))

(defn score [deck]
  (->> (reverse deck)
       (map * (range 1 ##Inf))
       (reduce +)))

;; part 1 + 2
(doseq [combat-fn [combat recursive-combat]]
  (->> (combat-fn input)
       (score)
       (println)))
