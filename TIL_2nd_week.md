# TIL
### Today **24.01.22** I learned 데이터 구조<br/>
---
## 1. 데이터 구조
1. 자료구조
    - 컴퓨터 공학에서는 자료구조 라고 함
    - 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠놓은 것
2. 데이터 구조 활용
    - 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 메서드를 호출하여 다양한 기능 활용하기

---
## 2. 메서드
1. 메서드
    - 객체에 속한 함수(객체의 상태를 조작하거나 동작을 수행)
    - 메서드는 클래스 내부에 정의되는 함수
    - 클래스는 파이썬에서 타입을 표현하는 방법이며 이미 은연중에 사용해왔음
    - help 함수를 이용해 str 함수를 호출해보면 class임을 확인할 수 있음
    - 사용법은 `객체.메서드()`
        - 메서드는 어딘가(클래스)에 속해있는 함수이며, 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재한다.

2. 문자열 조회/탐색 및 검증 메서드
    1. s.find(x) : x의 첫번째 위치를 반환, 없으면 -1 반환
    2. s.index(x) : x의 첫번째 위치를 반환, 없으면 오류 발생
    3. s.isalpha() : 모든 문자열이 알파벳인지 확인, 하나라도 알파벳 아니면 False 반환
    4. s.isupper() : 모든 문자열이 대문자인지 확인(T,F 값 반환)
    5. s.islower() : 모든 문자열이 소문자인지 확인(T,F 값 반환)

3. 문자열 조작 메서드 (str은 불변이기 때문에 새로운 문자열로 반환)
    1. s.replace(old, new[, count]) : 바꿀 대상 굴자를 새로운 글자로 바꿔서 반환
    2. s.strip([chars]) : 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거
    3. s.split(sep=None, maxsplit = -1) : 지정한 문자를 구분자로 문자열을 분리하여 문자열의 리스트로 반환
    4. 'separator'.join([iterable]) : iterable 요소들을 원래의 문자열을 구분자로 이용하여 하나의 문자열로 연결
    5. s.capitalize() : 첫글자를 대문자로 변경
    6. s.title() : 띄어쓰기 기준으로 각 단어 첫 글자는 대문자로, 나머지는 소문자로 변환
    7. s.upper() : 모두 대문자로 변경
    8. s.lower() : 모두 소문자로 변경
    9. s.swapcase() : 대 <> 소문자 서로 변경

    `메서드는 이어서 사용 가능`

4. 리스트 값 추가 및 삭제 메서드
    1. L.append(x) : 리스트 마지막에 항목 x를 추가
    2. L.extend(iterable) : iterable m의 모든 항목들을 리스트 끝에 추가 (+= 와 같은 기능)
    3. L.insert(i, x) : 리스트 인덱스 i에 항목 x를 삽입
    4. L.remove(x) : 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거
    5. L.pop() : 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거
    6. L.pop(i) : 리스트의 인덱스 i에 있는 항목을 반환 후 제거
    7. L.clear() : 리스트의 모든 항목 삭제(데이터만 삭제)

5. 리스트 탐색 및 정렬 메서드
    1. L.index(x, start, end) : 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환
    2. L.reverse() : 리스트의 순서를 역순으로 변경(정렬X)
    3. L.sort() : 리스트를 정렬(매개변수 이용 가능)
    4. L.count() : 리스트의 항목 x의 개수를 반환

