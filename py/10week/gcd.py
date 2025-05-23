def gcd(a, b):
    # b가 0이면 a가 최대공약수
    if b == 0:
        return a
     # a와 b의 나머지를 이용해 재귀 호출
    return gcd(b, a % b)
     #나머지가 0이 될 때까지 반복하면 그때의 a가 최대공약수

# 사용자에게 숫자 입력받기
a = int(input("첫 번째 숫자를 입력하세요: "))
b = int(input("두 번째 숫자를 입력하세요: "))

# 결과 출력
print("최대공약수는:", gcd(a, b))
