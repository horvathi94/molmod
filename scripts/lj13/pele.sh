#!/bin/bash

docker run --rm -it \
	--name pele \
	--mount type=bind,source=$(pwd),target=/home/pele \
	horvathi/pele \
	bash
