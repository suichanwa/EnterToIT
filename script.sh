#!/bin/bash

#run docker deamon for arch linux 
sudo systemctl start docker

#check if docker is started
#sudo systemctl status docker

#run arch linux on docker 
#and then connect to it


#download docker debian localy 

#react docker image with debian
sudo docker build -t debian .

