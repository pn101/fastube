migrate:
	- python fastube/manage.py makemigrations users posts tags notifications
	- python fastube/manage.py migrate

test:
	- python fastube/manage.py test users posts tags notifications

services:
	- redis-server
