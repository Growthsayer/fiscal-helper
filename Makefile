build:
  @echo "Building the project..."
	python -m build
	@echo "Deleting files in the dist/ folder..."
	rm -rf dist/*
deploy:
	@echo "Deploying the project..."
	twine python -m twine upload --repository pypi dist/*
test:
	coverage run -m pytest -v
coverage:
	coverage report --omit='*/site-packages/*' -m
fancyCov:
	coverage html --omit='*/site-packages/*'