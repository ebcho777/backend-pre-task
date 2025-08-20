# 테스트 코드 실행 방법

1. schema.sql을 이용하여, DB와 테이블 생성
2. (optional) data.sql을 이용하여, 테이블에 데이터 주입
3. docker compose up --build
   기타)
   - .env 에 mysql 의 DB_NAME, DB_USER, DB_PASSWORD 등의 정보가 있습니다.
   - 테스트 DB 이고, 별 다른 가치가 없으므로 repo에 같이 올렸습니다.
   - schema.sql 과 .env에 DB_NAME은 mydatabase로 해놓았는데, 2개의 값이 같아야 합니다.
   - docker compose up 수행시, DB 컨테이너가 올라오기까지는 시간이 조금 걸립니다.

# ENDPOINT

## API Endpoint

http://localhost:8000/api/contacts/

## SWAGGER

http://localhost:8000/api/docs/
