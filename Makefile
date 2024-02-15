manage_py := docker compose exec -it backend python ./app/manage.py

run:
	$(manage_py) runserver 0.0.0.0:8000

makemigrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

shell:
	$(manage_py) shell_plus --print-sql

createsuperuser:
	$(manage_py) createsuperuser

flake:
	docker compose exec -it backend flake8 app/

worker:
	cd app && celery -A settings worker -l info --autoscale 1,10

beat:
	cd app && celery -A settings beat -l info

pytest:
	docker compose exec -it backend pytest app/tests --cov=app --cov-report html && coverage report --fail-under=75.4477

gunicorn:
	cd app && gunicorn --workers 4 settings.wsgi --timeout 30 --max-requests 10000 --log-level debug --bind 0.0.0.0:8000

collectstatic:
	$(manage_py) collectstatic --no-input && \
	docker cp backend:/tmp/static /tmp/static && \
	docker cp /tmp/static nginx:/etc/nginx/static
