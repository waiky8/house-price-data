#!/usr/bin/env python
# coding: utf-8

import bs4 as bs
import urllib.request
import csv
import datetime as dt
from datetime import datetime
import time

zoopla = "https://www.zoopla.co.uk/house-prices/browse/"

header = ["Postal District", "Average Price", "Date"]

inp_f = out_f = ""
f_in = f_out = writer = ""
avg_price = today_date = ""
num = 0


def extract_data(district, zoopla_data):
    global avg_price
    
    avg_price = ""
    
    print(zoopla_data)
    if not zoopla_data:
        print("No data for: ", district)
    else:
        avg_price = zoopla_data.get_text()

    write_data(district, avg_price, today_date)


def open_files():
    global f_in, f_out, writer
    
    f_in = open(inp_f, "r")
    f_out = open(out_f, "w", newline="")

    writer = csv.writer(f_out)
    write_header()


def read_zoopla_page(url):
    print(url)

    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source, "lxml")
    extract = soup.find(class_="market-panel-stat-element-value js-market-stats-average-value")
    
    return extract


def write_header():
    writer.writerow(header)


def write_data(l_district, l_avg_price, l_today_date):
    global num
    
    num += 1
    writer.writerow([l_district, l_avg_price, l_today_date])
    print(num, ">>>", l_district, l_avg_price, l_today_date)


def close_files():
    f_in.close()
    f_out.close()


def main():
    global inp_f, out_f, today_date

    start_time = time.time()

    today_date = datetime.today().strftime('%Y%m%d')

    for i in range(3):
        if i == 0:
            inp_f = "data/postal_districts_set1_a_to_g.txt"
            out_f = "data/house_prices_set1_a_to_g_" + today_date + ".csv"
        elif i == 1:
            inp_f = "data/postal_districts_set2_h_to_n.txt"
            out_f = "data/house_prices_set2_h_to_n_" + today_date + ".csv"
        else:
            inp_f = "data/postal_districts_set3_o_to_z.txt"
            out_f = "data/house_prices_set3_o_to_z_" + today_date + ".csv"

        open_files()

        for district in f_in:
            district = district.rstrip("\n")
            zoopla_data = read_zoopla_page(zoopla + district + "/")
            extract_data(district, zoopla_data)

        close_files()
    
    elapsed_time = time.time() - start_time
    print("\n", dt.timedelta(seconds=elapsed_time))


if __name__ == "__main__":
    main()
