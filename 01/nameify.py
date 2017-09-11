word = "taco shell"

split = word.split(' ')
# splits words by spaces

word_upper = split[0].capitalize() + " " + split[1].capitalize()
# capitalizes each word and puts them back together

print (word_upper)
