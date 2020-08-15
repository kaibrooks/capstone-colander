# Running capstone-colander
*The methods below all accomplish the same result.*
## Using Docker (Recommended)

Docker keeps all necessary components on the project together, such as packages, dependencies, and the correct Python version. This containerization ensures the user doesn't need to download or manage any external frameworks and the project continues to function through changes in packages/OS/Python version.

This requires [Docker](https://www.docker.com/products/docker-desktop "Download Docker").

This project contains `build.sh`, a script that builds the container and runs the code inside. In the command line, from the project root directory (the directory containing `build.sh`):

```
./build.sh
```

Opening `/build.sh` in an editor reveals the individual commands it runs.

## Running from source (hard mode)
This project development environment is the Python 3.8-buster image. `requirements.txt` contains additional packages the project uses.

With the above environment, run:

```
python3 main.py
```