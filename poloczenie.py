import psycopg2
from settings import connection_info


def connection(ci=None):
    if ci is None:
        ci = connection_info
    connection = psycopg2.connect(**ci)
    connection.autocommit = True
    return connection
