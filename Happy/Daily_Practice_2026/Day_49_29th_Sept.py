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

# Accessing Dictionary Items
print(person['country'])
print(person['skills'][2])
print(person['address']['street'])

print(person.get('first_name'))
print(person.get('salary'))
print(person.get('CTC',0))


#Adding Items to a Dictionary

person['Job_Title']='Senior Consultant'
person['skills'].append('pytest')



# print(json.dumps(person,indent=4))


# Modifying Items in a Dictionary
person['first_name']= 'Shubham'
person['age'] = 29
print(json.dumps(person,indent=4))

# Removing Key and Value Pairs from a Dictionary

