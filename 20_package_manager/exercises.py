'''
Exercises
'''
import numpy,webbrowser,pandas,requests,json,re

from collections import Counter

'''
1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
'''
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
romeo_and_juliet = response.text

romeo_and_juliet_list = romeo_and_juliet.split()

rj_frequent_words = Counter(romeo_and_juliet_list).most_common(10)

'''
2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
the min, max, mean, median, standard deviation of cats' weight in metric units.
the min, max, mean, median, standard deviation of cats' lifespan in years.
Create a frequency table of country and breed of cats
'''

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
cat_api_res = response.json()
cat_weight = []
cat_weight_metric = []
cat_weight_metric_split = []
cat_weight_metric_split_values = []

def cat_weight_func (variable): 
    for i in range(len(variable)):
        cat_weight.append(variable[i]['weight'])
    for i in range(len(cat_weight)):
        cat_weight_metric.append(cat_weight[i]['metric'])
    for i in cat_weight_metric:
        items_split= i.split()
        cat_weight_metric_split.append(items_split)
    for i in cat_weight_metric_split:
        del(i[1])
    # for i in cat_weight_metric_split:
    #     if index < cat_weight_metric_split_values[index]:
    #         index = 0
    #         index = index + 1
    #         value = 0
    #         cat_weight_metric_split_values.append(cat_weight_metric_split[index][value])
    #         value += 1
    #         cat_weight_metric_split_values.append(cat_weight_metric_split[index][value])
    #     return cat_weight_metric_split_values


print(cat_weight_func(cat_api_res))

