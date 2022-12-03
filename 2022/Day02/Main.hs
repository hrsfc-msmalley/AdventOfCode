import System.IO
import Data.List

calculatescore1 :: String -> Int
calculatescore1 x
  | "A X" == x = 1 + 3
  | "A Y" == x = 2 + 6
  | "A Z" == x = 3 + 0
  | "B X" == x = 1 + 0
  | "B Y" == x = 2 + 3
  | "B Z" == x = 3 + 6
  | "C X" == x = 1 + 6
  | "C Y" == x = 2 + 0
  | otherwise = 3 + 3

calculatescore2 :: String -> Int
calculatescore2 x
  | "A X" == x = 0 + 3
  | "A Y" == x = 3 + 1
  | "A Z" == x = 6 + 2
  | "B X" == x = 0 + 1
  | "B Y" == x = 3 + 2
  | "B Z" == x = 6 + 3
  | "C X" == x = 0 + 2
  | "C Y" == x = 3 + 3
  | otherwise = 6 + 1


main = do
  handle <- openFile "input.txt" ReadMode
  contents <- hGetContents handle
  let inputList = lines contents
  let output1 = [calculatescore1 x | x <- inputList]
  print (sum output1)
  let output2 = [calculatescore2 x | x <- inputList]
  print (sum output2)
  hClose handle
