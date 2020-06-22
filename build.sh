# build and run the docker container
# Kai Brooks
# github.com/kaibrooks
#
chmod +x build.sh
docker build -t capstone-colander .
docker run -it --rm capstone-colander:latest