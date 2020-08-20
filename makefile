# macos makefile

# packages
#pip3 install -r requirements.txt # install from requirements.txt
#pip3 install cycler func-timeout kiwisolver matplotlib numpy pandas Pillow pyparsing python-dateutil pytz setuptools six wheel # as listed in the docker image (docker exec cc pip list)

.PHONY: install test lint build-docker run-docker clean-docker help

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
	@echo '  install   - does install things	'
	@echo '  test	    - does test things	'
	@echo '  lint	    - run the flake8 linter '
	@echo '  version    - display version from git tags '
