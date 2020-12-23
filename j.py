

'''import json

person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)


print( person_dict)
'''

'''
import json

person = {'name': 'Bob',
'age':10,
'domain': 'BA'
}

person_json = json.dumps(person)
print(person_json)'''

''''
import json
person = {'name': 'Bob',
'age':10,
'domain': 'BA'
}

with open('person.txt', 'w') as json_file:
    json.dumps(person, json_file)'''




