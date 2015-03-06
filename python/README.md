# Anagram Kata
This is a worked example in Python based upon the Anagram kata.

Run the tests with:

    python test-anagram.py
    
The source of the kata is the Dave Thomas' Anagram Kata that you can find [here](http://codekata.com/kata/kata06-anagrams/). You can also find out more about the London Code Dojo at our [homepage](http://www.meetup.com/London-Code-Dojo/).

The text of the kata at the link above is reproduced below:

# Kata: Anagrams
Let’s solve some crossword puzzle clues.

In England, I used to waste hour upon hour doing newspaper crosswords. As crossword fans will know, English cryptic crosswords have a totally different feel to their American counterparts: most clues involve punning or word play, and there are lots of anagrams to work through. For example, a recent Guardian crossword had:

	Down:
	..
	21. Most unusual form of arrest (6)

The hint is the phrase ‘form of,’ indicating that we’re looking for an anagram. Sure enough ‘arrest’ has six letters, and can be arranged nicely into ‘rarest,’ meaning ‘most unusual.’ (Other anagrams include raster, raters, Sartre, and starer)

A while back we had a thread on the Ruby mailing list about finding anagrams, and I’d like to resurrect it here. The challenge is fairly simple: given a file containing one word per line, print out all the combinations of words that are anagrams; each line in the output contains all the words from the input that are anagrams of each other. For example, your program might include in its output:

	kinship pinkish
	enlist inlets listen silent
	boaster boaters borates
	fresher refresh
	sinks skins
	knits stink
	rots sort

If you run this on the word list here you should find 20683 sets of anagrams (a total of 48162 words), including all-time favorites such as

	crepitus cuprites pictures piecrust
	paste pates peats septa spate tapes tepas
	punctilio unpolitic
	sunders undress

For added programming pleasure, find the longest words that are anagrams, and find the set of anagrams containing the most words (so “parsley players replays sparely” would not win, having only four words in the set).

## Kata Objectives
Apart from having some fun with words, this kata should make you think somewhat about algorithms. The simplest algorithms to find all the anagram combinations may take inordinate amounts of time to do the job. Working though alternatives should help bring the time down by orders of magnitude. To give you a possible point of comparison, I hacked a solution together in 25 lines of Ruby. It runs on this wordlist in 1.8s on a 1.7GHz i7. It’s also an interesting exercise in testing: can you write unit tests to verify that your code is working correctly before setting it to work on the full dictionary.

The source code and the materials are licensed under a Creative Commons License, see the LICENSE file for details.