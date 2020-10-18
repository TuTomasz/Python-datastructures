.PHONY: setup build install-build uninstall-build publish clean test lint

# Setup Constants
POETRY_VERSION = 1.0.10

# Set up environment and install dependencies
setup:
	make clean
	@echo Install Poetry Version $(POETRY_VERSION)
	[ -f ./poetry.lock ] && rm -r poetry.lock || echo lock file not found
	pip install --upgrade --force-reinstall 'poetry==$(POETRY_VERSION)'
	@echo 🧰 Installing  Dependencies 
	poetry install

# build datastructure package localy
build:
	@echo 🏗️ Initializing New Build
	make -k clean 
	make test
	make lint
	@echo 🔧 Building Packages
	poetry build

# install built package globaly on your computer with pip
install-build:
	@echo 💿 Install build 
	pip install dist/*.tar.gz

# uninstall built package globaly on your computer with pip
uninstall-build:
	@echo 💿 UnInstall build 
	pip uninstall python-datastructures

# publish to pypi
publish:
	@echo ✈️ Publish build to Pypi
	poetry publish 

clean:
	@echo 🧹 cleanup
	rm -r ./dist/ || echo dir file not found

# run unit tests
test:
	@echo 🧪 Running Tests
	poetry run pytest tests/

# format code
lint:
	@echo ♻️ Reformatting Code
	poetry run black .

