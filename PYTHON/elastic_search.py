from elasticsearch import Elasticsearch
es = Elasticsearch(['http://localhost:49154']) # connecting to elasticsearch
es.ping()


employees_data = [
    {
    'name': 'Vishnu',
    'age': 21,
    'programming_languages': ['C++', 'python', 'nodejs']
    },
    {
    'name': 'Sanjay',
    'age': 23,
    'programming_languages': ['python', 'C#']
    },
    {
    'name': 'Arjun',
    'age': 33,
    'programming_languages': ['C++', 'Ruby']
    },
    {
    'name': 'Ram',
    'age': 27,
    'programming_languages': ['Rust', 'python']
    }
]
for data in employees_data: es.index(index='employees', document=data)