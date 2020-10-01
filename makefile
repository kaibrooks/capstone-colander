# makefile
# kai brooks
# github.com/kaibrooks/capstone-colander

.PHONY: install upgrade uninstall uninstall-brew-macos install-python3-macos test lint build-docker run-docker stop-docker version help

#SHELL:=/bin/bash
BLUE='\033[0;34m'
NC='\033[0m' # no color

install:
		@echo "\n${BLUE}Installing packages...${NC}\n"
		@curl "https://codeload.github.com/kaibrooks/capstone-colander/zip/master" -o capstone.zip
		@unzip capstone.zip
		@rm capstone.zip
		@sudo cp -R capstone-colander-master/. .
		@sudo rm -rf capstone-colander-master
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
		@sudo rm .gitignore LICENSE requirements.txt assign.py geneticalgorithm.py write_csv.py prints.py main.py score.py load_csv.py

uninstall-brew-macos:
		@echo "\n${BLUE}Uninstalling Homebrew...${NC}\n"
		@/bin/bash -c "$$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall.sh)"
		@echo "\n${BLUE}Removing /usr/local/Homebrew/...${NC}\n"
		@sudo rm -r /usr/local/Homebrew/

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
	@echo '  version				- display version from git tags '
