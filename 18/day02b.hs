main = print . solve . lines =<< readFile "day02.txt"

solve :: Eq a => [[a]] -> [a]
solve l = head $ ncommon (subtract 1 $ length $ head l) l

ncommon :: Eq a => Int -> [[a]] -> [[a]]
ncommon n l = filter ((n ==) . length) (commons l)

commons :: Eq a => [[a]] -> [[a]]
commons l = map (uncurry common) [(x,y) | x <- l, y <- l]

common :: Eq a => [a] -> [a] -> [a]
common x y = fst $ unzip $ filter (uncurry (==)) $ zip x y
