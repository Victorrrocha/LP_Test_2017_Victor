# my grammar

from pyparsing import Word, alphas, nums, OneOrMore

# define grammar
num = Word(nums)
date = num + "/" + num + "/" + num
schoolName = OneOrMore( Word(alphas) )
score = Word(nums)
schoolAndScore = schoolName + score
gameResults = date + schoolAndScore + schoolAndScore

# string to test grammar
results = "03/05/96 esem 100 cap 90"

# parse input string
print results, "->", gameResults.parseString(results)
