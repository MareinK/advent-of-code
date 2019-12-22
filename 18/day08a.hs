import Data.List.Split

main = print . solve . parse =<< readFile "day08.txt"

parse :: String -> [Int]
parse = map read . splitOn " "

solve :: [Int] -> Int
solve = sum . fst . metadata

metadata :: [Int] -> ([Int], [Int])
metadata (0:n:xs) = splitAt n xs
metadata (k:n:xs) = (d1 ++ d2, r2) where
    (d1, r1) = metadata xs
    (d2, r2) = metadata (k-1:n:r1)
