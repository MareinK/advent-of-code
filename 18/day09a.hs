import Data.List.Index (insertAt, deleteAt)
import qualified Data.Map as Map
import Text.Regex.PCRE ((=~), getAllTextMatches)

import Debug.Trace

type Cycle a = (Int, [a])
type Scores = Map.Map Int Int

magic = 23
jump = -7

main = print . solve . parse =<< readFile "day09.txt"

parse :: String -> (Int, Int)
parse = (\[n, k] -> (n,k)) . map read . getAllTextMatches . (=~ "\\d+")

solve :: (Int, Int) -> Int
solve (n, k) = maximum $ Map.elems $ play (0, [0]) 1 where
    play :: Cycle Int -> Int -> Scores
    play s i
        | i == k + 1 = Map.fromList [(p, 0) | p <- [0..n-1]]
        | i `rem` magic == 0 = Map.adjust ((i + j) +) p (play t (i + 1))
        | otherwise = play (place i s) (i + 1)
        where
            p = ((i - 1) `rem` n)
            (j, t) = jumpPop jump s

place :: a -> Cycle a -> Cycle a
place a (i, l) = let j = (i + 2) `mod` length l in (j, insertAt j a l)

jumpPop :: Int -> Cycle a -> (a, Cycle a)
jumpPop k (i, l) = let j = (i + k) `mod` length l in (l !! j , (j, deleteAt j l))
