#!/usr/bin/env python
# coding: utf-8

import mysql.connector
import csv
import glob
import datetime
import time

inp_files = sorted(glob.glob("data/house_prices_*_20200417.csv"))
print(inp_files)

dbase = "houses"
tables = ["average_price_by_district"]
mydb = f_in = ""
columns = values = now = num = ""
r_postcode_district = r_avg_price_num = r_date = ""


def connect_sql():
    global mydb

    mydb = mysql.connector.connect(
        host="localhost",
        user="waiky",
        passwd="Programallday1!",
        database=dbase
    )


def get_columns(table):
    global columns, values, now

    columns = ""
    values = ""

    now = datetime.datetime.now()

    if table == "average_price_by_district":
        columns = "(postcode_district, average_price, date, timestamp) VALUES (%s, %s, %s, %s)"
        values = (r_postcode_district, r_avg_price_num, r_date, now)

    else:
        print("Unrecognised table: " + table)


def write_table(table):
    mycursor = mydb.cursor()

    sql = "REPLACE INTO " + table + " " + columns
    val = values

    print(sql, val)
    mycursor.execute(sql, val)
    mydb.commit()


def close_connection():
    mydb.close()


def open_files(f):
    global f_in

    f_in = open(f, "r")


def close_files():
    f_in.close()


def main():
    global r_postcode_district, r_avg_price_num, r_date
    global num

    start_time = time.time()

    connect_sql()

    num = 0

    for f in inp_files:
        open_files(f)

        header = True

        for row in csv.reader(f_in):
            r_postcode_district = row[0]
            r_avg_price = row[1]
            r_date = row[2]

            if r_avg_price in ("", "—"):
                r_avg_price_num = 0.00
            else:
                r_avg_price_num = r_avg_price.replace("£", "").replace(",", "")

            print(r_avg_price, " converted ", r_avg_price_num)

            if header:
                header = False
                continue

            num += 1
            print(num, ">>>", r_postcode_district, r_avg_price)
            for table in tables:
                get_columns(table)
                write_table(table)

        close_files()

    close_connection()

    print("\n", num, " records inserted.")

    elapsed_time = time.time() - start_time
    print("\n", datetime.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
