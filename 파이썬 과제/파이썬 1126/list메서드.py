Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[38,23,12,53]
>>> a
[38, 23, 12, 53]
>>> person=['yoonseong','male',1.5,180]
>>> person
['yoonseong', 'male', 1.5, 180]
>>> b=[]
>>> c=list()
>>> range(10)
range(0, 10)
>>> a=list(range(10))
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> b=list(range(5,12))
>>> b
[5, 6, 7, 8, 9, 10, 11]
>>> c=list(range(5,12,2))
>>> c
[5, 7, 9, 11]
>>> e=list(range(10,0,-1))
>>> e
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> year=[2015,2016,2017,2018,2019,2020,2021]
>>> year
[2015, 2016, 2017, 2018, 2019, 2020, 2021]
>>> population=[100,101,102,103,108,110,115]
>>> year[4:7]
[2019, 2020, 2021]
>>> population[4:7]
[108, 110, 115]
>>> year[-3:]
[2019, 2020, 2021]
>>> population[-3:]
[108, 110, 115]
>>> a=[1,20,3]
>>> a.append(500)
>>> a
[1, 20, 3, 500]
>>> len(a)
4
>>> a.append([500,600])
>>> a
[1, 20, 3, 500, [500, 600]]
>>> a.extend([500,600])
>>> a
[1, 20, 3, 500, [500, 600], 500, 600]
>>> a.insert(1,8000)
>>> a
[1, 8000, 20, 3, 500, [500, 600], 500, 600]
>>> a.insert(len(a),111)
>>> a
[1, 8000, 20, 3, 500, [500, 600], 500, 600, 111]
>>> a=[10,20,30]
>>> a.insert(1,[500,600])
>>> a
[10, [500, 600], 20, 30]
>>> a=[10,20,30]
>>> a.pop()
30
>>> a
[10, 20]
>>> a.remove(20)
>>> a
[10]
>>> a=[1,2,3,4]
>>> a.index(4)
3
>>> a=[1,1,1,1,1]
>>> a.count
<built-in method count of list object at 0x000001E0F28CA300>
>>> a.count(1)
5
>>> a=[1,2,3,4,5]
>>> a.reverse()
>>> a
[5, 4, 3, 2, 1]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5]
>>> a.sort(reverse=True)
>>> a
[5, 4, 3, 2, 1]
>>> #sort의 역순!
>>> a.sort(a,reverse=True)
a
print(a)