---
## 3. 복사
1. 할당
    - 할당 연산자(=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사
    ```
    origin_lst = [1,2,3]
    copy_lst = origin_lst
    print(origin_lst, copy_lst) # [1,2,3] [1,2,3]

    copy_lst[0] = 'hi'
    print(origin_lst, copy_lst) # ['hi',2,3] ['hi',2,3]
    ```

2. 얕은 복사
    - 슬라이싱을 통해 생성된 객체는 원본 객체와 독립적으로 존재
    ```
    a = [1,2,3]
    b = a[:]
    print(a, b) #[1,2,3] [1,2,3]

    b[0] = 100
    print(a, b) #[1,2,3] [100,2,3]
    ```
    - 얕은 복사의 한계
        - 2차원 리스트와 같이 변경 가능한 객체 안에 변경 가능한 객체가 있는 경우
        ```
        a = [1,2,[1,2,]]
        b = a[:]
        print(a, b) #[1,2,[1,2]] [1,2,[1,2]]
        
        b[2][0] = 100
        print(a, b) #[1,2,[1,2]] [1,2,[1,2]]
        ```
        - a와 b의 주소는 다르지만 내부 객체의 주소는 같기 때문에 함께 변경됨

3. 깊은 복사
    - 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함
    - 리스트 깊은 복사 예시
    ```
    import copy

    origin_lst = [1,2,[1,2]]
    deep_copied_lst = copy.deepcopy(origin_lst)

    deep_copied_lst[2][0] = 100

    print(origin_lst) # [1,2,[1,2]]
    print(deep_copied_lst) # [1,2,[100,2]]
    ```

---
## 참고
1. isdecimal()
    - 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True
2. isdigit()
    - isdecimal()과 비슷하지만, 유니코드 숫자도 인식
3. isnumeric()
    - isdigit()과 유사하지만, 몇 가지 추가적인 유니코드 문자들을 인식(분수, 지수, 루트 기호도 숫자로 인식)


### Today **24.01.23** I learned 비시퀀스 메서드<br/>
---
## 1. 비시퀀스 메서드

### 1. set
1. 고유한 항목들의 정렬되지 않은 컬렉션
        - 중복되지 않은 비시퀀스를 의미함
    1. s.add(x)
        - 세트 s에 항목x를 추가하고, 이미 x가 있다면 변화는 없다.
    2. s.clear()
        - 세트 s의 모든 항목을 제거
    3. s.remove(x)
        - 세트 s에서 항목 x를 제거하고, 항목이 없을 경우 Key error
    4. s.pop()
        - 세트 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거
    5. s.discard(x)
        - 세트 s에서 항목 x를 제거
    6. s.update(iterable)
        - 세트 s에 다른 iterable 요소를 추가

2. 세트의 집합 메서드
    ```
    set_1 = {0,1,2,3,4}
    set_2 = {0,1,2,3,4}

    ```
    1. set1.difference(set2) #차집합 set1 - set2
        - set1에는 들어있지만 set2에는 없는 항목으로 세트를 생성 후 반환
    2. set2.intersection(set2) # 교집합 set1 & set2
        - set1, set2 모두 들어있는 항목으로 세트를 생성 후 반환
    3. set1.issubset(set2)
        - set1 항목이 모두 set2에 들어있으면 True를 반환 set1 <= set2
    4. set1.issuperset(set2)
        - set2 항목이 모두 set1에 들어있으면 True를 반환 set >= set2   
    5. set1.union(set2) # 합집합 set1 | set2
        - set1 또는 set2에 들어있는 항목으로 세트를 생성 후 반환

---
### 2. 딕셔너리
1. 고유한 항목들의 정렬되지 않은 컬렉션 (key:value)
    1. .clear()
        - 딕셔너리 D의 모든 키/값 쌍을 제거
    2. .get(key[,default])
        - 키 연결된 값을 반환하거나 키가 없으면 None 혹은 기본 값을 반환
    ```
    person = {
	'name' : 'Alice'
    'age' : 25
    }
    print(person.get('name')) # Alice
    print(person.get('country')) # None
    print(person.get('country', 'Unknown')) # Unknown 
    ```
    3. .keys()
        - 딕셔너리 키를 모은 객체를 반환(iterable)
    ```
    person.keys() # dict_keys(['name','age'])
    for key in person.keys():
	print(key)
    
    # name
    # age
    ```
    4. .values()
        - 딕셔너리 값을 모은 객체를 반환
    ```
    for value in person.values():
	print(value)
    
    # Alice
    # 25
    ```
    5. items()
        - 딕셔너리 키/값 쌍을 모은 객체를 반환
    ```
    for key, value in person.items():
	print(k, v)

    # name Alice
    # age 25
    ```
    6. .pop(key[,default])
        - 키를 제거하고 연결됐던 값을 반환(없으면 에러나 default를 반환)
    ```
    print(person.pop('age')) # 25
    print(person) # {'name':'Alice'}
    print(person.pop('country', None)) #None
    print(person.pop('country')) # Keyerror
    ```
    7. .setdefault(key[,default])
        - 키와 연결된 값을 반환, 키가 없다면 default와 연결한 키를 딕셔너리에 추가하고 default를 반환
    ```
    print(person.setdefault('country', 'KOREA')) # KOREA
    print(person) # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}
    ```
    8. .update([other])
        - other가 제공하는 키/값 쌍으로 딕셔너리를 갱신, 기존 키는 덮어씀
    ```
    person = {
	'name' : 'Alice'
    'age' : 25
    }
        
    other_person = {
        'name' : 'Jane',
        'gender' : 'Female'
    }
    person.update(other_person)
    print(person)
    # {'name': 'Jane', 'age': 25, 'gender': 'Female'}

    person.update(age=50, country = 'KOREA')
    print(person)
    # {'name': 'Jane', 'age': 25, 'gender': 'Female', 'country': 'KOREA'}
    ```

---

### 참고
## 해시
1. 해시 테이블
    - 해시 함수를 사용하여 변환한 값을 색인(index)으로 삼아 키(key)와 데이터(value)를 저장하는 자료구조
    - 데이터를 효율적으로 저장하고 검색하기 위해 사용
    - 해시 테이블 원리
        - 키를 해시 함수를 통해 해시 값으로 변환하고, 이 해시 값을 인덱스로 사용하여 데이터를 저장하거나 검색
        - 데이터 검색이 매우 빠르게 이루어짐

2. 해시
    - 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것
    - 이렇게 생성된 고유한 값은 주로 해당 데이터를 **식별** 하는데 사용될 수 있음
    - 일종의 주민번호와 같은 역할
    - 데이터를 고유하게 식별
    - 파이썬에서는 해시 함수를 사용하여 데이터를 해시 값으로 변환하며, 이 해시값은 정수로 표현 됨

3. 해시 함수
    - 임의의 길이의 데이터를 입력받아 고정된 길의의 데이터(해시 값)를 출력하는 함수
    - 주로 해시 테이블 자료구조에 사용되며, 매우 빠른 데이터 검색을 위한 컴퓨터 소프트웨어에서 유용하게 사용

4. set의 요소 & 딕셔너리의 키와 해시테이블 관계
    - 파이썬에서 세트의 요소와 딕셔너리의 키는 해시 테이블을 이용하여 중복되는 않은 고유한 값을 저장함
    - 세트 내의 각 요소는 해시 함수를 통해 해시 값으로 변환되고, 이 해시값을 기반으로 해시 테이블에 저장됨
    - 따라서 딕셔너리의 키는 매우 빠른 탐색 속도를 제공하며, 중복된 값을 허용하지 않음

5. 파이썬에서 해시 함수
    - 파이썬에서 해시 함수의 동작 방식은 객체의 타입에 따라 달라짐
    - 정수와 문자열은 서로 다른 타입이며, 이들의 해시 값을 계산하는 방식도 다름

6. 파이썬에서의 해시 함수 - 정수
    - 같은 정수는 항상 같은 해시 값을 가짐
    - 해시 테이블에 정수를 저장할 때 효율적인 방법
    - 예를 들어, hash(1)과 hash(2)는 항상 서로 다른 해시 값을 갖지만, hash(1)은 항상 동일한 해시 값을 갖게 됨
    ```
    print(hash(1)) # 1
    print(hash(1)) # 1

    print(hash('a')) # 실행시마다 다름
    print(hash('a')) # 실행시마다 다름
    ```

7. 파이썬에서의 해시 함수 - 문자열
    - 문자열은 가변적인 길이를 갖고 있고, 문자열에 포함된 각 유니코드 코드 포인트 등을 기반으로 해시 값을 계산
    - 이로 인해 문자열의 해시 값은 실행 시마다 다르게 계산됨
    ```
    print(hash(1)) # 1
    print(hash(1)) # 1

    print(hash('a')) # 실행시마다 다름
    print(hash('a')) # 실행시마다 다름
    ```

8. set의 pop 메서드의 결과와 해시 테이블의 관계
    - pop 메서드는 set에서 임의의 요소를 제거하고 반환
    - 실행할 때마다 다른 요소를 얻는다는 의미에서의 무작위가 아니라 '임의'라는 의미에서 '무작위'
    - 해시 테이블에 나타나는 순서대로 반환하는 것

9. hashable
    - hash() 함수의 인자로 전달해서 결과를 반환 받을 수 있는 객체를 hashable 이라 함
    - 대부분의 불변형 데이터 타입은 hashable
    - 단, tuple의 경우 불변형이지만 해시 불가능한 객체를 참조 할 때는 tuple 자체도 해시 불가능해지는 경우가 있음

10. hashable과 불변성 간의 관계
    - 해시 테이블의 키는 불변해야 함
        - 객체가 생성된 후에 그 값을 변경할 수 없어야 함
    - 불변 객체는 해시 값이 변하지 않으므로 동일한 값에 대해 일관된 해시 값을 유지할 수 있음
    - 단 'hash 가능하다 != 불변하다'

11. 가변형 객체가 hashable 하지 않은 이유
    - 값이 변경될 수 있기 때문에 동일한 객체에 대한 해시 값이 변경될 가능성이 있음(해시 테이블의 무결성 유지 불가)
    - 가변형 객체가 변경되면 해시 값이 변경되기 때문에, 같은 객체에 대한 서로 다른 해시 값이 반환될 수 있음(해시 값의 일관성 유지 불가)
    ```
    print(hash([1,2,3]))
    my_set = {[1,2,3],1,2,3,4,5}
    my_dict = {{3,2}:'a'}
    ```

12. hashable 객체가 필요한 이유
    1. 해시 테이블 기반 자료 구조 사용
        - set와 dict의 키
        - 중복 값 방지
        - 빠른 검색과 조회
    2. 불변성을 통한 일관된 해시 값
    3. 안정성과 예측 가능성 유지

### Today **24.01.24** I learned 객체지향<br/>
---
## 1. 객체지향

### 1. 절차지향 프로그래밍
- 프로그램을 **데이터**와 **절차**로 구성하는 방식의 프로그래밍 패러다임
- 절차지향 프로그래밍 특징
    - 데이터와 해당 데이터를 처리하는 함수가 분리되어 있으며, 함수 호출의 흐름이 중요
    - 함수와 데이터가 분리 돼있음
    - 코드의 순차적인 흐름과 함수 호출에 의해 프로그램이 진행
    - 실제로 실행되는 내용이 무엇이 무엇인가가 중요
    - 데이터를 다시 재사용하기보다는 처음부터 끝까지 실행되는 결과물이 중요한 방식

소프트웨어 위기
- 하드웨어의 발전으로 컴퓨터 계산용량과 문제의 복잡성이 급격히 증가함에 따라 소프트웨어에 발생한 충격

### 2. 객체지향 프로그래밍
- 데이터와 해당 데이터를 조작하는 **메서드를 하나의 객체로 묶어** 관리하는 방식의 프로그래밍 패러다임

### 3. 차이
- 데이터와 해당 데이터를 처리하는 메서드를 하나의 객체로 묶음
- 객체 간 상호작용과 메세지 전달이 중요

## 2. 클래스
- 파이썬에서 타입을 표현하는 방법
- 객체를 생성하기 위한 설계도
- 데이터와 기능을 함께 묶는 방법을 제공

## 2. 객체
- 클래스에서 정의한 것을 토대로 메모리에 할당된 것(변수 함수 모두 다 객체)
- '속성'과 '행동'으로 구성된 모든 것

- 클래스로 만든 객체를 인스턴스 라고도 함
ex) 아이유는 객체다(o), 아이유는 인스턴스다(x), 아이유는 가수의 인스턴스다(o)

