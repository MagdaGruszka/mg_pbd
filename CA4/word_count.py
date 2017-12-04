FILE_NAME = 'jimmy.txt'

wordCounter = {}

with open(FILE_NAME,'r') as fh:
  for line in fh:
    # Replacing punctuation characters. Making the string to lower.
    # The split will spit the line into a list.
    word_list = line.replace(',','').replace('\'','').replace('.','').lower().split()
    for word in word_list:
      # Adding  the word into the wordCounter dictionary.
      if word not in wordCounter:
        wordCounter[word] = 1
      else:
        # if the word is already in the dictionary update its count.
        wordCounter[word] = wordCounter[word] + 1

print('{:15}{:3}'.format('Word','Count'))
print('-' * 18)

# printing the words and its occurrence.
for  (word,occurance)  in wordCounter.items(): 
  print('{:15}{:3}'.format(occurance, word))