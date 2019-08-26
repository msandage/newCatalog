A README file is included in the GitHub repo containing the following information: 

IP address: 100.27.8.112

URL: http://100.27.8.112.xip.io

Summary of software installed: Python, Apache, mod_wsgi, Flask, pip, Ubuntu16, SQLAlchemy, SQLite3

Summary of configurations made: 
Changed the SSH port from 22 to 2200. 
Disabled all incoming ports (including 20) except 80, 123, 2200, and Apache. 
Disabled remote root login.
Added user grader with password "grader" and sudo privileges.
Added authorized keys for each user.

List of third-party resources used to complete this project:
Flask mod_wsgi documentation https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/
DigitalOcean deployment tutorial https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
