# house-price-data
This is similar to the way I compiled data regarding schools (https://github.com/waiky8/schools-data) but instead of querying Ofsted I queried Zoopla.
Again, I used **beautiful soup** to crawl the website, created a transitional csv file and finally loaded it into **MySQL**.

I used UK postal districts to try and capture a more complete dataset. In addition, a timestamp was added to allow for updated prices to be added later on. 

Note, this same data was converted to SQLite so that it could be used by another application (https://github.com/waiky8/schools-view).
