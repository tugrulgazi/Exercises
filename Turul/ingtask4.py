# -*- coding: utf-8 -*-
s = str(input('Which fucking string do you wanna test: '))
slist=list(s.upper())
t=0
def balloon(a):
    global t
    try:
        for i in ['B','A','L','L','O','O','N']:
            a.remove(i)
        print(''.join(a))
        t+=1
        balloon(a)
        return t
    except:
        return t

print(balloon(slist))
        


        
        

    







