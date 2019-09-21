import  xml.etree.ElementTree as ET
from pprint import pprint


tree = ET.parse('newsafr.xml')
root = tree.getroot()
xml_items = root.findall('channel/item/description')
word_more_6 = []
for item in xml_items:
    word = item.text.split()
    for str in word:
        if len(str) >= 6:
            word_more_6.append(str)
dict_word = {}
for i in word_more_6:
    if i in dict_word.keys():
        dict_word[i] += 1
    else:
        dict_word.setdefault(i)
        dict_word[i] = 1
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