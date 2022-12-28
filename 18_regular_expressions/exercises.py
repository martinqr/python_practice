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
common_word = Counter(paragraph_list).most_common()


