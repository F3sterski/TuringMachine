__author__ = 'Adam Zielke'

import xml.etree.ElementTree as ET

tree = ET.parse('program.xml')
root = tree.getroot()
alphabet = root.find('alphabet').text.split(' ')
word = raw_input("Please input word: ")
word = list(word)
print word[0]
sum = 0
for i in range(len(alphabet)):
    sum += word.count(alphabet[i])
if sum is not len(word):
    print "word contains letters that not exist in alphabet"
    exit()
head = []
state = root.find('start').text
end = root.find('end').text
index = 0
letter_before = word[0]
letter = ""
while state != end:
    direction = root.findall("./delta/"+state+"/"+letter_before+"/direction")[0].text
    letter = root.findall("./delta/"+state+"/"+letter_before+"/alphabet")[0].text
    state = root.findall("./delta/"+state+"/"+letter_before+"/move")[0].text
    if direction == 'L':
        index -= 1
    elif direction == 'R':
        index += 1
    if index >= len(word):
        word.append('B')
    print direction + " " + letter + " " + state + " " + str(index) + " " + str(len(word))
    letter_before = word[index]
    word[index] = letter
    print word
print word
