Language - Python

Framework - Django

Database - PostrgeSQL + PostGIS

Deploy.

1 Create virtualenvironment

virtualenv fbr_ve

2 Clone repo

cd fbr_ve

git clone git@github.com:zdimon/fbr.git

Update project

git pull

sudo apt-get purge postgres*
sudo apt-get purge postgis*
sudo apt-get purge gdal*

sudo rm -rf /var/lib/postgresql/
sudo rm -rf /var/log/postgresql/
sudo rm -rf /etc/postgresql/

http://www.ubuntuupdates.org/package/core/precise/main/updates/postgresql-server-dev-9.1
http://www.ubuntuupdates.org/package/core/precise/main/updates/postgresql-client-9.1

sudo passwd postgres

sudo -s -u postgres

psql

\password postgres

выходим из psql по ctrl+d





