;; old part 1

(def req-fields ["byr" "iyr" "eyr" "hgt" "hcl" "ecl" "pid"])

(println
 (let [input (clojure.string/split (slurp "4.txt") #"\n\n")]
   (->> (for [i input]
          (every?
           #(clojure.string/includes? i %)
           req-fields))
        (filter identity)
        (count))))

;; part 1+2

(ns aoc (:require [clojure.set]))

(def fields
  [{:name "byr"
    :match #"^(\d{4})$"
    :parse read-string
    :rules #(<= 1920 % 2002)}
   {:name "iyr"
    :match #"^(\d{4})$"
    :parse read-string
    :rules #(<= 2010 % 2020)}
   {:name "eyr"
    :match #"^(\d{4})$"
    :parse read-string
    :rules #(<= 2020 % 2030)}
   {:name "hgt"
    :match #"^(\d+)(cm|in)$"
    :parse #(list (read-string %1) %2)
    :rules #(case (second %)
              "cm" (<= 150 (first %) 193)
              "in" (<= 59 (first %) 76))}
   {:name "hcl"
    :match #"^(#[0-9a-f]{6})$"
    :parse identity
    :rules (constantly true)}
   {:name "ecl"
    :match #"^(\w*)$"
    :parse identity
    :rules #(contains? #{"amb" "blu" "brn" "gry" "grn" "hzl" "oth"} %)}
   {:name "pid"
    :match #"^(\d{9})$"
    :parse identity
    :rules (constantly true)}])

(def passports
  (for [passport (clojure.string/split (slurp "4.txt") #"\n\n")]
    (into {} (map (comp vec rest) (re-seq #"(\S*):(\S*)" passport)))))

(defn check-field [passport field]
  (some->> (get passport (:name field))
           (re-find (:match field))
           (rest)
           (apply (:parse field))
           ((:rules field))))

(defn check-passport [passport]
  (every? (partial check-field passport) fields))

(->> passports
     (filter #(clojure.set/subset?
               (set (map :name fields))
               (set (keys %))))
     (count)
     (println))

(->> passports
     (filter check-passport)
     (count)
     (println))
