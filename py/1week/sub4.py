import random
from turtle import *

class Car:
    def __init__(self, speed, color, fname):
        self.speed = speed
        self.color = color
        self.turtle = Turtle()
        self.turtle.shape(fname)

    def drive(self, distance):
        self.turtle.forward(distance)  # 자동차 속도

    def turnleft(self, degree):
        self.turtle.left(degree)

# 자동차 이미지 등록
register_shape("car.gif")
register_shape("car1.gif")
register_shape("car2.gif")

# 자동차 객체 리스트 생성
cars = [
    Car(0, "green", "car.gif"),
    Car(0, "blue", "car1.gif"),
    Car(0, "red", "car2.gif")
]

# 초기 위치 리스트 생성
position = [-100, 0, 100]

# 자동차 객체 위치 설정
for i in range(3):
    cars[i].turtle.up()
    cars[i].turtle.goto(position[i], -200)  # 각 자동차 배치
    cars[i].turtle.left(90)  # 방향 조정
    cars[i].turtle.down()  

# 자동차 경주 
for _ in range(10):
    for car in cars:
        car.drive(random.randint(30, 100))  
