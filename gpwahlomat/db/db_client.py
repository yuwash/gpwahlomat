import configparser
import psycopg2


config = configparser.ConfigParser()
config.readfp(open('config.cfg'))
dbname = config.get('db', 'name')
user = config.get('db', 'user')
host = config.get('db', 'host')
port = config.get('db', 'port')
password = config.get('db', 'password')


def database_connection():
    connection = psycopg2.connect(
        host=host, port=port, user=user, password=password, database=dbname)
    connection.set_session(autocommit=True)

    return connection
