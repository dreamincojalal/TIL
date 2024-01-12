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