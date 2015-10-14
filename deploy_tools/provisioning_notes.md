Provisioning a new site
=======================

## Required packages:
* nginx
* python3
* git
* pip
* virtualenv

eg, on ubuntu:
	sudo apt-get install nginx git python3 python3-pip
	sudo pip install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, agustin01.cloudapp.net

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, agustin01.cloudapp.net

# Folder structure:
Assume we have a user account at /home/username

/home/username
	sites
		SITENAME
			database
			source
			static
			virtualenv
