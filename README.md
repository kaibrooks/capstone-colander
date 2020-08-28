# Quick Start

Capstone-Colander includes a `makefile` to install the Python environment and required packages.

## 1. Clone the repo

Run this to download the project.

```
git clone https://github.com/kaibrooks/capstone-colander
```

## 2. Set up your Python environment
This project requires Python 3. Do you have it?  

### I have Python already
Just install the Python libraries with:
```
make install
```

### I need to install Python on a Mac
Install Python 3 using [Homebrew](https://brew.sh) with:
```
make install-python3-macos
make install
```
Note: You can install Python 3 without Homebrew by following the *install Python3 on a different OS* below.

### I need to install Python 3 on a different OS
[Download Python here](https://www.python.org/downloads/release/python-385/ "Download Python here"), then run
```
make install
```

### I don't know if I have Python
Check with
```
python --version
```

### I want to use Docker
Download a container from the Docker Hub:
```
docker pull (...coming soon)
```

## 3. Run the project
Run the project with
```
python3 main.py
```

See the next section for more details on using Capstone-Colander

# Running capstone-colander
