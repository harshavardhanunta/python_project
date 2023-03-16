'''
l = [{'dir' :'-build/test/sample.cpp', 'file' : '-build/test/sample.h'},
      {'dir' : '-build/sample2.cpp','file' : 'sample2.h'}]
for item in l:
    item['dir']=item['dir'].replace('/test/','/')
    item['file']=item['file'].replace('2.h','/.')
print(l)'''


def sequare_list_elements(number):
    '''@args:
       @dics:
       @return:
    '''
    if type(number) == list: 
        num = []
        for elements in number:
            num.append(elements*2)
        return num
    else:
        print("enter the valide list")
number = ["suresh","janardhan","harsha"]
result = sequare_list_elements(number)
print(result)
























