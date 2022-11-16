#1

my_list = []

#2

my_colors = ['red','blue','yellow','black','white']

#3

len(my_colors)

#4

my_colors[0]
my_colors[2]
my_colors[4]

#5

mixed_data_types = ['name','age','height','marital status','address']

#6

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#7

# print(it_companies)

#8

# print(len(it_companies))

#9

# print(it_companies[0])
# print(it_companies[3])
# print(it_companies[6])

#10

# it_companies[0] = 'Space X'
# print(it_companies) 

#11

# it_companies.append('Globant')
# print(it_companies) #add a company to it_companies.

#12

# it_companies.insert(3,'Samsung')
# print(it_companies) #add a company in the middle of it_companies

#13

# it_companies[2] = it_companies[2].upper()

# print(it_companies)

#14

# it_companies.extend(['#; '])

# print(it_companies)

#15

# print(it_companies.index('Googale')) #returns the index of an item in the list, if doesnt exist return Value error

#16

# it_companies.sort()
# print(it_companies) #return the list it_companies sorted alphabetical

#17

# it_companies.reverse()
# print(it_companies) #return the list it_companies reversed.

#18

# print(it_companies[3:])

#19

# print(it_companies[:-3])

#20

# print(it_companies[::2])

#21

# it_companies.remove('Facebook')
# print(it_companies)

#22

# it_companies.remove('Apple')
# print(it_companies)

#23

# it_companies.remove('Amazon')
# print(it_companies)

#24

# it_companies.clear()
# print(it_companies) #clear all the items in a list

#25

del it_companies

#26

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

# print(front_end + back_end)

#27

full_stack = front_end + back_end + ['Python','SQL']

# print(full_stack)

### ///////////////////////////////////////////////////////////////////// ###

#1

#Sort the list and find the min and max age

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

# print(max(ages)) #max age
# print(min(ages)) #min age

#Add the min age and the max age again to the list

max_age = max(ages)
min_age = min(ages)

ages.append(max_age)
ages.append(min_age)

print(ages)

#Find the median age (one middle item or two middle items divided by two)

median_age = ((max_age - min_age) / 2) + min_age

# print(median_age)

# Find the average age (sum of all items divided by their number )

average_age = sum(ages)

# print(average_age)

# Find the range of the ages (max minus min)

range_ages = [min_age,max_age]

# print(range_ages)

# Compare the value of (min - average) and (max - average), use abs() method

# print(abs(max_age) , abs(min_age))

### ///////////////////////////////////////////////////////////////////// ###

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

# Find the middle country(ies) in the countries list

# print(countries[int(len(countries) / 2)]) # Lesotho == countries[96]
# print(countries.index('Lesotho'))  #Return 96


# Divide the countries list into two equal lists if it is even if not one more country for the first half.

countries_list_first_half = countries[:int(len(countries) / 2)]
countries_list_second_half = countries[int(len(countries) / 2):]

# print(len(countries_list_first_half))
# print(len(countries_list_second_half))

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as scandic countries.

countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first_three_countries = countries_list[0:3]
scandic_countries = countries_list[3:]

print(first_three_countries)
print(scandic_countries)


















