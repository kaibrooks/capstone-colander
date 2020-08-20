# makefile
# kai brooks
# github.com/kaibrooks/capstone-colander

.PHONY: install install-python3-macos test lint build-docker run-docker stop-docker version help

BLUE='\033[0;34m'
NC='\033[0m' # no color

# This version-strategy uses git tags to set the version string
TAG := $(shell git describe --tags --always --dirty)

install:
		@echo "\n${BLUE}Installing packages...${NC}\n"
		# as listed in the docker image (docker exec cc pip list)
		@pip3 install cycler func-timeout kiwisolver matplotlib numpy pandas Pillow pyparsing python-dateutil pytz setuptools six wheel 
		
install-python3-macos:
		@echo "\n${BLUE}Installing Python 3...${NC}\n"
		/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" # install homebrew 
		brew install python3 # install python 3

test:
		@echo "\n${BLUE}Running tests...${NC}\n"
		@python3 -m unittest discover -s test -v -p 'test_*.py'
		#python3 -m unittest -v 'test/SCO/test_sco.py'

lint:
		@echo "\n${BLUE}Running Flake8 against source and test files...${NC}\n"
		flake8

build-docker:
		@echo "\n${BLUE}Building docker container${NC}\n"
		docker build -t capstone-colander .

run-docker:
		@echo "\n${BLUE}Running Docker container...${NC}\n"
		docker run -it --name cc --rm -v `pwd`/io:/io capstone-colander:latest

stop-docker:
		@echo "n${BLUE}Cleaning docker container${NC}\n"
		docker stop cc; docker rm cc
		
version:
		@echo $(TAG)

help:
	@echo ''
	@echo 'Usage: make [TARGET]'
	@echo 'Targets:'
	@echo '  install                - install python packages	'
	@echo '  install-python3-macos	- install homebrew and python3 for macOS	'
	@echo '  test					- run tests	'
	@echo '  lint					- run the flake8 linter '
	@echo '  build-docker			- build the docker container'
	@echo '  run-docker				- run the docker container'
	@echo '  stop-docker			- stop the docker container'
	@echo '  version				- display version from git tags '