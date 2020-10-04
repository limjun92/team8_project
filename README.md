# team8_project

## RunUP

### db가 없을 경우 db를 생성

1. 0001_initial.py 와 db.sqlite3 있다면 삭제
2. TERMINAL = > python manage.py makemigrations
3. db.sqlite3 가 생성된다면 삭제
4. TERMINAL = > python manage.py migrate
5. 0001_initial.py와 db.sqlite3의 생성을 확인
6. python manage.py runserver
7. 웹 페이지로 이동시 db를 생성을 기다려야 함(약 1시간)

### db가 생성되어 있을 경우 실행

1. python manage.py runserver
