# Docker-Compose-PostgreSQL
 use PostgreSQL with Docker-Compose

## 파일 설명
- `app` : PostgreSQL 실행할 파이썬 스크립트 저장 디렉터리
  - main.py : main 함수
  - pgsqltool.py : PostgreSQL Connection 클래스
- `.env` : 환경변수 설정(ex. PostgreSQL 설정정보 등)
- `docker-compose.yml` : docker-compose 설정
- `dockerfile` : 도커 컨테이너 설정
- `requirements.txt` : Python 라이브러리 설치 요소


## CentOS 7 기준 실행 방법

- `.env` 파일에 PostgreSQL의 HOST, DATABASE, USERNAME, PASSWORD, PORT 등 설정
- `app` 디렉터리 안에 main.py 를 통해 PostgreSQL 조회.
- `docker-compose.yml` 파일이 존재하는 디렉터리 상에서 다음과 같은 명령어를 수행해 Docker-Compose 실행
  - `docker-compose up [-option] [-service]` : 컨테이너 생성 및 실행
    - [option]
      - -d : 백그라운드 실행
      - -no-deps : 링크 서비스 실행하지 않음
      - -build : 이미지 빌드
      - -t : 타임아웃 지정(Default 10 Sec)
  - `docker-compose ps` :현재 동작 중인 컨테이너 상태 확인
  - `docker-compose logs` : 컨테이너의 로그 출력
  - `docker-compose run` : docker-compose up 명령어를 이용해 생성 및 실행된 컨테이너에서 임의의 명령을 실행하기 위해 사용.
    - 예를 들어 특정 서비스에서 /bin/bash 를 실행시켜 쉘 환경으로 집입하고자 하면 다음과 같이 수행한다.
      - `docker-compose run [Service name][command]`
      - `docker-compose run postgres /bin/bash`
  - `docker-compose [start/stop/pause/unpause/restart]
    - 여러개 서비스 또는 특정 서비스 시작, 정지, 일시정지, 일시정지 해제, 재시작 수행
  - `docker-compose rm` : docker-compose로 생성한 컨테이너 일괄 삭제
  - `docker-compose kill` : 실행중인 컨테이너를 강제로 정지 
  - `docker-compose [-rmi] down` : 네트워크 정보, 볼륨 컨테이너들을 일광 정지 및 삭제
  - `docker-compose port` : 서비스 프라이빗 포트 번호의 설정을 확인
  - `docker-compose config` : docker-compose의 구성 파일 내용 확인 가능


## Virtual Box를 통한 local PostgreSQL 접속 시 에러 처리

- listen 문제
  - vitualbox 설정 - 네트워크 - 어뎁터1 -고급 -포트포워딩에 PostgreSQL 포트 추가(ex.5432)

- Server Connecting Error
  ``` 
  Error connecting to the server.
  server closed the connection unexpectedly
  This probably meas the server terminated abnormally before or while processing the request.
  ```
  - local의 Postgresql 디렉터리의 postgresql.conf 설정 변경(postgresql/data/postgresql.conf)
    ```
    #------------------------------------------------------------------------------
    # CONNECTIONS AND AUTHENTICATION
    #------------------------------------------------------------------------------

    # - Connection Settings -

    listen_addresses = '*'		# what IP address(es) to listen on;
	    				# comma-separated list of addresses;
		    			# defaults to 'localhost'; use '*' for all
			    		# (change requires restart)
    port = 5432				# (change requires restart)
    ```
    - listen_address 부분을 'localhost' 에서 *(와일드카드)로 변경

- Access to database denied 에러
  ```
  FATAL: no pg_hba.conf entry for host "192.168.56.1", user "testuser", database "test"..
  ```
  - local의 Postgresql 디렉터리의 pg_hba.conf 파일 다음과 같이 수정(postgresql/data/pg_hba.conf)
    ```
    # TYPE  DATABASE        USER            ADDRESS                 METHOD

    # "local" is for Unix domain socket connections only
    local   all             all                                     trust
    # IPv4 local connections:
    host    all             all             0.0.0.0/0            trust
    # IPv6 local connections:
    host    all             all             ::1/128                 trust
    # Allow replication connections from localhost, by a user with the
    # replication privilege.
    local   all     all                                     trust
    host    all     all             127.0.0.1/32            trust
    host    all     all             ::1/128                 trust
    ```


