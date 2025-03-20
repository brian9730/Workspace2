#자동차 경주 프로그램
from turtle import *  # turtle 모듈을 가져옴
import random  # random 모듈을 가져옴

class Car:  # 자동차 클래스를 정의함
    def __init__(self, speed, color, fname, locate, goal):  
        self.speed = speed  
        self.color = color
        self.turtle = Turtle() 
        self.turtle.shape(fname)  
        self.turtle.speed(self.speed)  
        self.locate = locate  
        self.goal = goal   
        
    def drive(self, distance):  # 자동차 주어진 거리만큼 이동시키는 함수
        self.turtle.forward(distance)

    def goto(self, x, y):  # 자동차 특정 좌표로 이동시키는 함수
        self.turtle.goto(x, y)

    def turnleft(self, degree):  # 자동차 방향을 회전시키는 함수
        self.turtle.left(degree)

    def write(self, write):  # 화면에 검은선을 표시하는 함수
        self.turtle.write(write)

    def hide(self):  # 자동차 숨기는 함수
        self.turtle.hideturtle()

register_shape("car2.gif")  # 자동차 이미지 등록

car_list = []  # 자동차 객체를 저장할 리스트 생성
y = -100  # 초기 y 좌표 설정
n = 0  # 순위 변수 

for i in range(3):  # 3개의 자동차 객체를 생성
    car_list.append(Car(10, "red", "car2.gif", -400, 0))

for car in car_list:  # 각 자동차를 초기 위치에 배치
    car.turtle.penup()  # 펜 들어서 이동
    car.goto(-400, y)  # x는 고정, y = -100, 0, 100 위치로 이동
    car.turtle.pendown()  # 펜 내려서 쓰기
    y += 100  # 다음 자동차를 위로 100만큼 이동

for i in range(400):  # 자동차 경주 시작 (최대 400번)
    for car in car_list:  # 모든 자동차에 대해 실행
        speed = random.randint(2, 20)  # 랜덤한 속도(2~20)
        if car.locate < 400:  # 자동차가 도착 지점에 도착하지 않으면 계속 진행
            if car.locate + speed >= 400:  # 이동 후 도착 지점을 넘어가게 된다면 400에 멈춤 
                speed = 400 - car.locate  
                n += 1  # 순위 증가
                car.goal = 1  # 도착 여부를 1로 설정
                car.hide()  # 자동차를 숨김
            car.drive(speed)  # 자동차를 이동시킴
            if car.goal == 1:  # 도착한 자동차라면
                car.write(str(n) + "등")  # 해당 순위를 화면에 표시
        car.locate += speed  # 자동차의 위치 업데이트