#### 객체의 특징
- 타입 : 어떤 연산자와 조작이 가능한가?
- 속성 : 어떤 상태를 가지는가?
- 조작법 : 어떤 행위를 할 수 있는가?
- 객체 = 속성 + 기능
- 클래스 선언은 파스칼 케이스(어퍼 카멜케이스)
    - `class Person:`
- 함수 선언은 스네이크 케이스
    - `def num_sum:`

### 2-1. 생성자 함수
- 객체를 생성할 때 자동으로 호출되는 특별한 메서드
- `__init__`이라는 이름의 메서드로 정의되며, 객체의 초기화를 담당
- 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정

### 2-2. 인스턴스 변수
- 인스턴스(객체)마다 별도로 유지되는 변수
- 인스턴스마다 독립적인 값을 가지며, 인스턴스가 생성될 때마다 초기화 됨

### 2-3. 클래스 변수
- 클래스 내부에 선언된 변수
- 클래스로 생성된 모든 인스턴스들이 공유하는 변수

### 2-4. 인스턴스 메서드
- 각각의 인스턴스에서 호출할 수 있는 메서드
- 인스턴스 변수에 접근하고 수정하는 등의 작업을 수행

### 2-5. 인스턴스와 클래스 간의 이름 공간(namespace)
- 클래스를 정의하면 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면 인스턴스 객체가 생성되고 독립적인 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스 > 클래스 순으로 탐색

