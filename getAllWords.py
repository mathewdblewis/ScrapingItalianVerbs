import requests; import json

allWords = []
for letter in [chr(65+i) for i in range(26)]:
	x = requests.get('https://www.italian-verbs.com/?browse='+letter).text
	allWords += [t.split('100')[0] for t in x.split('lemma=')[1:]]

open('allWords.json','w').write(json.dumps(allWords))
