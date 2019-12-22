{-# LANGUAGE RecordWildCards #-}

import Control.Monad
import Data.Either.Unwrap
import qualified Data.Map as Map
import Text.Parsec
import Text.Parsec.String

main = print . solve . map parseLine . lines =<< readFile "day03.txt"

data Rectangle = Rectangle {
    rid :: Int,
    x :: Int,
    y :: Int,
    w :: Int,
    h :: Int
} deriving (Show, Read)

parseLine :: String -> Rectangle
parseLine = fromRight . parse rectangle ""

rectangle :: Parser Rectangle
rectangle = do
    void $ string "#"
    id <- many1 digit
    void $ string " @ "
    x <- many1 digit
    void $ string ","
    y <- many1 digit
    void $ string ": "
    w <- many1 digit
    void $ string "x"
    h <- many1 digit
    return $ mkrect [id,x,y,w,h]
    
mkrect :: [String] -> Rectangle
mkrect xs = Rectangle {..} where
    [rid, x, y, w, h] = map read xs

type OverlapMap = Map.Map (Int,Int) Int

solve :: [Rectangle] -> Int
solve xs = rid $ head $ filter (nooverlap (rectcounts xs)) xs 

nooverlap :: OverlapMap -> Rectangle -> Bool
nooverlap m x = all (== 1) (Map.intersection m $ rectcount x)

rectcounts :: [Rectangle] -> OverlapMap
rectcounts xs = foldl1 (Map.unionWith (+)) (map rectcount xs)

rectcount :: Rectangle -> OverlapMap
rectcount r = Map.fromList [((x,y),1) | x <- [x r..x r+w r-1], y <- [y r..y r+h r-1]]
