from nltk.corpus import stopwords
import json
import re


en_stops = set(stopwords.words('english'))
with open("news.json", "r") as read_file:
    data = json.load(read_file)
for d in data:
    s = d["text"].lower()
    a = s.split(' ')
    c = []
    for word in a: 
        word = re.sub(r'[^a-z0-9]', '', word)
        if word not in en_stops and word != '':
            c.append(word)
    a = ' '.join(c)

    s = d["title"].lower()
    a1 = s.split(' ')
    c = []
    for word in a1: 
        word = re.sub(r'[^a-z0-9]', '', word)
        if word != '':
            c.append(word)
    a1 = ' '.join(c)
    x = {
        'title': a1,
        'date': d["date"],
        'text': a,
        'url': d["url"]
    }
    with open("data_file.json", "a") as write_file:
        write_file.write('\n')
        json.dump(x, write_file)
        write_file.write(',')