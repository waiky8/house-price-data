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
        user="waiky",
        passwd="Programallday1!",
        database=dbase
    )


def create_table(table, columns):
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE " + table + "(" + columns + ")")

    print(table + " table created!")


def get_columns(table):
    columns = ""

    if table == "average_price_by_district":
        columns = ("postcode_district VARCHAR(10) NOT NULL, "
                   "average_price FLOAT(10,2), "
                   "date VARCHAR(8), "
                   "timestamp TIMESTAMP, "
                   "PRIMARY KEY (postcode_district)"
                   )

    else:
        print("Unrecognised table: " + table)

    return columns


def close_connection():
    mydb.close()


def main():
    connect_sql()

    for table in tables:
        columns = get_columns(table)
        if columns == '':
            continue
        else:
            create_table(table, columns)

    close_connection()


if __name__ == "__main__":
    main()
