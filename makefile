# makefile
# kai brooks
# github.com/kaibrooks/capstone-colander

.PHONY: install upgrade uninstall uninstall-brew-macos install-python3-macos test lint build-docker run-docker stop-docker version help

#SHELL:=/bin/bash
BLUE='\033[0;34m'
NC='\033[0m' # no color

install:
		@echo "\n${BLUE}Installing packages...${NC}\n"
		@curl "https://codeload.github.com/kaibrooks/capstone-colander/zip/dev" -o capstone.zip
		@unzip capstone.zip
		@rm capstone.zip
		@sudo cp -R capstone-colander-dev/* .
		@sudo rm -rf capstone-colander-dev
		@pip3 install -r requirements.txt

upgrade:
		@echo "\n${BLUE}Upgrading packages...${NC}\n"
		@pip3 install --upgrade -r requirements.txt	

install-python3-macos:
		@echo "\n${BLUE}Installing Homebrew and Python 3...${NC}\n"
		@/bin/bash -c "$$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
		@brew install python3

uninstall:
		@echo "\n${BLUE}Uninstalling packages...${NC}\n"
		@pip3 uninstall -r requirements.txt
		@sudo rm -rf io test src .github .vscode
		@sudo rm .flake8 .gitignore Dockerfile LICENSE README.md build.sh requirements.txt
		
uninstall-brew-macos:
		@echo "\n${BLUE}Uninstalling Homebrew...${NC}\n"
		@/bin/bash -c "$$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall.sh)"
		@echo "\n${BLUE}Removing /usr/local/Homebrew/...${NC}\n"
		@sudo rm -r /usr/local/Homebrew/

test:
		@echo "\n${BLUE}Running tests...${NC}\n"
		@python3 -m unittest discover -s test -v -p 'test_*.py'
		#python3 -m unittest -v 'test/SCO/test_sco.py'

lint:
		@echo "\n${BLUE}Running Flake8 against source and test files...${NC}\n"
		@flake8

build-docker:
		@echo "\n${BLUE}Building docker container${NC}\n"
		@docker build -t capstone-colander .

run-docker:
		@echo "\n${BLUE}Running Docker container...${NC}\n"
		@docker run -it --name cc --rm -v `pwd`/io:/io capstone-colander:latest bash

stop-docker:
		@echo "n${BLUE}Cleaning Docker container...${NC}\n"
		@docker stop cc; docker rm cc
		
remove-docker:
		@echo "n${BLUE}Removing Docker image...${NC}\n"
		@docker rmi capstone-colander

version:
		@echo $(shell git describe --tags --always --dirty)

help:
	@echo ''
	@echo 'Usage: make [TARGET]'
	@echo 'Targets:'
	@echo '  install                - install python packages	'
	@echo '  upgrade				- upgrade python packages	'
	@echo '  install-python3-macos	- install homebrew and python3 for macOS	'
	@echo '  uninstall				- remove python packages	'
	@echo '  uninstall-brew-macos	- uninstall homebrew for macos (keep python3)	'
	@echo '  test					- run tests	'
	@echo '  lint					- run the flake8 linter '
	@echo '  build-docker			- build the docker container'
	@echo '  run-docker				- run the docker container in a bash shell'
	@echo '  stop-docker			- stop the docker container'
	@echo '  remove-docker			- removes the docker image'
	@echo '  version				- display version from git tags '