# TIL
### Today **24.01.11** I learned 마크다운, CLI, GIT<br/>
---
## 1. 마크다운 문법
1. `#`
    - 앞에 `#`을 넣어 글자의 크기를 조절할 수 있다.
    - 최대 6개까지 가능하다.
2. 리스트
    - 순서가 있는 리스트는 숫자를 이용해 작성한다.
    - 순서가 필요 없는 경우는 `-` 를 이용해 작성한다.
3. Code block
    - ```python
        print('hello')
        ```
    - \```python print('hello')\```
4. 링크 & 이미지 삽입
    - `[주소](www.google.com)`
    - `[이미지](https://ssl.~~~.jpg)` - 인터넷
    - `[이미지](C:\Users\-\Desktop\-.png)` - 컴퓨터
5. 문단 구분하기
    - `---`
6. 글자 속성 변경
    - `**` 굵게
    - `*` 기울임
    - `~~` 취소선

[마크다운 공식 문서](https://www.markdownguide.org/basic-syntax/)

## 2. CLI
1. `cd .`
    - 내 위치
2. `cd ..`
    - 상위 위치로 이동
3. `cd ../..`
    - 상위의 상위로 위치 이동
4. `mkdir`
    - (make directory) 폴더 만들기
5. `ls`
    - 리스트 확인
6. `rm -r`
    - 파일 삭제

## 3. GIT
1. Working Directory (내 PC)
    - 실제 작업하는 파일들이 위치하는 영역
2. Staging Area (중간다리)
    - Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비영역
3. Repository (Git Hub)
    - 버전이력과 파일들이 영구적으로 저장되는 영역, 모든 버전과 변경이력이 기록됨

## 4. GIT 명령어
1. git init
    - 로컬 저장소 설정(초기화), git의 버전관리를 시작할 디렉터리에서 진행
2. git add .
    - 변경사항 있는 파일을 staging area에 추가
3. git commit -m "메세지"
    - 변경이력 남기기
4. git status
    - 깃 상태 확인
5. git log(git log --oneline)
    - 커밋 히스토리를 조회
6. git remote add (이름) (원격 저장소 URL)
    - 원격 저장소 추가
7. git remote -v
    - 연결이 되어있나 확인
8. git remote remove (이름)
    - 등록된 원격 저장소 삭제
9. git clone
    - 어떤 프로젝트의 원격 저장소를 복제할 때 사용 (처음 1번만)

## 5. 과정
    1. git push 과정
        1. git init
        2. git add .
        3. git commit -m ""
        4. git push
    
    2. git pull 과정
        1. git clone (처음 할때), git pull

### 로컬에서 확인할 수 있는 것들(인터넷선 뽑아도 되는 기능)
1. git status
2. git log, git log --oneline
3. git config

### 주의사항
1. .git 폴더 내부에 다시 .git이 만들어져서는 안된다 (충돌할 수 있음)
    - git init 내부 폴더에 다시 git init 하지 말 것

### 자리를 바꾸면 해야할 일들
1. 자격 증명 관리자에서 깃허브 제거
2. 새로운 이메일, 이름 등록

---

### Today **24.01.12** I learned 파이썬 기초 문법<br/>
---
## 1. 파이썬 기초 문법
1. 파이썬 이용 시 주의 해야할 것
    - 대, 소문자 구분
    - 띄어쓰기
    - 스펠링

2. 사칙연산
    - `+` 더하기
    - `-` 빼기
    - `/` 나누기(float)
    - `//` 몫 구하기
    - `%` 나머지 구하기

3. 데이터 타입
    - int 정수 1+1 == 2
    - str 문자 '1'+'1' == 11
    - list 리스트 
        - 인덱스를 다른 언어보다 자유롭게 컨트롤 할 수 있다는 장점이 있다.
    - dictionary 딕셔너리
    - tuple 튜플

4. 조건문
    - if
    - elif
    - else

5. 반복문
    - while
    - for

### Today **24.01.13** I learned 싱글톤 패턴<br/>
---
## 1. 싱글톤 패턴
1. 어플리케이션 내에서 로그를 기록하거나 캐싱을 할때 사용
2. 프로그램 전역적으로 사용하고 유일할때 사용
3. 사용자가 인스턴스를 요청할때마다 만약 인스턴스가 존재하지 않으면 만들어서 반환하고(요청한 값)<br/>있다면 있는 그 값을 그대로 반환
4. 외부에서 인스턴스가 생성할 수 없도록 생성자를 private으로 막아두면<br/>싱글톤 패턴 구현 가능

## 2. 권장되는 방법
1. Enum
    - Thread-safe하게 구현
    - 쉽게 만들 수 있음.
2. Bill Pugh Solution
    - 리소스 낭비될 일이 없음
    - Thread-safe하게 구현
    - 구현방식이 단순

### Today **24.01.14** I learned 싱글톤 패턴<br/>
---
## 3. 어디서 사용되는지
1. 어플리케이션 내에서 로그를 기록하거나 캐싱을 할 때 사용
2. 프로그램 전역적으로 사용하고 유일할 때 사용 (게임의 레벨, 점수, 아이템 등)
3. 인스턴스 생성 비용이 높은 경우

## 4. 왜 사용하는지
1. 고정된 메모리 영역을 가지고 하나의 인스턴스만 사용하기 때문에 메모리 낭비를 방지
2. 싱글턴 클래스의 인스턴스는 전역이기 때문에 다른 클래스의 인스턴스들이 데이터를 공유하기 쉬움
3. DBCP(데이터 베이스 커넥션 풀) 처럼 공통된 객체를 여러 개 생성해야 하는 상황에 많이 사용

## 5. 주의사항
1. 인스턴스가 유일해야 함
2. 멀티쓰레드 환경에서 조심해야함
3. 싱글톤 인스턴스가 계속해서 유지되면, 메모리를 계속해서 점유하기 때문에 메모리 관리가 필요함

### Today **24.01.15** I learned 파이썬 기초 문법<br/>
---
1. Style Guide
    1. 직관적인 변수명
    2. 적절한 들여쓰기 사용

2. 문자열의 특징
    1. 순서가 있음
    2. 변경이 불가능함
        - `my_str = 'hello'`<br/>`'my_str[1] = 'z` <br/> TypeError: 'str' object does not support item assignment
    
3. Escape 시퀀스
    1. 역슬래시 \ 뒤에 특수문자가 와서 특수한 기능을 하는 문자 조합
        1. `\n` 줄바꿈
        2. `\t` 탭
        3. `\\` 백슬래시
        4. `\'` 작은 따옴표
        5. `\"` 큰 따옴표

4. 문자열 내에 변수나 표현식 삽입이 가능한 f-string
    - `bugs = 'roaches`<br>`counts = 13`<br>`area = living room`
    - `print(f'Debugging {bugs}{counts}{area}.)` <br>#Debugging roacehs 13 living room
    - 간단한 표현식도 사용이 가능하다.<br>`{3+2}`

5. 인덱스
    - 'H  E  L  L  O '<br>
    - -5 -4 -3 -2 -1<br>
    -  0   1   2   3   4

6. 슬라이싱
    - `my_str = 'Hello'`
    - `my_str[:3]` #'Hel'
    - `my_str[3:]` #'lo'
    - `my_str[0:5:2]` #'hlo'
    - `my_str[::-1]` #'olleh'문자열 뒤집기

### Today **24.01.16** I learned 파이썬 기초 문법<br/>
---
1. 리스트
    - 변경 가능한 시퀀스 자료
    - 어떤 자료도 저장 가능 문자, 숫자, 리스트 모두 저장 가능
    - 순서가 없음

2. 튜플
    - 소괄호로 표기
    - 어떤 자료형도 저장 가능
    - 변경 불가능함<br>
    - 길이가 1인 튜플을 만들 땐 `my_tuple_2 = (1,)` 와 같이 만들어야 함.<br>
    `my_tuple_3 = (1)` = 1 <br>
    컴마가 없으면 정수가 된다. <br>
    - 인덱스는 리스트와 같음
    - 슬라이싱 역시 튜플로 나옴
    - 안전하게 여러개의 값을 전달, 그룹화, 다중할당 등
    - 개발자가 직접 사용하기보다 파이썬 내부 동작 에서 주로 사용됨.

3. range
    - 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형
    - 내장함수

4. 딕셔너리
    - key, value 쌍으로 이뤄진 순서와 중복이 없는 변경 가능한 자료형
    - 딕셔너리의 key는 변경 불가능한 자료형(str, int, float, tuple, range)만 가능
    - value는 모든 자료형 사용 가능
    - 중괄호로 표기
    - 딕셔너리는 순서가 없기 때문에 인덱스로 접근이 불가능
    - value값은 변경이 가능하나, key값은 변경 불가능
    - key가 같을 경우 가장 하단에 있는 값으로 출력됨.
    ```
    my_dict = {
	'apple' : 100,
    'list' : [1, 2, 3],
    'apple' : 12}
    ```
    `{'apple': 12, 'list':[1,2,3]}`

5. set
    - 순서와 중복이 없는 변경 가능한 자료형
    - 수학에서의 집합과 동일한 연산 처리 가능
    - 중괄호로 표기
    - 빈 set 값을 넣을땐 내장함수를 이용해야함. set()
        - 이는 빈 딕셔너리 dic={} 와 겹치기 때문임.
    - 인덱스 접근 불가능
```
my_set_1 = {1,2,3}
my_set_2 = {3,6,9}
합
print(my_set_1 | my_set_2) #{1,2,3,6,9}
차
print(my_set_1 - my_set_2) #{1,2}
곱
print(my_set_1 & my_set_2) #{3}
```

6. None
    - 파이썬에서 '값이 없음'을 표현
    - variable = None
    `print(variable) #None`


7. Boolean
    -참, 거짓(True, False)를 표현하는 자료형


---
Type Conversion (형 변환)
1. 암시적 형변환(컴퓨터가 알아서 해주는 형변환)
	- 3+5.0 = 8.0 int + float = float
	- True + 3 = 4 Boolean + int = int
2. 명시적 형변환(개발자가 직접 형변환을 하는 것)
	- int('1') = 1
    - str(1)+'등' = 1등
    - float('3.5') = 3.5
    - int(3.5) = 3
    
---
비교 연산자
is 
is not
값 비교가 아니라 메모리 내에서 같은 객체를 참조하는지 확인
==는 동등성, is는 식별성	
```
print(2.0 == 2) #True
print(2.0 is 2) # False
```
None, True, False 등을 비교할 때 사용

`print(1 == True) #True`
`print(1 is True) #False`

논리 연산자
`print(not True) # False`
`print(not 0) #True`

---
## 단축평가

- 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작
- 코드 실행을 최적화 하고 불필요한 연산을 피할 수 있도록 함
```
vowels = 'aeiou'
if ('a' and 'b') in vowels #False
if ('b' and 'a') in vowels #True
모든 문자열은 true, 따라서 and는 뒤의 값도 true여야 하므로 단축평가가 일어나지 않는데 따라서  'a'가 출력된다.

if ('a' or 'b') # a
if ('b' or 'a') # b
if ('a' and 'b') # b
if ('b' and 'a') # a
```


### 시퀀스형 연산자

- +와 *는 시퀀스 간 연산에서 산술 연산자일때와 다른 역할을 가짐

`+` 결합 연산자
`*` 반복 연산자

소괄호의 우선순위가 가장 높으므로 코드를 짤때 grouping 해주는게 중요하다.

### Today **24.01.17** I learned 파이썬 기초 문법<br/>
---

## 함수
1. 함수의 특징
    - 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음
    - 코드의 중복 방지
    - 재사용성이 높아지고, 코드의 가독성과 유지 보수성 향상

2. 내장 함수
    - 파이썬이 기본적으로 제공하는 함수(별도의 import 없이 사용 가능)

3. 함수 호출
    - 함수를 실행하기 위해 함수의 이름을 사용하여 함수의 코드 블록을 실행하는 것
    - 함수를 호출하기 위해선 함수의 이름과 필요한 인자(argument)를 전달해야 함
    - 호출 부분에서 전달된 인자는 함수 정의 시 작성한 매개변수에 대입

4. 함수 정의
    - 정의는 def 키워드로 시작
    - def 키워드 이후 함수 이름 작성
    - 괄호안에 매개변수를 정의할 수 있음
    - 매개변수는 함수에 전달되는 값을 나타냄

5. 함수 반환 값
    - 함수는 필요한 경우 결과를 반환할 수 있음
    - return 키워드 이후에 반환할 값을 명시
    - return문은 함수의 실행을 종료하고(함수의 종료조건), <br>
    결과를 호출 부분으로 반환(return 이후는 죽은 코드)
    - return이 없는 함수도 존재

6. 매개변수와 인자의 차이
    - 매개변수 : 함수를 정의할 때, 함수가 받을 값을 나타내는 변수
    - 인자 : 함수를 호출할 때, 실제로 전달되는 값
    ```
    def sum(num1, num2): #num1, num2 는 매개변수
        return num1+num2
    
    sum(1, 2) #1, 2는 인자
    ```

## 인자

1. 위치 인자
    - 함수 호출 시 인자의 위치에 따라 전달되는 인자
    - 위치 인자는 함수 호출 시 반드시 값을 전달해야 함
    ```
    def greet(name, age):
        print(f'안녕하세요, {name}님! {age}살이시군요.')
    
    greet('Alice', 25) #안녕하세요, Alice님! 25살이시군요.
    ```

2. 기본 인자 값
    - 함수 정의에서 매개변수에 기본 값을 할당하는 것
    - 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
    ```
    def greet(name, age = 30):
        print(f'안녕하세요, {name}님! {age}살이시군요.')
    
    greet('Alice', 25) #안녕하세요, Alice님! 25살이시군요.
    greet('Bob') #안녕하세요, Bob님! 30살이시군요.
    ```

3. 키워드 인자
    - 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
    - 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
    - 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
        - 단 호출 시 키워드 인자는 위치인자 뒤에 위치해야 함
    `greet(age=30, 'Bob') #positional  argument follows keyword argument`

4. 임의의 인자 목록
    - 정해지지 않은 개수의 인자를 처리하는 인자
    - 함수 정의 시 매개변수 앞에 '*'를 붙여 사용하며, 여러 개의 인자를 tuple로 처리

    ```
    def cal_sum(*args):
        print(args)
        total = sum(args)
        print(f'합계: {total}')
    cal_sum(1, 2, 3)
    #(1, 2, 3)
    #합계 : 6
    ```

5. 임의의 키워드 인자 목록
    - 정해지지 않은 개수의 키워드 인자를 처리하는 인자
    - 함수 정의 시 매개변수 앖에 '**'를 붙여 사용하며, 여러개의 인자를 dictionary로 묶어 처리
    ```
    def print_info(**kargs):
        print(kargs)
    print_info(name = 'Eve', age = 30) # {'name': 'Eve','age': 30 }
    ```

---

## 파이썬의 범위(Scope)

1. 종류
    - 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분한다.
    1. scope
        - global scope : 코드가 어디든 참조할 수 있는 공간
        - local scope : 함수가 만든 scope(함수 내부에서만 참조 가능)
    2. variable
        - global variable : global scope에 정의된 변수
        - local variable : local scope에 정의된 변수

2. 변수의 수명 주기
    - 변수의 수명주기는 변수가 선언되는 위치와 스코프에 따라 결정됨
    1. built in scope
        - 파이썬이 실행된 이후 영원히 유지
    2. global scope
        - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    3. local scope
        - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
    
3. 이름 검색 규칙
    - Local scope > Enclosed scope > Global scope > Built in scope<br> 변수가 로컬에 없으면 Enclosed로, Global, Built-in 순서로 찾아나감.<br>함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음
    ```
    print(sum)
    print(sum(range(3))) # 3

    sum = 5

    print(sum) # 5
    print(sum(range(3))) #TypeError:'int'object is not callable
    5(range(3))
    ```

4. Global 키워드
    - 변수의 스코프를 전역 범위로 지정하기 위해 사용
    - 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용
    - 권장되지는 않음
    - 함수로 값을 바꾸고자 한다면 항상 인자로 넘기고, 함수의 반환값을 사용하는 것을 권장

5. 재귀 함수
    - 함수 내부에서 자기 자신을 호출하는 함수
    - 특정 알고리즘 식을 표현할 때 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
    - 1개 이상의 base case(종료상황)가 존재하고, 수렴하도록 작성
    - 예시
    ```
    def factorial(n):
	    if n === 0:
            return 1
        return n*factorial(n-1)
        
    result = factorial(5)
    print(result) # 120
    ```
    - n -= 1 없어도 동작하는 이유는 n = 0이 될때까지 반복되며, 종료조건을 설정하여 <br> 
    재귀호출이 멈추도록 하기 때문이다. 문제를 작은문제로 분할하는데 사용된다.
    - 종료조건을 명확히 해야한다.(무한 호출에 빠짐)
    - 반복되는 호출이 종료조건을 향하도록

## 유용한 내장 함수
    
1. map
    - map(function, iterable)
    - 순회 가능한 데이터 구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환
    - function > 함수, iterable > 반복 가능한 것(시퀀스, 리스트, 튜플 등등)
    ```
    a = ['1','2','3','4','5']
    result = list(map(int, a))
    print(result) # [1,2,3,4,5]
    ```

2. zip
    - zip(*iterables)
    - 임의의 iterable을 모아 튜플을 원소로 하는 zip object 반환
    ```
    girls = ['jane', 'ashley']
    boys = ['peter', 'jay']
    pair = zip(girls, boys)

    print(list(pair)) #[('jane','peter'),('ashley','jay)]
    ```
3. lambda
    - lambda 매개변수: 표현식
        - 매개변수
            - 함수에 전달되는 매개변수들
            - 여러개의 매개변수가 있을 경우 쉼표로 구분
        - 표현식
            - 함수의 실행되는 코드블록으로, 결과값을 반환하는 표현식으로 작성
    - 간단한 연산이나 함수를 한줄로 표현할 때 사용
    - 함수를 매개변수로 전달하는 경우에도 유용하게 활용
    - 제한사항
        - 로직이 복잡한 함수는 람다함수로 변경 불가능
        - 1줄로 작성해야 함

## Packing과 Unpacking
1. 패킹
    1. '*'을 활용한 패킹
        - 인자 개수에 관계없이 튜플 하나로 패킹 돼 내부에서 처리
        ```
        def my_func(*objects):
            print(objects) #(1,2,3,4,5)
            print(type(objects)) #<class 'tuple'>

        my_func(1,2,3,4,5)
        ```
2. 언패킹
    - 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
    ```
    packed_values = 1,2,3,4,5
    a,b,c,d,e = packed_values
    print(a,b,c,d,e) # 1 2 3 4 5
    ```
    1. '*'을 활용한 언패킹
    ```
    names = ['alice', 'jane', 'peter']
    print(*names) # alice jane peter
    ```
    2. '**'을 활용한 언패킹
    ```
    def my_function(x,y,z):
        print(x,y,z)

    my_dict = {'x':1,'y':2,'z':3}
    my_function(**my_dict) # 1 2 3
    ```
### '*'
- 패킹 연산자로 사용될 때
    - 여러개의 인자를 하나의 튜플로 묶는 역할
- 언패킹 연산자로 사용될 때
    - 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인자로 전달
### '**'
- 언패킹 연산자로 사용될 때 딕셔너리의 키-값 쌍을 키워드 인자로 언패킹 하여 함수의 인자로 전달하는 역할

### Today **24.01.18** I learned 파이썬 기초 문법<br/>
---

## 모듈
1. 모듈
    - 한 파일로 묶인 변수와 함수의 모음
    - 특정한 기능을 하는 코드가 작성된 파이썬 파일

2. 모듈 가져오기
    - 모듈 내 변수와 함수에 접근하려면 import 문이 필요
    `import math`

3. 모듈 사용하기
    - '.(dot)'은 점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라 라는 의미의 연산자
    `print(math.pi)`

4. 모듈을 import 하는 다른 방법
    - from 절을 활용해 특정 모듈을 미리 참조하고 어떤 요소를 import 할지 명시
    ```
    from math import pi, sqrt

    print(pi)
    print(sqrt(4))
    ```
    - math에서 pi와 sqrt만 사용 한다는 코드, math 입력 없이 바로 사용 가능
    - 명시적이진 않아서 권장하지 않음
    - 이름이 같은 함수와 변수가 존재할 경우 마지막에 입력된 코드로 덮혀짐

5. 모듈 주의사항
    - 만약 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생
    - 마지막에 import된 이름으로 대체 됨
    ```
    from math import pi, sqrt # sqrt
    from my_math importr sqrt # sqrt
    # my_math의 sqrt로 이용됨
    ```
    - 모듈 내 모든 요소를 한번에 import 하는 * 요소가 있는데 권장되진 않음(명시적이지 않기 때문에)

6. 사용자 정의 모듈
    - 다른 파일에서 직접 정의한 함수도 모듈로 이용이 가능하다.
    - 크기 : 모듈 < 패키지 < 라이브러리

7. 패키지
    - 관련된 모듈들을 하나의 디렉토리에 모아놓은 것
    - PSL 내부 패키지 < 외부 패키지(pip를 사용하여 설치 후 import)
    
8. pip
    - 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템
    - PYPI에 저장된 외부 패키지들을 설치
    - 설치 방법
        - pip install '모듈명'
        - 최소, 특정, 최신 버전을 선택해서 받아올 수 있음.

9. 패키지 사용 목적
    - 모듈들의 이름공간을 구분하여 충돌을 방지
    - 모듈들을 효율적으로 관리하고 재사용 할 수 있도록 돕는 역할

---
## 제어문

1. 제어문
    - 코드의 실행 흐름을 제어하는데 사용되는 구문
    - 조건에 다라 코드 블록을 실행하거나 반복적으로 코드를 실행

2. 조건문
    - 주어진 조건식을 평가하여 해당 조건이 참인 경우에만 코드블록을 실행
    - 동시에 검사하는것이 아니라 순차적으로 비교

3. 반복문
    1. for
        - 임의의 시퀀스 항목들을 시퀀스에 들어있는 순서대로 반복(str, tuple, list, range...)
        - for 변수 in 반복가능한 객체(시퀀스 + 딕셔너리, set):
            코드블록
        - 문자열은 시퀀스다.(문자열 순회도 가능함)
        - 딕셔너리 역시 순회가 가능하다.
        ```
        my_dict = {
            'x' = 10,
            'y' = 20,
            'z' = 30,
        }
        for key in my_dict:
            print(key) # x y z
            print(my_dict[key]) 10 20 30
        ```
        - 딕셔너리 기본 반복은 키 값만 출력
        - 인덱스로 리스트 순회

    2. while
        - 주어진 조건식이 참일 동안 코드를 반복해서 실행(종료조건 반드시 필요)
        - 반복 제어
            - break : 반복을 즉시 중지
            - continue : 다음 반복으로 건너 뜀(하단의 코드를 읽지않고 다음 반복으로 넘어감)
            - 주의사항 : break, continue를 남용하는 것은 코드의 가독성을 저하할 수 있음
            - 특정한 종료조건을 만들어 break를 대신하거나, if문을 사용해 continue처럼<br> 코드를 건너뛸 수도 있음

## List Comprehension

1. 리스트 컨프리헨션
    - 간결하고 효율적인 리스트 생성방법
    - [expression for 변수 in iterable]
    - list(expression for 변수 in iterable)

    ```
    for num in numbers:
        squared_numbers.append(num**2)
        
    squared_numbers = [num**2 for num in numbers]
    ```
    - [expression for 변수 in iterable if 조건식]
    - list(expression for 변수 in iterable if 조건식)
    - 변환 연습을 하되, 남용은 하지 말 것.

## 참고사항
1. pass
    - 아무런 동작도 수행하지 않고 넘어가는 역할
    - 문법적으로 문장이 필요하지만 실행에는 영향을 주지 않아야 할 때 사용

2. enumerate
    - emumerate(iterable, start = 0)
    - iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수
    ```
    fruits = ['apple', 'banana', 'cherry']
    for index, fruit in enumerate(fruits):
        print(f'인덱스 {index}: {fruit}')
    # 인덱스 0: apple
    # 인덱스 1: banana
    # 인덱스 2: cherry
    ```

