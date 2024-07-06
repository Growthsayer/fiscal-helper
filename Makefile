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
fullDeploy:
	@echo "Creating the virtual environment..."
	@python3 -m venv venv
	@echo "Activating the virtual environment and upgrading packages..."
	@bash -c "source venv/bin/activate && \
	pip install --upgrade hatchling build && \
	pip install --upgrade twine"
	@echo "Building and deploying the project..."
	@make build
	@make deploy
	@echo "Deactivating the virtual environment..."
	@bash -c "source venv/bin/activate && deactivate"