'''
Numpy

called numeric python. It is one of the most popular packages in machine learning and data science community.

'''

import numpy,webbrowser,pandas,requests

lst = [1,2,3,4,5]

np_arr = numpy.array(lst)

# print(np_arr * 2) # [ 2  4  6  8 10]


url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
# for url in url_lists:
#     webbrowser.open_new_tab(url)


##########################################################################

'''
Uninstalling Packages
If you do not like to keep the installed packages, you can remove them using the following command.

pip uninstall packagename


--------------------------------

List of Packages
To see the installed packages on our machine. We can use pip followed by list.

pip list

--------------------------------

Show Package
To show information about a package

pip show packagename

If we want even more details, just add --verbose

--------------------------------

PIP Freeze
Generate installed Python packages with their version and the output is suitable to use it in a requirements file. A requirements.txt file is a file that 
should contain all the installed Python packages in a Python project.

--------------------------------


'''

'''
Reading from URL
'''
# url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

# response = requests.get(url) # opening a network and fetching a data

# print(response)
# print(response.status_code) # status code, success:200
# print(response.headers)     # headers information
# print(response.text) # gives all the text from the page


'''
Let us read from an API. API stands for Application Program Interface. It is a means to exchange structure data between servers primarily a json data. An example of an API:https://restcountries.eu/rest/v2/all. Let us read this API using requests module.
'''

url = 'https://restcountries.com/v3.1/lang/spa'  # countries api language
response = requests.get(url)  # opening a network and fetching a data
# print(response) # response object
# print(response.status_code)  # status code, success:200
countries = response.json()
# print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries

