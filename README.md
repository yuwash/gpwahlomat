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

