build:
	@echo "Building the project..."
	@rm -rf dist/*
	@python3 -m build
deploy:
	@echo "Deploying the project..."
	@python3 -m twine upload --repository pypi dist/*
test:
	coverage run -m pytest -v
coverage:
	coverage report --omit='*/site-packages/*' -m
fancyCov:
	coverage html --omit='*/site-packages/*'