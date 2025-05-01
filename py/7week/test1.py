'''
순차자료구조 배열을 이용한 전화번호부관리 프로그램
기능: 입력, 수정, 삭제, 출력, 종료
설명을 키로 찾아 수정, 삭제 작업함
입력시 성명의 중복체크 해줘야함


--> 수정
순차자료구조(배열)을 이용한 전화번호부관리 프로그램 소스를
객체지향 프로그램 구조로 변경하기
'''


class Phonebook:
    # 클래스 생성
    def __init__(self):
        self.PhoneBook = []  # 전화번호부를 저장할 리스트 초기

    
    def add_new_user(self, name, phone): # 사용자 추가 함수
        # 사용자 이름이 있는지 확인
        if self.find_user(name) != None:
            print("이미 저장된 이름입니다")  #오류!
            return
        
        self.PhoneBook.append([name, phone])# 이름이 없으면 사용자 추가
    
    
    def find_user(self, name):# 사용자 이름으로 사용자 찾기
        count = 0  # 리스트 내 인덱스 번호를 추적
        position = None  # 위치 초기값
        
        for i in self.PhoneBook:# 전화번호에서 해당 이름이 있는지 확인
            if(i[0] == name):  # 이름이 있으면
                position = count  # 해당 위치를 count에 저장
                break  # 이름을 찾았으면 반복문 종료
            else:
                count += 1  # 일치하지 않으면 count를 증가시켜 다음 인덱스로
        return position  # 없으면 non으로

    
    def edit_user(self, name):# 이름으로 사용자를 찾고 전화번호 수정
        position = self.find_user(name)  # 이름으로 찾기
        if(position == None):  # 위치가 None이면 정보가 없음
            print("해당 정보가 존재하지 않습니다.")  
            return
        
        edit_value = input("수정할 전화번호 입력  : ")# 해당 사용자 정보를 찾으면 전화번호 입력
        self.PhoneBook[position][1] = edit_value  #전화번호 수정

    
    def delete_user(self, name):#사용자 삭제
        position = self.find_user(name)  # 이름으로 위치 찾기
        if(position == None):  # 위치가 None이면 해당 정보가 없다는 의미
            print("해당 정보가 존재하지 않습니다.") 
            return
        
        del(self.PhoneBook[position])# 해당 사용자 리스트에서 삭제

    
    def all_phone(self):# 전체 출력
        print("" * 10, "전화번호부", "" * 10)  # 나눔선
        for i in self.PhoneBook:  # 전화번호부에 있는 모든 사용자 출력
            print("이름: %5s   전화번호:%5s" % (i[0], i[1]))  # 사용자 이름과 전화번호 출력
        print("*" * 32)  # 나눔선

# 메인
if __name__ == '__main__':

    phonebook = Phonebook()  # 전화번호부 객체 생성

    # 반복문
    while True:
        
        choice = input("사용자 추가(n), 수정(e), 삭제(d), 전체 출력(p), 종료(q) : ")

        if (choice == 'n'):  
            name = input("이름: ")  
            phone = input("전화번호 : ") 
            phonebook.add_new_user(name, phone)  

        elif (choice == 'e'):  
            name = input("수정할 사용자의 이름을 입력하세요 : ") 
            phonebook.edit_user(name)  

        elif (choice == 'd'): 
            name = input("삭제할 사용자의 이름을 입력하세요 : ")  
            phonebook.delete_user(name)  

        elif (choice == 'p'): 
            phonebook.all_phone()  

        elif (choice == 'q'): 
            print("\n프로그램을 종료합니다.") 
            break  

        else: 
            print("다시 입력하세요")
