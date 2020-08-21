# macos makefile
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" # install homebrew 

brew install python3 # install python 3

# packages
pip3 install -r requirements.txt # install from requirements.txt
pip3 install cycler func-timeout kiwisolver matplotlib numpy pandas Pillow pyparsing python-dateutil pytz setuptools six wheel # as listed in the docker image (docker exec cc pip list)