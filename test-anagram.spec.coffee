anagram = require './anagram'

readWordList = anagram.readWordList
anagrams = anagram.anagrams
sortedLetters = anagram.sortedLetters

describe 'Find an anagram', ->
  it 'should read lines from a file', ->
    count = 0
    list = readWordList 'test_list.txt'
    expect(list.length).toBe(10)

  it 'the sortedLetters of tea should be a e t', ->
    sorted = sortedLetters 'tea'
    expect(sorted).toBe('aet')
   
  it 'ate should have anagrams eat and tea', ->
    wordList = readWordList 'english_words.txt'  
    list = anagrams 'ate', wordList
    expect(list).toBeDefined()
    expect(list.length).toBe(2)
    expect(list.indexOf('eat')).not.toBe(-1)
    expect(list.indexOf('tea')).not.toBe(-1)

  it 'arrest should have anagram rarest', ->
    wordList = readWordList 'english_words.txt'
    list = anagrams 'arrest', wordList
    expect(list.length).toBe(4)
    expect(list.indexOf('rarest')).not.toBe(-1)