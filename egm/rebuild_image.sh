#!/bin/bash -e

# construyo la imagen inicial
rm -Rf .docker/tmp/base/ #borra la carpeta temporal
mkdir -p .docker/tmp/base/.docker; #vuelve a crear
cp Dockerfile .docker/tmp/base/Dockerfile; #copia el Dockerfile
cp requirements.txt .docker/tmp/base/requirements.txt;
cp run.sh .docker/tmp/base/run.sh;
cd .docker/tmp/base/ && docker build --tag buho/egm .; # construyá la imagen
rm -Rf .docker/tmp
cd ../../../
