# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 20:42:03 2022

@author: stefa
"""

import bs4, requests, re, json, time

# A function to get the text from random wikipedia pages.
def get_tekst(url): 
    tekst = ''
    for paragraph in soup.findAll('p'): 
        tekst += paragraph.text
    # Regex to delete all links
    clean_tekst = re.sub(r'\[\d*\]','', tekst)
    clean_tekst_splitted = clean_tekst.title().split()
    append_to_dict(clean_tekst_splitted)     

words = {}

# A funtion which gets each word that comes after a word and saves it in a dictionary.
def append_to_dict(list_string):
    index = 0
    for chunk in list_string: 
        if index < len(list_string) - 1:
            next_word = list_string[index + 1]
            # If a word is not in the dict yet, it will be added.
            if chunk not in words.keys():
                words[chunk] = {next_word: 1}
            # If a word is already in the dict, it will either + the count by one, or it will be added as a new key.
            else:
                if next_word not in words[chunk].keys():
                    to_append = {next_word : 1}
                    words[chunk].update(to_append)
                else: 
                    words[chunk][next_word] += 1 
            index +=1
        else: 
            break    
    
count = 0

# while loop that gets the bs4 of a given number of pages.
while count < 15000: 
    time.sleep(0.05)
    print('Ronde nummer ' + str(count))
    url = 'https://nl.wikipedia.org/wiki/Special:Random'
    res = requests.get(url) 
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser') 
    get_tekst(url)
    count +=1

#Function to creates the most probable sentence.
def make_sentence(woord):
    global counts
    global sentence
    while counts < int(length):
        next_word_sentence = max(words[woord], key=words[woord].get)
        sentence += str(next_word_sentence.lower()) + ' '
        counts += 1
        make_sentence(next_word_sentence)
    
# A start of the program to give the user the feeling of control

print('Voor welk woord wil je een zin?')
woord = input()
print('Hoe lang wil je dat de zin wordt?')
length = input()
counts = 0  

sentence = woord + ' '

make_sentence(woord)
print(sentence)

# Last part to save file in a json so the dict can be used later.

tf = open("myDictionary.json", "w")
json.dump(words,tf)
tf.close()





