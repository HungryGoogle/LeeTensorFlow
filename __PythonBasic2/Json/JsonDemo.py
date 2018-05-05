import json

dic = {'age': 23, 'job': 'student'}
dic_str = json.dumps(dic)
print(type(dic_str), dic_str)
# out: <class 'str'> {"age": 23, "job": "student"}

dic_obj = json.loads(dic_str)
print(type(dic_obj), dic_obj)
# out: <class 'dict'> {'age': 23, 'job': 'student'}

