{-# LANGUAGE TupleSections #-}

import qualified Data.Map as Map

main = print . checksum . lines =<< readFile "day02.txt"

checksum :: Ord a => [[a]] -> Int
checksum l = product $ map (countndups l) [2, 3]

countndups :: Ord a => [[a]] -> Int -> Int
countndups l i = length $ filter (containsndups i) l

containsndups :: Ord a => Int -> [a] -> Bool
containsndups i l = elem i $ Map.elems $ counter l

counter :: Ord a => [a] -> Map.Map a Int
counter = Map.fromListWithKey (const (+)) . map (, 1)
