"""
This file contains methods to work with DB.

It depends on team, but it can be use SQLAlchemy library, it was made solution to use psycopg2. But goal is the same
- to create class, which can be used to work with DB. Later when you work longer with project, you can add as many
methods as the project needs. Just please keep in mind, SQLAlchemy uses more ORM (object relational mapping) methods,
psycopg2 - pure sql statements. And this sql statement depends on which DB is used in project - SQL, MySQL, MongoSQL,
etc.
"""
import logging

import psycopg2

from users.users import LOCAL_DB_USER
from users.users_forms import DataBaseUser


class DatabaseMethods:
    """
    DB methods
    """

    def __init__(self, user: DataBaseUser = LOCAL_DB_USER, log: logging = None):
        self.user = user
        self.log = log

    def create_connection(self):
        """
        Create connection to DB
        return: connection
        """
        connection = None
        try:
            connection = psycopg2.connect(user=self.user.username,
                                          password=self.user.password,
                                          host=self.user.host,
                                          port=self.user.port,
                                          database=self.user.database)
        except psycopg2.Error as error:
            self.log.error("Not connected to DB", error)
        return connection

    def return_sql_query(self, sql_query):
        """
        Returns data from DB
        :param sql_query: sql_query for executing
        :return records
        """
        connection = self.create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(sql_query)
            mobile_records = cursor.fetchall()
            return mobile_records
        except psycopg2.Error as error:
            self.log.error("Error while fetching data from Database", error)
        finally:
            connection.close()
        return None

    def update_sql_query(self, sql_query: str) -> None:
        """
        Updates data in database table/tables
        :param sql_query: sql_query for executing
        """
        connection = self.create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(sql_query)
            connection.commit()
        except psycopg2.Error as error:
            self.log.error("Error while fetching data from Database", error)
        finally:
            connection.close()

    def delete_row_from_database(self, sql_query: str) -> None:
        """
        Executing sql request in DB.
        :param sql_query: sql request
        :return: None
        """
        self.log.info('Creates new connection.')
        connection = self.create_connection()
        cursor = connection.cursor()
        self.log.info(f'Executes sql query: {sql_query}.')
        cursor.execute(sql_query)
        connection.commit()
        connection.close()
