#!/bin/sh

if [ "$#" -ne 1 ]; then
    echo "Provide the name of the container as an argument!"
    exit 1
fi

docker run -ti --mount type=bind,source="$(pwd)"/,target=/frontend/app -p 80:8000 $1