#5명 성적 입력받고 함수를 이용해서 각각 최고점 최소점 평균을 구하는 함수 만들기
#사용자가 질문을 통해 최고점 최저점 평균 선택
def max_score(num):
    max_v = max(num)
    print("최고점:", max_v)

def min_score(num):
    min_v = min(num)
    print("최저점:", min_v)

def avg(num):
    average = sum(num) / len(num)
    print("평균:", average)

a = int(input("점수를 입력하세요: "))
b = int(input("점수를 입력하세요: "))
c = int(input("점수를 입력하세요: "))
d = int(input("점수를 입력하세요: "))
e = int(input("점수를 입력하세요: "))

num = [a, b, c, d, e]

while True:
    choice = int(input("검색하고 싶은 내용을 선택하세요 0:종료, 1:최고점, 2:최저점, 3:평균: "))
    if choice == 0:
         sys.exit()  # 프로그램 종료
    elif choice == 1:
        max_score(num)
    elif choice == 2:
        min_score(num)
    elif choice == 3:
        avg(num)
    else:
        print("잘못 입력했습니다.")
