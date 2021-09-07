dev-infra:
	cd infra/docker/ && docker-compose up -d

dev-api:
	cd src/ && uvicorn api:app --reload

api-dependencies:
	pip3 install -r requirements.txt
