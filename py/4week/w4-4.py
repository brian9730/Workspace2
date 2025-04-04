list1 = []
list2 = []

# 학생 정보 입력
for i in range(3):
    list1.append(input("이름 :"))
    kor = int(input("국어성적 :"))
    eng = int(input("영어성적 :"))
    math = int(input("수학성적 :"))

    list1.append(kor)
    list1.append(eng)
    list1.append(math)

    list2.append(list1)
    list1 = []


# 학생별 출력 함수
def score():
    total_kor = total_eng = total_math = 0

    for i in range(len(list2)):
        print("\n%d번째 학생" % (i + 1))
        print("%5s" % list2[i][0], end=" ")
        hap = 0
        for j in range(1, 4):
            print("%d" % list2[i][j], end=" ")
            hap += list2[i][j]
        print("-->합:%3d, 평균:%3.1f" % (hap, hap / 3))

        total_kor += list2[i][1]
        total_eng += list2[i][2]
        total_math += list2[i][3]

    # 과목별 총합 및 평균
    print("\n[과목별 총합 및 평균]")
    print("국어 총합: %3d, 평균: %4.1f" % (total_kor, total_kor / 3))
    print("영어 총합: %3d, 평균: %4.1f" % (total_eng, total_eng / 3))
    print("수학 총합: %3d, 평균: %4.1f" % (total_math, total_math / 3))

    # 전체 총합 및 평균
    total_all = total_kor + total_eng + total_math
    avg_all = total_all / 9
    print("\n전체 총합: %3d, 전체 평균: %4.1f" % (total_all, avg_all))


# 메뉴 루프
while True:
    print("\n[메뉴] 1.전체학생 출력  2.특정학생 성적변경  3.종료")
    choice = input("선택하세요: ")

    if choice == "1":
        score()

    elif choice == "2":
        name = input("점수를 변경할 학생 이름: ")
        for student in list2:
            if student[0] == name:
                print(f"현재 성적 - 국어: {student[1]}, 영어: {student[2]}, 수학: {student[3]}")
                print("변경할 과목을 선택하세요: 1.국어  2.영어  3.수학")
                subject_choice = input("선택: ")
                if subject_choice == "1":
                    student[1] = int(input("새 국어 점수: "))
                elif subject_choice == "2":
                    student[2] = int(input("새 영어 점수: "))
                elif subject_choice == "3":
                    student[3] = int(input("새 수학 점수: "))
                else:
                    print("잘못된 선택입니다.")
                break  # 학생을 찾았으니 반복 종료
        else:
            print("학생을 찾을 수 없습니다.")  # `for` 루프에서 `break`가 실행되지 않으면 실행됨

    elif choice == "3":
        print("프로그램 종료")
        break

    else:
        print("잘못된 메뉴 선택입니다.")
