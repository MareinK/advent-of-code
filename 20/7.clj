(ns aoc (:require [clojure.set]))

(def parents (->> (clojure.string/split (slurp "7.txt") #"\n")
                  (map #(let [[color colorsstr] (rest (re-find #"(.*) bags contain (.*)" %))
                              colors (map second (re-seq #"\d+ (.*?) bag" colorsstr))]
                          (apply hash-map (interleave colors (repeat #{color})))))
                  (apply merge-with clojure.set/union)))

(defn ancestors [color]
  (->> (get parents color)
       (map ancestors)
       (apply clojure.set/union (clojure.set/union (get parents color)))))

(->> "shiny gold"
     (ancestors)
     (count)
     (println))

;; part 2

(def children (->> (clojure.string/split (slurp "7.txt") #"\n")
                   (map #(let [[color colorsstr] (rest (re-find #"(.*) bags contain (.*)" %))
                               colorstrs (map rest (re-seq #"(\d+) (.*?) bag" colorsstr))
                               colors (map (juxt (comp read-string first) (comp identity second)) colorstrs)]
                           {color colors}))
                   (apply merge)))

(defn descendants [[count color]]
  (->> (get children color)
       (map #(repeat (first %) %))
       (apply concat)
       (map descendants)
       (apply concat (get children color))))

(->> [1 "shiny gold"]
     (descendants)
     (map first)
     (reduce +)
     (println))

;; cleaned

(def bags-graph
  (->> (clojure.string/split-lines (slurp "7.txt"))
       (mapcat #(let [[name-a colors-str] (clojure.string/split % #" bags contain ")]
                  (for [[count-b name-b] (map rest (re-seq #"(\d+) (.*?) bag" colors-str))]
                    {name-a {:children [{:name name-b :count (read-string count-b)}]}
                     name-b {:parents [{:name name-a :count 1}]}})))
       (apply merge-with (partial merge-with concat))))

(def reachable
  (memoize
   (fn [graph edge-type node]
     (->> (get graph node)
          (edge-type)
          (mapcat #(repeat (:count %) (:name %)))
          ((juxt identity (partial mapcat (partial reachable graph edge-type))))
          (apply concat)))))

(doseq [[relation coll-type] [[:parents set] [:children list*]]]
  (->> (reachable bags-graph relation "shiny gold")
       (coll-type)
       (count)
       (println)))


;; (ns aoc
;;   (:require [clojure.edn :as edn]
;;             [clojure.string :as str]
;;             [clojure.spec.alpha :as s]
;;             [clojure.spec.gen.alpha :as gen]))

;; (s/def ::rule
;;   (s/cat
;;    :name ::name
;;    :str1 #{'bags}
;;    :str2 #{'contain}
;;    :bags ::bag-list))

;; (s/def ::bag-list
;;   (s/alt
;;    :single ::bag
;;    :multiple (s/cat :bag ::bag :comma #{(quote ",")} :bags ::bag-list)))

;; (s/def ::bag
;;   (s/alt
;;    :singular
;;    (s/cat :count #{1}
;;           :name ::name
;;           :bags #{'bag})
;;    :plural
;;    (s/cat :count (s/int-in 2 6)
;;           :name ::name
;;           :bags #{'bags})))

;; (s/def ::name
;;   (s/cat
;;    :adjective #{'posh 'drab 'shiny 'dim 'pale 'muted 'dull 'dotted 'light 'wavy 'bright 'vibrant 'dark 'mirrored 'faded 'plaid 'striped 'clear}
;;    :color #{'violet 'yellow 'gold 'gray 'green 'beige 'white 'orange 'black 'maroon 'crimson 'teal 'turquoise 'lavender 'cyan 'purple 'olive 'brown 'coral 'salmon 'red 'aqua 'magenta 'blue 'bronze 'tomato 'lime 'fuchsia 'indigo 'plum 'chartreuse 'tan 'silver}))

;; (-> (s/gen ::rule)
;;     (gen/sample)
;;     (println))

;; (->> (slurp "7.txt")
;;      (str/split-lines)
;;      (mapv #(let [edn (edn/read-string (format "[%s]" %))]
;;               (s/conform ::rule edn)))
;;      (println))

;; (println (s/conform ::rule (edn/read-string "[clear black bags contain 1 clear coral bag , 1 wavy bronze bag]")))




;; (ns aoc
;;   (:require [instaparse.core :as insta]))

;; (def as-and-bs
;;   (insta/parser
;;    "S = AB*
;;      AB = A B
;;      A = 'a'+
;;      B = 'b'+"))

;; (println (as-and-bs "aaaaabbbaaaabb"))
