#!/bin/bash


# Set env variables
readonly SSH_PSWD=raspberry
readonly PROJECT_NAME=b-control-frontend
readonly TARGET_HOST=pi@192.168.178.201
readonly TARGET_PATH=/home/pi/projects/b-control-backend
readonly SOURCE_PATH=./src/*

export PKG_CONFIG_ALLOW_CROSS=1

# Delete target directory on target
sshpass -p ${SSH_PSWD} ssh ${TARGET_HOST} "rm -rf ${TARGET_PATH}/*"

# Copy binary to target
sshpass -p ${SSH_PSWD} scp ${SOURCE_PATH} ${TARGET_HOST}:${TARGET_PATH}
