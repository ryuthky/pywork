# -*- coding: utf-8 -*-
aaa=('A','B','C','D')
bbb=('1','2','3','4')
dic_out={}
for a in aaa:
    dic_in={}
    for b in bbb:
        dic_in.update({b:0})
    dic_out.update({a:dic_in})
print(dic_out)

dic_out['A']['1']='A1'
dic_out['A']['2']='A2'
dic_out['A']['3']='A3'
dic_out['A']['4']='A4'

print(dic_out)
print(dic_out.keys())
print(dic_out.items())