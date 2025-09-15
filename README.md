# Web Scraper Test Task

## Project Description

This repository contains a set of Python scripts for a test assignment. The scripts demonstrate working with APIs, HTML parsing via XPath, regular expressions, and SQL queries for processing job vacancies and addresses.

## Project Structure

```
web-scraper-test-task/
├── README.md                # Project description and instructions
├── requirements.txt         # Python dependencies
├── task1_api/               # API job scraper
│   ├── api_scraper.py       # Script for collecting jobs via API
│   └── task1_results.json   # Saved jobs in JSON format
├── task2_xpath/             # XPath address scraper
│   ├── xpath_scraper.py     # Script for collecting addresses via XPath
│   └── task2_results.json   # Saved addresses in JSON format
├── task3_sql/               # SQL queries and database
│   ├── query.sql            # SQL query for job selection
│   └── task3_db.sqlite3     # SQLite database with sample data
│   └── task3_results.csv    # SQL query results
├── task4_regex/             # Regex scraper
│   ├── regex_scraper.py     # Script for extracting URLs, emails, bots, parentheses
│   ├── task4_results.json   # Regex scraper results
│   └── text.txt             # Input text for parsing
```

## Installation

Install Python 3.8+ and required libraries:

```
pip install -r requirements.txt
```

## How to Run

### 1. API Scraper (task1_api)

Collects jobs via API and saves them to task1_results.json.

```
python task1_api/api_scraper.py
```

### 2. XPath Scraper (task2_xpath)

Collects job addresses from the web page via XPath and saves them to task2_results.json.

```
python task2_xpath/xpath_scraper.py
```

### 3. SQL Query (task3_sql)

Executes a query to select jobs in Kyiv and Lviv.

```
sqlite3 task3_sql/task3_db.sqlite3 < task3_sql/query.sql > task3_sql/task3_results.csv
```

### 4. Regex Scraper (task4_regex)

Extracts URLs, emails, Telegram bots, and text in parentheses from text.txt. Results are saved to task4_results.json.

```
python task4_regex/regex_scraper.py
```

## Output Formats

- task1_results.json — array of jobs from API.
- task2_results.json — array of job addresses.
- task3_results.csv — table with url and description for jobs in Kyiv and Lviv.
- task4_results.json — dictionary with keys: urls, emails, bots, parentheses.

## Requirements

- Python 3.8+
- SQLite3
- Internet connection for API and web parsing

---

### Task 1 — API Scraper Notes

**Requirement:**
> The assignment specified that job data should be extracted from the key `results` in the API response.

**Reality:**
> The actual API returns job data under the key `jobs`, not `results`.
> Therefore, in the implementation, the code uses `data.get("jobs", [])` to collect job entries.
> This difference was handled in the code to ensure correct data extraction.

---

### Task 2 — XPath Scraper Notes

**Requirement (p.2):**
> Extract all tags containing email addresses.

**Reality:**
> There are no email addresses present on the main job listing page (with 32 vacancies) or on any individual job detail page at [https://marketdino.pl/kariera/wyniki?page=1&page_size=32](https://marketdino.pl/kariera/wyniki?page=1&page_size=32).
> All inspected tags and blocks on both the general and detail pages do not contain any email addresses.
> Therefore, the email extraction logic was not implemented, as there is no data to extract for this requirement.

---
