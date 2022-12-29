'''
Exercises: Level 1
'''

'''
1. What is the most frequent word in the following paragraph?
'''

import re
from collections import Counter

paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something 
which can give you all the capabilities to develop an application what else can you love.'''

replace_dot = re.sub('\.','', paragraph)

paragraph_list = replace_dot.split()
common_word_paragraph = Counter(paragraph_list).most_common()

'''
Exercises: Level 2
Write a pattern which identifies if a string is a valid python variable
'''

def test_variable (variable):
    if re.findall('-',variable) or re.findall( '\d',variable) :
        return False
    else:
        return True

'''
Exercises: Level 3
'''

# Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding 
as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es 
thi%s mo@tivate yo@u to be a tea@cher!?'''

clean_sentence = re.sub('[$/%/@/&/#/;]','',sentence)

print(clean_sentence)

sentence_list = clean_sentence.split()
common_word_sentence = Counter(sentence_list).most_common()
