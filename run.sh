#!/bin/bash

docker run --rm -it \
	--gpus all \
	--name molmod \
	--mount type=bind,source=$(pwd)/scripts,target=/home/molmod \
	-p 8000:8000 \
	horvathi/molmod \
	jupyter notebook --no-browser --ip 0.0.0.0 --port 8000 /home/molmod
