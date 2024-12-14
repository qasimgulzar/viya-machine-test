pre-requirements: ## install Python requirements for running pip-tools
	pip install -r requirements/pip.txt
	pip install -r requirements/pip-tools.txt

compile-requirements: pre-requirements
	pip-compile -v --allow-unsafe ${COMPILE_OPTS} -o requirements/base.txt requirements/base.in

local-requirements:
	pip install -r requirements/base.txt

base-requirements: pre-requirements
	pip-sync requirements/base.txt
	make local-requirements
#init-alembic:
#	docker compose exec app alembic init -t async migrations
#make-migrations:
#	docker compose exec app alembic revision --autogenerate
#migrate:
#	docker compose exec app alembic upgrade head