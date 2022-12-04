#!/bin/bash

# Start docker container
docker run --rm -it \
	--gpus all \
	--name hoomd-blue \
	--mount type=bind,source=$(pwd),target=/home/molmod \
	-p 8000:8000 \
	glotzerlab/software \
	jupyter notebook --no-browser --ip 0.0.0.0 --port 8000 /home/molmod
