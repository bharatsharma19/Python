import json

"""
data = '{"var1":"Bharat" , "var2":64}'
print(data)

parsed = json.loads(data)
print(parsed['var1'])
# parsed1 = json.load(data)
# print(parsed1)
"""

data2 = {
    "Channel_name": "Mits",
    "Cars": ['Rolls royce', 'Lamborghini'],
    "Fridge": ('Roti', 'Liquor')
}

jscomp = json.dumps(data2)
print(jscomp)
