"""
This file contains users, whose are created from user classes
"""
from users.users_forms import DataBaseUser, WebUser

DB_USER = DataBaseUser(
    username='dbadmin',
    password='sdgasgas',
    host='localhost',
    port='5432',
    database='db_name',
)
DB_QA_USER = DataBaseUser(
    username='dbadmin',
    password='clpocdbadmin123',
    host='here_we_add_host',
    port='5432',
    database='db_name',
)

LOCAL_DB_USER = DataBaseUser(
    username="postgres",
    password="mysecretpassword",
    host="localhost",
    port="25432",
    database="db_name",
)

WB_USER = WebUser(
    email='fdjfdfj@orioninc.com',
    password='asfhgpfdohmpoh1196',
    port=8080,
)
