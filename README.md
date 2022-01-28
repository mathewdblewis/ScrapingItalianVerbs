PURPOSE:
  this code scrapes all the Italian verbs from this site:
  https://www.italian-verbs.com/
  so that they can be put into a quizlet flashcard set

HOW TO USE THIS CODE:
  first run getAllWords.py
  this will create allWords.json
  then run getData.py
  this will create allData.json
  _allWords.json is what I got for allWords.json, so mine (_allWords.json) should be the same as yours (allWords.json)
  similarly for allData.json

WHAT THE CODE PRODUCES:
  allWords.json is a json formatted list of all the words (verbs) that are on the website
  allData.json is a json file that represents a dictionary
  the format is as follows: dic[word][mood][tense]
  for example, dic[ABALIENARE][INDICATIVO][PRESENTE] =
    ["io abalieno","tu abalieni","lui/lei abaliena","noi abalieniamo","voi abalienate","loro abalienano"]

NOTE:
  strings such as \u00f2 represent a non ascii character
  you can google \u00f2 and find out what it is (its a ò)

RECOMMENDATION:
  try building this yourself, and look at my code for guidance as needed

