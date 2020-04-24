#!/bin/sh

git pull
docker build -t testapp_img .
docker tag testapp_img bogdanpolitic/idp:try_14_04
docker push bogdanpolitic/idp:try_14_04
docker stack rm testapp
docker stack deploy -c docker-compose-visualize.yml testapp
