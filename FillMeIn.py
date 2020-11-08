import textstat

# Take in a paragraph and difficulty level, return list of difficult words 
def complexityFunction(text, level):
	words = []
	words = text.split()
	selectedWords = []
	for i in words:
		if(textstat.flesch_reading_ease(i) <= level):
			selectedWords.append(i)
	return selectedWords

#Set default language to english
textstat.set_lang("en")

# Create empty string array
sentences = []

# Select word blank selection complexity 1 - 5
print("Please enter blank selection complexity (1 - 5): ")
level = int(input())


# Keyboard input from command line
print("Please enter text:")
text = input()


# Split paragraph into sentences separated by '.'
text.replace("!", ".")
text.replace("?", ".")
text.replace(";", ".")
text.replace(":", ".")
sentences = text.split(".")


print("\n")

for sentence in sentences:
  complexWords = complexityFunction(sentence, 100/level)
  print(complexWords)
  words = sentence.split()
  for word in words:
    if word in complexWords:
      print("_____", end = " ")
    else:
      print(word, end = " ")
  print("\n")


  
