

def max_score(num):
    max_v = max(num)
    print("최고점:", max_v)

def min_score(num):
    min_v = min(num)
    print("최저점:", min_v)

def avg(num):
    average = sum(num) / len(num)
    print("평균점:", average)

# 점수들을 리스트에 저장
num = []
for i in range(5):  # 5명 점수 입력
    score = int(input(f"{i+1}번 학생의 점수를 입력하세요: "))
    num.append(score)

while True:
    choice = int(input("검색하고 싶은 내용을 선택하세요 0:종료, 1:최고점, 2:최저점, 3:평균: "))
    if choice == 0:
        break  # 프로그램 종료
    elif choice == 1:
        max_score(num)  # 리스트에 저장된 점수로 함수 호출
    elif choice == 2:
        min_score(num)  # 리스트에 저장된 점수로 함수 호출
    elif choice == 3:
        avg(num)  # 리스트에 저장된 점수로 함수 호출
    else:
        print("잘못 입력했습니다.")
