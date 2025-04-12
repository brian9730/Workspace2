''' 단순연결리스트를 이용한 객체지향 전화번호부 자료관리.
- 단순연결리스트 클래스에 노드 클래스를 삽입
- 이름 중복 체크
- 이름순으로 연결리스트에 저장
- 24.04.15
'''

class PhoneBook: #클래스 생성
        class Node:
                def __init__(self, data):
                        self.data = data #노드생성
                        self.next = None 
		
        def __init__(self): #단순연결리스트 생성자로 구성
                self.head = None 


        def insertNode(self, add_data):                    
                if self.head == None:  # 빈 연결리스트
                        self.head= self.Node(add_data)#첫 번째 노드 생성
                        print("신규입력 완료\n") #성공 메시지 출력
                        return
    
                current = self.head #현재에 헤드의 주소값 저장
                prev= None #이전 노드를 None로 초기화
                while current :    #노드가 있을때까지
                        if current.data[0] == add_data[0]: # 이미 있는 이름이라면
                                print("이미 있는 이름입니다\n")
                                return
                        elif current.data[0] > add_data[0] : #새로운 이름이 이미 있는 이름보다 작으면 (이름순 정렬)
                                break
                        prev = current #이전 노드를 현재 노드로 업데이트
                        current = current.next #현재 노드를 다음 노드로 이동
                        
                new_node = self.Node(add_data) # 새노드 생성
                
                if not prev : # 가장 작은 이름이면
                        new_node.next = self.head #헤드가 가르키는 주소값을 생성된 노드가 가르키는 주소값에 저장
                        self.head = new_node #생성된 노드의 주소값을 헤드에 저장

                else : #prev 와 current사이에 신규 노드 삽입하면 됨
                        prev.next = new_node #이전 노드에 생성된 노드의 주소값 저장
                        new_node.next = current #현재 노드의 주소값을 생성된 노드가 가르키는 주소값에 저장
                print("신규입력 완료\n")
                
      #연락처 수정          
        def changeNode(self, change_name):
                current = self.head  #현재 노드를 head로 시작
                while current : #currnet가 none이 아닐때까지 반복
                        if current.data[0] == change_name: #수정할 이름을 찾으면 
                                print("\n{}전화번호는 {}입니다.".format(current.data[0], current.data[1]))
                                current.data[1] = input("변경할 전화번호:")
                                print("\n{}의 전화번호가 {}으로 수정되었습니다.".format(current.data[0], current.data[1]))
                                return
                        current=current.next #다음노드의 주소값을 현재에 저장
                print("없는 이름입니다\n")
                
                      
      #연락처 전체 출력
        def printNodes(self): 
                current = self.head #현재 노드를 head로 설정
                if current == None:  # 빈 리스트이면
                        return 
                while current != None:
                        print(current.data, end = ' ')
                        current = current.next
               
                return
                
       #연락처 삭제
         
        def deleteNode(self, delete_name):
                if self.head == None: # 빈 연결리스트
                        print("연결리스트가 비어 있습니다\n")
                        return
                current = self.head #현재 노드를 head로 설정
                prev = None #이전 노드 초기화
  	  
                while current :
                        if current.data[0] == delete_name :
                                if not prev:  # 첫번째 자료임
                                        self.head = current.next #다음 노드의 주소값을 헤드에 저장
                                else :
                                        prev.next = current.next #다음 노드의 주소값을 이전 노드의 next에 저장
                                del current  # 해당 노드를 메모리에서 free시킴
                                print("연락처가 삭제되었습니다\n")
                                return
                        prev = current  # 다음 노드로 이동/현재 노드주소를 prev값에 넣음
                        current = current.next #다음 노드 주소값을 current에 넣음
                
                print("없는 이름 입니다\n")


        #연락처 찾기        

        def findNode(self,find_name):
                if self.head == None:
                        print("빈 리스트입니다")
                        return None
                current = self.head #현재 노드를 헤드로 설정

                while current :
                        if currnet.data[0] > find_name: #현재 이름보다 찾을 이름이 작다면
                                break;
                        if current.data[0] == find_name: #찾는 이름을 current가 가지고 있다면
                                print('\n{}님의 전화번호는 {} 입니다.' .format(current.data[0], current.data[1]))
                                return current
                        current = current.next # current가 다음 노드의 주소를 가짐.
                print("없는 이름입니다\n")
                return None

	    
if __name__=="__main__":

    print('단순연결리스트를 이용한 전화번호부 관리 프로그램입니다.\n')
    
    P = PhoneBook()  # 단순연결리스트 생성

    while True:
        print('\n1: 입력\t 2:수정\t 3:삭제\t 4:탐색\t 0:종료\n')
        
        ch = input("기능 선택--> ")
            
        if ch == '0':
            P.printNodes()
            print('종료합니다\n')
            break

        elif ch == '1':
            add_data =[]
            add_data.append(input('입력할 이름: '))         
            add_data.append(input('입력할 전화번호: '))
            P.insertNode(add_data) 
            P.printNodes()
            
        elif ch == '2':
            change_name = (input('전화번호를 수정할 이름:'))
            P.changeNode(change_name)  
            P.printNodes()

        elif ch == '3':
            delete_name = input('삭제할 이름: ')
            P.deleteNode(delete_name)                            
            P.printNodes()
            
        elif ch == '4':
            search_name = input('탐색할 이름 : ')
            P.findNode(search_name)
        else:       
            print('\n잘못된 입력입니다.\n')

    
