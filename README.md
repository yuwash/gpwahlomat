# gpwahlomat

An application to help voters see which political parties are the best fit to their beliefs.

# setup

1. Clone repo
2. <code>cd to repo folder</code>
3. <code>pip install -r requirements.txt</code>
4. Rename configcfg.txt to config.cfg and edit the contents.
5. You will need a local postgresql install and to have a user named wahlomat, then run this:
<code>python db_create.py</code>
6. <code>python gpwahlomat/run.py</code>

After doing this you will have a local database with the needed tables and the app can be reached at port 5000.

# setup windows
0. install Visual C++ Build Tools from http://landinghub.visualstudio.com/visual-cpp-build-tools
1. install Python3 for windows
2. install PostgreSQL from http://www.bigsql.org/postgresql/installers.jsp
3. Clone repo
4. <code>cd to repo folder</code>
5. run <code>pip install virtualenv</code> as admin
6. change in virtual environment ```call venv\Scripts\activate.bat```
7. Rename configcfg.txt to config.cfg and edit the contents.
8. to db create run follow commands in PSQL Commandline
8. create a user run ```CREATE USER wahlomat WITH Password 'wahlomat';```
9. create a DB with owner wahlomat run ```CREATE DATABASE wahlomat OWNER wahlomat;```
10. then run this <code>python db_create.py</code>
11. <code>python gpwahlomat/run.py</code>
