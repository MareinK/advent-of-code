import Control.Monad
import Data.List.Split

main = print . solve . parse =<< readFile "day08.txt"

data Node = Node ([Int], [Node]) deriving Show

parse :: String -> Node
parse = tree . map read . splitOn " "

tree :: [Int] -> Node
tree = fst . helper where
    helper :: [Int] -> (Node, [Int])
    helper (0:n:xs) = (Node (take n xs, []), drop n xs)
    helper (k:n:xs) = (Node (d, c:cs), r2) where
        (c, r1) = helper xs
        (Node (d, cs), r2) = helper (k-1:n:r1)

solve :: Node -> Int
solve = value

value :: Node -> Int
value (Node (xs, [])) = sum xs
value (Node (xs, cs)) = sum $ map (value . (cs !!)) indices where
    indices = [x | x <- map (subtract 1) xs, x >= 0, x < length cs ]
