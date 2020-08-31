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

Just install the project's Python libraries with:

```
make install
```

### I need to install Python on a Mac

Install Python 3 using [Homebrew](https://brew.sh) with:

```
make install-python3-macos
make install
```

Note: You can install Python 3 without Homebrew by following the _install Python3 on a different OS_ below.

### I need to install Python 3 on a different OS

[Download and install Python here](https://www.python.org/downloads/release/python-385/ "Download Python here"). Then, install the project's Python libraries with:

```
make install
```

### I don't know if I have Python

Check with:

```
python --version
```

### Alternative: I want to use Docker

Download the project's container from the Docker Hub with:

```
docker pull (...coming soon)
```

## 3. Run the project

Run the project with

```
python3 main.py
```

See the next section for more details on using capstone-colander

# Running capstone-colander

(Detailed information here)

# Removing capstone-colander

## Non-Docker installation

### Uninstall the Python packages the software uses

```
make uninstall
```

### (macOS) Uninstall Python3

```
brew uninstall python3
```

### (macOS) Uninstall Homebrew

```
make uninstall-brew-macos
```

### (Linux) Uninstall Python3

**DANGER ZONE**

```
sudo apt-get remove 'python3.*'
```

## Docker installation

The Docker image contains its own packages and Python interpreter, and doesn't need any other commands.

### Remove the Docker image

```
make remove-docker
```

# Developing capstone-colander

## Code Conventions

### Casing

A schism over camelCase vs. worm_case threatened to tear this project apart. This project uses both conventions, generally with camelCase for external-facing variables from CSV files, and worm_case for internal variables and file names.

The linter configuration stylizes for worm case.

## Dev environment

The project was developed and tested inside a Docker container, from the _Dockerfile_ build associated with its release in **master**.

## Linting

This project uses the [flake8](https://github.com/PyCQA/flake8) linter, with _.flake8_ in the project root containing the linter settings.

## Docker

## Test

## Methodology

## Releases

We post tested, released versions of the code base in **master**, with a release version according to the written specification.
