#b877006 김윤성 7-2번
count=0
Sum=0

fhand = open('mbox-short.txt')
for line in fhand:
     if line.startswith('X-DSPAM-Confidence'):
         line = line.rstrip()#\n 제거!
         count=count+1;
         atpos=line.find(':')# X-DSPAM-Confidence:이후를 찾는다.
         s=line[atpos+1:]#: 이후의 숫자를 s에 받는다.
        #s=line[20:]# X-DSPAM-Confidence이후를 슬라이싱 하는방법도 있다.
         
         Sum=Sum+float(s)
         
avg=Sum/count
print(avg)
print(type(line))
print(type(atpos))
