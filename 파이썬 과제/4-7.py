#b877006 김윤성
#성적 등급 표시 프로그램

def computergrade():
    try:
        Score=float(input("성적을 입력하세요:"))
        if Score<1.0 and Score>0.0: # 0.0과 1.0 사이의 점수를 입력받아야 함으로
                if Score>=0.9:
                    grade='A'
                elif Score>=0.8:
                    grade='B'
                elif Score>=0.7:
                    grade='C'
                elif Score>=0.6:
                    grade='D'
                elif Score<0.6:
                    grade='F'
        return grade  
    except:
        return "Bad Score"
           #print("Bad Score")
            
print(computergrade())
