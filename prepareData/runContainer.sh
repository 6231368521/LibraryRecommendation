#!/bin/bash

exec docker build -t preparedata .

exec docker run --name preparedatacontainer -d preparedata

cont_id = docker inspect --format="{{.Id}}" preparedatacontainer

exec docker cp $cont_id:/backend /backend


