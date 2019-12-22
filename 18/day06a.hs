import Data.List.Extra
import Data.Maybe
import GHC.Exts

main = print . solve . parse =<< readFile "day06.txt"

type Coord = (Int, Int)
type Bounds = (Int, Int, Int, Int)

parse :: String -> [Coord]
parse = map (read . ("(" ++) . (++ ")")) . lines

solve :: [Coord] -> Int
solve cs = maximum . map length . group . sort . finiteAreas $ pureNearest cs

pureNearest :: [Coord] -> [Coord]
pureNearest = map fromJust . filter isJust . nearestGrid

nearestGrid :: [Coord] -> [Maybe Coord]
nearestGrid cs = map (nearest cs) $ coordsGrid cs

coordsGrid :: [Coord] -> [Coord]
coordsGrid cs = [(x,y) | x <- [x0..xn], y <- [y0..yn]] where
    (x0, xn, y0, yn) = bounds cs

bounds :: [Coord] -> Bounds
bounds cl = (minimum xs, maximum xs, minimum ys, maximum ys) where
    (xs, ys) = unzip cl

nearest :: [Coord] -> Coord -> Maybe Coord
nearest cs c = if length winners == 1 then Just $ snd $ head winners else Nothing where
    winners = head $ groupOn fst $ sort $ map ((,) =<< dist c) cs

dist :: Coord -> Coord -> Int
dist (x1,y1) (x2,y2) = abs (x1 - x2) + abs (y1 - y2)

finiteAreas :: [Coord] -> [Coord]
finiteAreas cs = filter (not . flip elem (boundaryCoords cs)) cs

boundaryCoords :: [Coord] -> [Coord]
boundaryCoords cs = filter (\(x,y) -> x == x0 || x == xn || y == y0 || y == yn) cs where
    (x0, xn, y0, yn) = bounds cs
