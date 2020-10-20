# UK House Prices
This was similar to the way data was compiled for schools (https://github.com/waiky8/schools-data), this time querying Zoopla instead.
Again, **beautiful soup** was used to traverse the website, creating a transitional csv file and finally loading the data into **MySQL**.

UK postal districts was used to capture a complete dataset. In addition, a timestamp was added to allow for updated prices to be added subsequently. 

Note, this same data was converted to **sqlite** so that it could be used by another application (https://github.com/waiky8/schools-view).
