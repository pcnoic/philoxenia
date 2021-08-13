dev-infra:
	cd infra/docker/ && docker-compose up

dev-client:
	cd client/ && quasar dev

dev-api:
	cd src/ && uvicorn api:app --reload

client-dependencies:
	cd client/ && npm install

api-dependencies:
	pip3 install -r requirements.txt
