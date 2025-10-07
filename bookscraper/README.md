# Book Categories Scraper

A simple [Scrapy](https://scrapy.org/) project that extracts **book category information** from [Books to Scrape](https://books.toscrape.com), a sandbox website commonly used for practicing web scraping.

This scraper collects:
- Each book **category name**
- The **total number of books** in that category

and saves the results into a JSON file (`categorydata.json`).

---

## Features

- Crawls all book categories automatically  
- Extracts category names and book counts  
- Saves structured data to a JSON file  

---

## Example Output

```json
[
  {
    "category": "Travel",
    "qty_books": "11"
  },
]
```

---

## Technologies Used

- **Python**
- **Scrapy**

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/book-categories-scraper.git
   cd book-categories-scraper
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Linux/Mac
   venv\Scripts\activate      # on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the spider using Scrapy’s command-line tool:

```bash
scrapy crawl bookspider
```

This will start scraping and generate a file named **`categorydata.json`** in your project’s root directory.

You can also export in a different format (e.g. CSV):

```bash
scrapy crawl bookspider -O categorydata.csv
```

---

## Example Command Flow

```bash
git clone https://github.com/yourusername/book-categories-scraper.git
cd book-categories-scraper
pip install -r requirements.txt
scrapy crawl bookspider
```

Result → `categorydata.json` created in your project folder

---

## Author

**Jean S1lva**  
[GitHub](https://github.com/JeanS1lva) • [Portfolio](https://JeanS1lva.github.io)

---

 *Made with Scrapy for web scraping practice and portfolio demonstration.*
