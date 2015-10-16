fs = require 'fs'

readWordList = (fileName) ->
  try
    data = fs.readFileSync fileName, 'ascii'
    # split the data into lines
    lines = data.split '\n'
    # remove trailing blank line if present
    if lines[lines.length - 1] is ""
      lines.pop()
    lines
  catch err
    console.error "There was an error opening the file: #{fileName}"
    console.log err

sortedLetters = (word) ->
  word.toLowerCase().split("").sort().join('')

anagrams = (word, wordList) ->
  sorted_word = sortedLetters(word)
  wordList.filter (x) ->
    (sorted_word is sortedLetters(x)) and (x isnt word)

list = ['kinship', 'enlist', 'boaster', 'fresher', 'sinks', 'knits', 'rots' ]
dictionary = readWordList 'english_words.txt'
for word in list
  anagramList = (anagrams(word, dictionary)).join()
  console.log "#{word},#{anagramList}"

module.exports =
  readWordList: readWordList
  sortedLetters: sortedLetters
  anagrams: anagrams
