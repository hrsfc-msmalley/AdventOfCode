import System.IO
import Data.List

sumGroups :: [String] -> [Int] -> [Int]
sumGroups [] ns = ns
sumGroups (x:xs) (n:ns)
  | x == "" = sumGroups xs (0:n:ns)
  | otherwise = sumGroups xs ((n + read x):ns)

main = do
  handle <- openFile "input.txt" ReadMode
  contents <- hGetContents handle
  let outputtop = sumGroups (lines contents) [0]
  print (take 1 (reverse (sort outputtop)))
  print (sum (take 3 (reverse (sort outputtop))))
  hClose handle
