# just run the docker container
# Kai Brooks
# github.com/kaibrooks

chmod +x run.sh # give execution privs to this script

# remove the old container
# this stops the container from continuing in the background if re-run
docker stop cc

# docker run -it --entrypoint sh capstone-colander:latest   # build to explore the container
docker run -it --name cc --rm -v `pwd`/io:/io capstone-colander:latest # gotta bind io if we want to output data