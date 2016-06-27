migrate:
	- python fastube/manage.py makemigrations users posts tags
	- python fastube/manage.py migrate

test:
	- python fastube/manage.py test users posts tags
