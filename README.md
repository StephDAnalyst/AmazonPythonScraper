# Amazon Phone Search Scrapy Project

This Scrapy project is designed to scrape phone product information from Amazon's search results. It utilizes Scrapy, a powerful web scraping framework, to extract data from Amazon's search pages.

## Project Structure

- **Spider: `Amazon_Phone_Search`**
  - Scrapy spider responsible for crawling Amazon search results for phone products and extracting relevant data.
  
- **Item Models:**
  - `AmazonItem`: Defines the structure of the scraped data, including product name, color variants, price, stars, rating count, feature bullets, images, and variant data.
  
- **Pipelines:**
  - `AmazonscraperPipeline`: Processes the scraped items, cleans the data, and prepares it for storage.
  
- **Settings:**
  - Various Scrapy settings configured to control the behavior of the crawling and scraping process.

## Usage

1. Install the necessary Python libraries and dependencies, including Scrapy and required middleware.

2. Install the ScrapeOps Proxy middleware:
   ```bash
   pip install scrapeops-scrapy-proxy-sdk 

3. Install the ScrapeOps Monitor SDK:
  ```bash
  pip install scrapeops-scrapy
  ```
4. Also ensure the scrapeops monitor are installed:
 ```bash
pip install scrapy scrapeops-scrapy
```

