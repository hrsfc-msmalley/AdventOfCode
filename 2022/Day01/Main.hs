import System.IO
import Data.List

sumGroups :: [String] -> [Int] -> [Int]
sumGroups [] ns = ns
sumGroups ("":xs) ns = sumGroups xs (0:ns)
sumGroups (x:xs) (n:ns) = sumGroups xs ((n + read x):ns)

main = do
  handle <- openFile "input.txt" ReadMode
  contents <- hGetContents handle
  let outputtop = sort (sumGroups (lines contents) [0])
  print (sum (take 1 (reverse (outputtop))))
  print (sum (take 3 (reverse (outputtop))))
  hClose handle
