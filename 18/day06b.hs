main = print . solve . parse =<< readFile "day06.txt"

type Coord = (Int, Int)
type Bounds = (Int, Int, Int, Int)

n = 10000

parse :: String -> [Coord]
parse = map (read . ("(" ++) . (++ ")")) . lines

solve :: [Coord] -> Int
solve cs = length $ filter (< n) $ map (totalDist cs) $ coordsGrid cs

totalDist :: [Coord] -> Coord -> Int
totalDist cs c = sum $ map (dist c) cs

coordsGrid :: [Coord] -> [Coord]
coordsGrid cs = [(x,y) | x <- [x0..xn], y <- [y0..yn]] where
    (x0, xn, y0, yn) = bounds cs

bounds :: [Coord] -> Bounds
bounds cl = (minimum xs, maximum xs, minimum ys, maximum ys) where
    (xs, ys) = unzip cl

dist :: Coord -> Coord -> Int
dist (x1,y1) (x2,y2) = abs (x1 - x2) + abs (y1 - y2)