#### 독립적인 이름 공간을 가지는 이점
- 각 인스턴스는 독립적인 메모리 공간을 가지며, 클래스와 다른 인스턴스 간에는 서로 데이터나 상태에 직접적인 접근이 불가능
- 객체지향 프로그래밍의 중요한 특성 중 하나로, 클래스와 인스턴스를 모듈화 하고 각각의 객체가 독립적으로 동작하도록 보장
- 이를 통해 클래스와 인스턴스는 다른 객체들과의 상호작용에서 서로 충돌이나 영향을 주지 않으면서 독립적으로 동작할 수 있음
- 코드의 가독성, 유지보수성, 재사용성을 높이는데 도움을 줌

## 3. 메서드

### 3-1. 인스턴스 메서드
- 클래스 내부에 정의되는 메서드의 기본
- 반드시 첫 번째 매개변수로 인스턴스 자신(self)을 전달받음

### 3-2. 생성자 메서드(`__init__`)
- 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
- 인스턴스 변수들의 초기값을 설정

### 3-3. 클래스 메서드
- 클래스가 호출하는 메서드
- 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
    1. @classmethod 데코레이터를 사용하여 정의z
    2. 호출 시, 첫번째 인자로 호출되는 클래스(cls)가 전달됨
    ```
    class Myclass:
        @classmethod
        def class_method(cls, arg1, ...):
            pass
    ```

