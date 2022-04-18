#B877006 김윤성

# 최대 최소에 넣을 변수를 잡는다
largest=None
smallest=None

while True:
    num=input('Enter a number:')
    if num=='done':
        break
    else:
        
        try:
            num=int(num)#num이 INT형으로 변환되면 TRY 실행
            if largest==None:
                largest=num
            elif smallest==None:
                smallest=num
            elif largest<num:
                largest=num
            elif smallest>num:
                smallest=num
                
        except:
            print('Invalid input')#아니면 EXCEPT문 실
            continue
try:
    print('smallest=',smallest)
    print('largest=',largest)
except:
    pass
