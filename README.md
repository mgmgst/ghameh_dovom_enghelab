# ghameh_dovom_enghelab

This project is done for ghameh_dovom_enghelab classes as a project series.

## How to run

1. Install python3, pip3, virtualenv, MySQL in your system.

2. Clone the project `https://github.com/mgmgst/ghameh_dovom_enghelab.git` && cd sms_serial_verification

3. in the app folder, rename the `config.py.sample` to `config.py` and do proper changes.

4. run this comand in MYSQL database : `CREATE DATABASE myworks;`

5. run this comand in MYSQL database : `CREATE USER 'myworks'@'localhost' IDENTIFIED BY 'works';`

6. run this comand in MYSQL database : `GRANT ALL PRIVILEGES ON myworks.* TO 'myworks'@'localhost';`

7. run this comand in MYSQL database : `DROP TABLE IF EXISTS works`

8. db configs are in config.py. Create the db and grant all access to the specified user with specified password, but you also need to add this table to the database manually: `CREATE TABLE works (name VARCHAR(100),title VARCHAR(100),message VARCHAR(250));`

9. Create a virtualenve named build using `virtualenv -p python3 venv`

10. Connect to virtualenv using `source venv/bin/activate`

11. From the project folder, install packages using `pip install -r ./app/requirements.txt`

12. Now environment is ready. Run it by `python app/main.py`

### Or you can use Dockerfile 