### 3-4. 스태틱(정적) 메서드
- 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드
- 주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용
    1. @staticmethod 데코레이터를 사용하여 정의
    2. 호출 시 필수적으로 작성해야 할 매개변수가 없음
    3. 객체 상태나 클래스 상태를 수정할 수 없으며 단지 기능(행동)만을 위한 메서드로 사용

### 3-5. 메서드 정리
1. 인스턴스 메서드
    - 인스턴스의 상태를 변경하거나, 해당 인스턴스의 특정 동작을 수행

2. 클래스 메서드
    - 인스턴스의 상태에 의존하지 않는 기능을 정의
    - 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행

3. 스태틱 메서드
    - 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행

#### 각자의 역할
- 클래스가 사용해야 할 것
    1. 클래스 메서드
    2. 스태틱 메서드

- 인스턴스가 사용해야 할 것
    1. 인스턴스 메서드

#### 참고
- 매직 메서드
    - 인스턴스 메서드이다.(데코레이터가 없기 때문에)
    - 특정 상황에서 자동으로 호출되는 메서드
    - `Double underscore(__)`가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
    - 스페셜 메서드 혹은 매직 메서드라고 불림
    - 예시 `__init__`, `__str__`
    - 여기서 `__str__`은 인스턴스를 프린트 할 때 바꿀 수 있다.

### Today **24.01.25** I learned 객체지향<br/>
---
## 1. 상속
- 기존의 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것

### 1-1. 상속이 필요한 이유
1. 코드 재사용
    - 상속을 통해 기존 클래스의 속성과 메서드를 재사용 할 수 있음
    - 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용할 수 있으며, 중복된 코드를 줄일 수 있음

2. 계층 구조
    - 상속을 통해 클래스들 간의 계층 구조를 형성할 수 있음
    - 부모 클래스와 자식 클래스 간의 관계를 표현하고, 더 구체적인 클래스를 만들 수 있음

3. 유지보수의 용이성
    - 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지보수가 용이해짐
    - 코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화 할 수 있음

```
class Person:
    pass

class Professor(Person):
    pass
```

