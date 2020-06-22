# Introduction


## Small heading

This does `a thing` I think.

# Running capstone-colander
*All of the methods below accomplish the same result.*
## Using Docker (Recommended)

Docker keeps all necessary components on the project together, such as packages, dependencies, and the correct Python version. This containerization ensures the user doesn't need to download or manage any external frameworks and the project continues to function through changes in packages/OS/Python version.

This requires [Docker](https://www.docker.com/products/docker-desktop "Download Docker").

In the command line (make sure Docker Desktop is running):

```
docker run -it --rm kaibrooks/capstone-colander:latest
```

This command downloads the pre-built container from the Docker Hub and runs it.

## 2. Building the container yourself
This method produces the same result as the above, except you build the container yourself instead of pulling a ready-to-run copy.

Navigate to the root directory of the project, where `Dockerfile` is located:
```
docker build -t capstone-colander .
```
When successful, the CLI outputs: `Successfully tagged capstone-colander:latest`

Run the newly-built container with 
```
docker run -it --rm capstone-colander:latest
```


## 3. Running from source
This method does not require Docker, but requires a specific Python environment:

* Python 3.8-buster

# Developer Installation