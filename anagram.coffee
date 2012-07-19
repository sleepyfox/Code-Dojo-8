fs = require 'fs'

readWordList = (fileName) ->
  try 
    data = fs.readFileSync fileName, 'ascii'
    # split the data into lines
    lines = data.split '\n'
    # remove trailing black line if present
    if lines[lines.length - 1] is ""
      lines.pop()
    lines
  catch err
    console.error "There was an error opening the file: #{fileName}"
    console.log err

sortedLetters = (word) ->    
  word.toLowerCase().split("").sort().join('')

anagrams = (word, wordList) ->
  matchedWords = []
  for checkWord in wordList
    if (sortedLetters(word) is sortedLetters(checkWord)) and (word isnt checkWord)
      matchedWords.push checkWord
  matchedWords

list = ['kinship', 'enlist', 'boaster', 'fresher', 'sinks', 'knits', 'rots' ]
dictionary = readWordList 'english_words.txt'
for word in list
  anagramList = (anagrams(word, dictionary)).join()
  console.log "#{word},#{anagramList}"

exports.readWordList = readWordList
exports.sortedLetters = sortedLetters
exports.anagrams = anagrams
