# 1주차 - 자료구조와 알고리즘
## 자료구조(Data Structure) 정의⭐⭐⭐
프로그램 설계, 구현과정에서 데이터를 구조적으로 저장하는 방식

특정 데이터의 효율적인 접근을 위한 자료의 조직 관리 저장 삽입 등등
## 자료구조(Data Structure) 필요성⭐⭐⭐
한정된 메모리를 효율적으로 사용하기 위하여 데이터 특성에 맞는 자료구조의 선택이 중요

특정 자료구조의 선택이 프로그램 성능에 영향을 미침


  
# 2주차 - 자료구조와 알고리즘

# 3주차 - 자료구조와 알고리즘

# 4주차 - 자료구조와 알고리즘
순차자료구조: 같은 자료구조에 속한 원소들을 일렬로 연속해서 저장함
장점: 특정 원소 탐색이 빠르다
단점: 메모리 낭비가 발생할 수 있다. 
         중간에 있는 원소 삽입, 삭제가 어렵다
```
ex) 
int a[3,4,5]
  
a[2] = 10   --> 3번쩨 원소를 10으로 바꿈

int = 4바이트

a가 100번지에 위치

= 100 + 4 *2 => 108번지 
```    
연결자료구조 : 같은 자료구조에 속한 원소들은 1:1관계이고 노드들은 메모리 빈 공간 어디에나 저장되고 주소값으로 연결되는 구조
장점 : 메모리 낭비가 없다
       중간에 있는 원소 삽입, 삭제가 용이하다(주소값만 있으면 가능)
단점: 특정 원소 탐색이 어렵다
      배열보다 구현이 어렵다
Linked list
