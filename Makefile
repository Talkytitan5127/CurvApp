build:
	docker-compose build

up:
	docker-compose up -d

run:
	docker-compose build
	docker-compose up -d

connect-db:
    docker exec -it db mysql -u rafikov -p
