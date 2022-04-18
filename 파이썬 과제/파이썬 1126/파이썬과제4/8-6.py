#b877006 김윤성 8-6번
# 최대 최소에 넣을 변수를 잡는다

x=list()
while True:
    num=input('Enter a number:')
    if num=='done':
        break
    else:
        x.append(float(num))# x리스트에 float으로 변형한 num을 넘긴다.
        #print(x)
def max():
    largest=None
    for Number in x:
        if largest==None:
                largest=Number
        elif largest<Number:
                largest=Number
    print('Maximum:',largest)
def min():
    smallest=None
    for Number in x:
        if smallest==None:
                smallest=Number
        elif smallest>Number:
                smallest=Number
    print('Minimum:',smallest)

max()
min()






