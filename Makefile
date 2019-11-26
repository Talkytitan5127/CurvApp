build:
	docker-compose build

up:
	docker-compose up -d

run:
	docker-compose build
	docker-compose up -d

connect_db:
	docker exec -it db mysql -u rafikov -p

down:
	docker-compose down

restart:
	make down
	make build
	make up
