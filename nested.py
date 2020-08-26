# Exercise 6
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:
d1 = {'simple_key': 'hello'}

d2 = {'k1': {'k2': 'hello'}}

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}

d1.get('simple_key')
d2['k1']['k2']
d3['k1'][0]['nest_key'][1]

