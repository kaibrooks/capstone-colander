# build and run the docker container
# Kai Brooks
# github.com/kaibrooks
#
chmod +x build.sh # give execution privs to this script
docker build -t capstone-colander . # build it

# docker run -it --entrypoint sh capstone-colander:latest   # build to explore the container
docker run -it --rm -v `pwd`/io:/io capstone-colander:latest # gotta bind io if we want to output data