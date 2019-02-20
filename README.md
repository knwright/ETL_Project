# ETL_Project

1) Extract ASIN numbers from lerner_catalog_data.csv and use them to create unique query urls to scrape Amazon.com for the following:
    - Book Title
    - Barnes and Noble's Price
    - List Price
    - ISBN-10
    - Product Details
    - Customer Rating

2) Save the scraped data as Barnes_book_data.csv.

3) Build the sqlite database that includes data from barnes_Book_Data.csv and Lerner_Product_internal.csv into it.

4) The primary purpose of this schema is to compare Amazon's price with Lerner Publishing's list price for 21st Century Books.



URL for Amazon scrape = 'http://search.barnesandnoble.com/bookSearch/isbnInquiry.asp?isbn={ISBN}


