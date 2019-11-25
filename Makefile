build:
	docker-compose build

up:
	docker-compose up -d

run:
	make build
	make up