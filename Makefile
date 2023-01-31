test:
	coverage run -m pytest -v
coverage:
	coverage report --omit='*/site-packages/*' -m