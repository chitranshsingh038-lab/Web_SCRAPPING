# Web_SCRAPPING
This Program is used to scrap a web page(web-scraping.dev).
# Web Scraping Script for Product Data

This project is a simple Python-based web scraper that collects product information from the demo website **web-scraping.dev**. It extracts product names, prices, descriptions, and image URLs, then stores the data in an Excel file.

## Features
* Scrapes product **name**
* Extracts **price**
* Extracts **short description**
* Builds full **image URLs**
* Stores scraped data in a clean **Excel (.xlsx)** file

## Requirements
Make sure you have the following Python libraries installed:
* Request module.
* BeautifulSoup.
* Pandas.

## How It Works
The script performs the following steps:

1. Sends a `GET` request to the product page.
2. Parses the HTML using **BeautifulSoup**.
3. Locates all product cards.
4. Extracts relevant product details.
5. Builds a pandas DataFrame.
6. Exports the data to `scraped_file.xlsx`.

## Output
The script generates:

```
scraped_file.xlsx
```

This file contains columns:
* name
* price
* image_url
* description

## Notes
* The scraper is for **educational purposes only**.
* The target site is a safe demo site built for web scraping practice.

## Contributing
Pull requests are welcome! Feel free to open an issue if you have ideas for improvements.

## License
This project is open-source and available under the MIT License.

