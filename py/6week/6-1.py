#후위 표기법을 사용한 우선순위 연산
a_stack=[]  #스택을 리스트로 생성

def push(push_data): # 입력 함수 = push
    a_stack.append(int(push_data)) #append를 사용하여 피연산자(숫자) 삽입
    print(f'삽입과정:{a_stack}') 

def pop() : # 출력 함수 = pop
    a=a_stack[-1] # a= top
    print(f'계산을 위해 스택에서 빼야하는 값:{a}') # top값인 a 출력
    a_stack.remove(a_stack[-1]) # top을 지운다
    return a

a=list(input("계산식을 후위 표기법으로 입력하세요.\n연산자와"
             "피연산자는 \",\"로 분리해서 입력하세요.\n").split(','))

for i in a:
    if i == '+' or i=='-' or i == '*' or i=='/' : # 연산자를 만나면
        pop_data1=pop() # 스택에 있는 피연산자를 top부터 
        pop_data2=pop()# 두개 꺼냄
        if i=='+':
            push(pop_data2+pop_data1) # 계산된 값을 스택에 다시 넣기
        elif i =='-':
            push(pop_data2-pop_data1)
        elif i=='*':
            push(pop_data2*pop_data1)
        elif i == '/':
            push(pop_data2/pop_data1)
    else:
        push(i) # 피연산자 이면 스택에 push
