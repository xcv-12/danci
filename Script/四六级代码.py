# -*- coding: cp936 -*-
import linecache
o=open('����������.csv')#�ļ�·��
o.seek(0)
r=o.readlines()
s1=str(input('����Ҫ��λ����Ϣ:'))
a=0
count=0
for i in r: #����ֵ��ϲ���
    if i.find(s1)>=0:       
        print(i)#��ʾ��λ��
        
    
