import json

person ={
    'first_name':'Indrajeet',
    'last_name':'Happy',
    'age':32,
    'country': 'India',
    'is_married': 'yes',
    'skills': ['python','linux','storage','automation'],
    'address' : {
        'street': '1st Avenue,5th Main',
        'zipcode': '22334'
    }
}


#Removing Key and Value Pairs from a Dictionary

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# dct.pop('key1')
# print(dct)
#
# dct.popitem()
# print(dct)

del dct['key3']
print(dct)

# print(dct.items())
# print(dct.keys())
# print(dct.values())

# Merge 2 dictionary
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# #Method 1 using update()
# merge_dic = dict1.copy()
# merge_dic.update(dict2)
# print(merge_dic)

#method 2 using **unpacking
dict3 ={**dict1,**dict2}
print(dict3)

# Method 3: using | operator (Python 3.9+)
dict4 = dict2 | dict1

print(dict4)


