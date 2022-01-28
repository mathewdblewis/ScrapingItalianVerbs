import requests; import json


dic = {}

allWords = json.loads(open('allWords.json','r').read())

for word in allWords:
	dic[word] = dict()
	html = requests.get('https://www.italian-verbs.com/?lemma='+word+'100').text
	x = [t.split('\n')[0] for t in html.split('<tr')[7:]]
	x = [t for t in x if 'lemma' not in t and len(t)>40]
	x = [t.split('</td')[0] for t in x]
	x = ['>'.join(t.split('>')[2:]) for t in x]
	x = [''.join(t.split('</span>')) for t in x]
	x = '\n'.join(x).split('<span class="modo">')
	A,B = x[:-3],x[-3:]
	A[0] = 'INDICATIVO\n'+A[0]

	for a in A:
		a = a.split('\n')
		body = '\n'.join(a[1:])
		D = {}
		for b in body.split('<span class="tempo">')[1:]:
			q = [t for t in b.split('\n') if t != '']
			D[q[0]] = q[1:]
		dic[word][a[0]] = D

	for b in B:
		b = b.split('\n')
		title,body = b[0],'\n'.join(b[1:])
		body = ''.join(body.split('&nbsp; '))
		body = ''.join(body.split('</b> '))
		body = ''.join(body.split('<b>'))
		body = [t.split(':') for t in body.split('\n') if t!='']
		dic[word][title] = {}
		for q in body: dic[word][title][q[0]] = [q[1]]


open('allData.json','w').write(json.dumps(dic))


