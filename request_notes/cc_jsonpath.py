import json
# import jsonpath
from jsonpath import jsonpath
import requests



cc_dict = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}

# cc_json = json.dumps(cc_dict)
# # print(cc_json)
# print(type(cc_json))
all_cc = jsonpath(cc_dict,'$.store.*')  #查看store节点下所有的值
print(all_cc)
print(jsonpath(cc_dict, '$..category'))  #查找cc_dict的category所有的值
print(jsonpath(cc_dict, '$.store.book[*].category'))  #查找book节点下所有子节点里的category的值
print(jsonpath(cc_dict, '$.store.book[*].isbn'))  #查找book节点下所有子节点里的category的值
print(jsonpath(cc_dict, '$.store.book[2].*'))  #查找book数组中第三个数组的所有值
print(jsonpath(cc_dict, '$.store.book[2].author'))  #查找book数组中第三个数组author的值

















# r = requests.get('')
# print(r.json())
# print(jsonpath.jsonpath(r.json(),'$.g.*'))