### 1-2. 부모 클래스
1. .super()
    - 불러올 때, 부모의 인자를 모두 가져와야함
    `.super()__init__(self, a, b, c)` 원하는것만 가져올 수 없음
    - 부모 클래스 객체를 반환하는 내장 함수
    - super의 2가지 사용 사례
        1. 단일 상속 구조
        - 명시적으로 이름을 지정하지 않고 부모 클래스를 참조할 수 있으므로, 코드를 더 유지 관리하기 쉽게 만들 수 있음
        - 클래스 이름이 변경되거나 부모 클래스가 교체되어도 super()를 사용하면 코드 수정이 더 적게 필요
        
        2. 다중 상속 구조
        - MRO를 따른 메서드 호출
        - 복잡한 다중 상속 구조에서 발생할 수 있는 문제를 방지

2. 다중상속
    - 둘 이상의 상위 클래스로부터 여러 행동이나 특징을 상속받을 수 있는 것
    - 상속받은 모든 클래스의 요소를 활용 가능함
    - 중복된 속성이나 메서드가 있는 경우 **상속 순서에 의해 결정됨**

3. 상속순서
    - MRO(Method Resolution Order) 알고리즘을 사용해 클래스 목록 생성
    - 부모 클래스로부터 상속된 속성들의 검색을 깊이 우선으로, 왼쪽에서 오른쪽으로, 계층 구조에서 겹치는 같은 클래스를 두번 검색하지 않음

4. mro()메서드
    - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
    - 기존의 인스턴스 > 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 > 자식 클래스 > 부모 클래스로 확장

5. MRO가 필요한 이유
    - 부모 클래스들이 여러 번 엑세스 되지 않도록, 각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 순서를 보존하고, 각 부모를 오직 한번만 호출하고, 부모들의 우선순위에 영향을 주지 않으면서 서브 클래스를 만드는 **단조적인 구조 형성**

## 2. 에러와 예외
### 2-1. 디버깅
1. 디버깅 방법
    1. print 함수 활용
    2. 개발 환경 등에서 제공하는 기능 활용
    3. Python tutor 활용

### 2-2. 에러
1. 문법에러
    1. 문법 오류
    2. 잘못된 할당
    3. EOL(End of Line)
    4. EOF(End of File)

2. 예외
    1. 내장 예외
        1. ZeroDivisionError
        2. NameError
        3. TypeError
            - 타입 불일치
            - 인자 누락
            - 인자 초과
            - 인자 타입 불일치
        4. ValueError
            - `int('1.5')`
        5. IndexError
        6. KeyError
            ```
            person = {'name': 'Alice'}
            person['age']
            ```
        7. ModuleNotFoundError
        8. ImportError
        9. KeyboardInterrupt
            - 무한루프 시 강제종료
        10. IndentationError
            - 잘못된 들여쓰기와 관련된 문법 오류

### 2-2. try와 except
1. try-except 구조
    - try 블록 안에는 예외가 발생할 수 있는 코드를 작성
    - except 블록 안에는 예외가 발생했을 때 처리할 코드를 작성
    - 예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동
    ```
    try:
        # 예외가 발생할 수 있는 코드
    except 예외:
        # 예외 처리 코드

    # 복수 예외 처리 연습
    try:
        num = int(input('100으로 나눌 값을 입력하시오 : '))
        print(100/num)
    except ValueError:
        print('숫자를 넣어주세요.')
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    except:
        print('에러가 발생하였습니다.')
    ```
    - 내장 예외 클래스는 상속 계층 구조를 가지기 때문에 except 절로 분기 시 반드시 하위 클래스를 먼저 확인 할 수 있도록 작성해야 함
    ```
    try:
        num = int(input('100으로 나눌 값을 입력하시오 : '))
    except BaseException:
        print('숫자를 넣어주세요') # 이 코드 밑으로는 동작하지 않음
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    except:
        print('에러가 발생하였습니다.')
    ```
### 참고
#### 1. as 키워드
    - as 키워드를 활용하여 에러 메세지를 except 블록에서 사용할 수 있음
```
my_list = []

try:
    number = my_list[1]
except IndexError as error:
    print(f'{error}가 발생했습니다.')

#list index out of range가 발생했습니다.
```

#### 2. EAFP, LBYL
 1. EAFP
    - 일단 실행하고 예외를 처리(try, except)
    - 예외 상황을 예측하기 어려운 경우에 유용
 2. LBYL
    - 실행하기 전에 조건을 검사(if, else)
    - 예외 상황을 미리 방지하고 싶을 때 유용