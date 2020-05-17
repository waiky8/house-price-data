#!/usr/bin/env python
# coding: utf-8

import mysql.connector

dbase = "houses"

tables = ["average_price_by_district"]
mydb = ""


def connect_sql():
    global mydb
    
    mydb = mysql.connector.connect(
        host="localhost",
        user="******",
        passwd="******",
        database=dbase
    )


def drop_table(table):
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS " + table)
    
    print(table + " table dropped!")


def close_connection():
    mydb.close()


def main():
    connect_sql()
    
    for table in tables:
        drop_table(table)
    
    close_connection()


if __name__ == "__main__":
    main()
