import re

'''
To find a pattern we use different set of re character sets that allows to search for a match in a string.

re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string
'''

'''
Match

# syntac
re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
'''

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
# print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>

# We can get the starting and ending position of the match as tuple using span
span = match.span()
# print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
# print(start, end)  # 100 105
substring = txt[start:end]
# print(substring)       # first


txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
# print(match)  # None
# The string does not string with I like to teach, therefore there was no match and the match method returned None.



'''
Search
returns a match object with a first match that was found
'''

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
# print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
# print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
# print(start, end)  # 100 105
substring = txt[start:end]
# print(substring)       # first


'''
Find all
returns all the matches as a list
'''

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
# print(matches)  # ['language', 'language']


txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
# print(matches)  # ['Python', 'python']

# Since we are using re.I both lowercase and uppercase letters are included


'''
Replacing a substring
'''

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
# print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
# match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
# print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

'''
Let us add one more example. The following string is really hard to read unless we remove the % symbol. Replacing the % with an empty string will clean the text.
'''

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
# print(matches)

'''
Splitting Text Using RegEx Split
'''

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
# print(re.split('\n', txt)) # splitting using \n - end of line symbol

'''
Writing RegEx Patterns
'''
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '

regex_pattern = r'apple'
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']


'''
Square brackets []
'''

regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['Apple', 'banana', 'apple', 'banana']

'''
Escape character \
'''

regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['6', '2019', '8', '2021']

'''
Period(.)
'''
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

'''
Zero or more times (*)
'''
regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['and banana are fruits']

'''
Quantifier in RegEx
'''

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['6', '2019', '8', '2021']

'''
Cart ^
'''

# Starts with
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['This']


# Negation

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['6,', '2019', '8', '2021']