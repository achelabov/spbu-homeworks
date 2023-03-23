postgres.start:
	if [ ! "$(shell docker ps -q -f name=hw-dbs)" ]; then \
        docker run -d -p 1337:5432 -e POSTGRES_PASSWORD=1337 --name hw-dbs postgres:13 ; \
    fi; \ 
	docker start hw-dbs

postgres.stop:
	docker stop hw-dbs
	docker rm hw-dbs

migrate.up:
	goose -dir . postgres "host=localhost port=1337 user=postgres password=1337 dbname=pet sslmode=disable" up

migrate.down:
	goose -dir . postgres "host=localhost port=1337 user=postgres password=1337 dbname=pet sslmode=disable" down

