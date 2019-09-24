import json
from pprint import pprint


with open ('newsafr.json', encoding='utf-8') as newsafr_file:
    file = json.load(newsafr_file)
    # pprint(file)
file_dict = dict(file)
news = file_dict['rss']['channel']['items']
dict_word = {}
for i in news:
    str_news = i['description'].split()
    for str in str_news:
        if len(str) >= 6:
            str = str.lower()
            if str in dict_word.keys():
                dict_word[str] += 1
            else:
                dict_word.setdefault(str)
                dict_word[str] = 1
counter = 0
final_dict = {}
while counter < 10:
    counter += 1
    a = ()
    max_value = max(dict_word.values())
    ten_max_dict = {k: v for k, v in dict_word.items() if v == max_value}
    for i, n in ten_max_dict.items():
        a = i
    final_dict.update(ten_max_dict)
    dict_word.pop(a)
pprint(final_dict)