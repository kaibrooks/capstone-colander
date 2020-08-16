# build and run the docker container
# Kai Brooks
# github.com/kaibrooks
# use 'docker exec cc pip list' to list all the packages the container uses

chmod +x build.sh # give execution privs to this script
docker build -t capstone-colander . # build it

# remove the old container
# this stops the container from continuing in the background if re-run
docker stop cc

# docker run -it --entrypoint sh capstone-colander:latest   # build to explore the container
docker run -it --name cc --rm -v `pwd`/io:/io capstone-colander:latest # gotta bind io if we want to output data