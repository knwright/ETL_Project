# ETL_Project

1) Extract ASIN numbers from 21stCenturyBooks_Amazon.csv and use them to create unique query urls to scrape Amazon.com for the following:
    - Book Title
    - Amazon's Price
    - List Price
    - ISBN-10
    - Product Dimensions
    - Customer Rating

2) Save the scraped data as Amazon_Book_Data.csv.

3) Build the sqlite database that includes data from Amazon_Book_Data.csv and Lerner_Product_internal.csv into it.

4) The primary purpose of this schema is to compare Amazon's price with Lerner Publishing's list price for 21st Century Books.



URL for Amazon scrape = http://www.amazon.com/dp/{ASIN}


