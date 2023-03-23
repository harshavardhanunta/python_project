'''
# output [{'dir': '-build/sample.cpp', 'file': '-build/test/sample.h'}, {'dir': '-build/ sample2.h', 'file': 'sample2.h'}]
l = [{'dir' : '-build/test/sample.cpp',
      'file' : '-build/test/sample.h',},
     {'dir' : '-build/ sample2.cpp',
      'file' : 'sample2.h'}]
print(l)
for item in l:
    item['dir']=item['dir'].replace('/test/', '/')
    item['dir']=item['dir'].replace('2.cpp', '2.h')
print(l)


# Remove the dictionary if 'test' is present
l = [{'dir' : '-build/test/sample.cpp',
      'file' : '-build/test/sample.h',},
     
     {'dir' : '-build/ sample2.cpp',
      'file' : 'sample2.h'},

     {'dir' : '-build/sample.cpp',
      'file' : '-build/test/sample.h',},
     
     {'dir' : '-build/ sample2.cpp',
      'file' : 'sample2.h'}]
#print(l)

for i in l:
    if  'test' in i['dir']:
        l.remove(i)
print(l)

l1 = []
for i in l:
    if 'test' not in i['dir']:
        l1.append(i)
print(l1)


# JSON file
import json
# json string
employee = '{"id" : "02", "name" : "Nithin", "department" : "Finance"}'
employee_dict = json.loads(employee)
print(employee_dict)
print(employee_dict['name'])


import json
with open('emp_details.json', 'r') as f:
    data = json.load(f)
    f1 = open('emp_details1.json', 'a')
    for i in data['emp_details']:
        i = json.dumps(i)
        f1.write(i)
    f1.close()
'''
import json
with open('emp_details.json', 'r') as f:
    data = json.load(f)
    print(data)
