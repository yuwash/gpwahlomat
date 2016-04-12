# gpwahlomat

An application to help voters see which political parties are the best fit to their beliefs.

# setup

1. Clone repo
2. <code>cd to repo folder</code>
3. <code>pip install -r requirements.txt</code>
4. You will need a local postgresql install and to have a user named wahlomat, then run this:
<code>python db_create.py</code>
5. <code>hug -f gpwahlomat/api/run.py</code>

After doing this you will have a local database with the needed tables and your port 8000 will be listening for requests to the specified addresses.

