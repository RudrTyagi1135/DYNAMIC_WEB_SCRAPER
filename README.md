# 🤖 Dynamic Web Scraper (Selenium Automation System)

A **browser automation-based web scraping system** built using **Python and Selenium**, designed to extract data from **modern JavaScript-heavy websites**.

This project demonstrates how to handle real-world scraping challenges such as **infinite scrolling**, **load-more pagination**, and **search-driven navigation workflows**.

---

## 🚀 Features

- 🔄 **Infinite scroll scraping automation**
- 🔘 **Load-more button handling**
- 🔍 **Search-based navigation workflows**
- 🌐 **Dynamic content extraction (JS-rendered pages)**
- ⚡ **Full HTML capture for downstream processing**
- 🧩 **Multi-pattern scraping system design**

---

## 🧠 What This Project Demonstrates

This project highlights the following **automation and data engineering skills**:

- **Browser automation using Selenium WebDriver**
- **Handling dynamic web content (JavaScript-rendered pages)**
- **Simulating real user interactions**
- **DOM manipulation using XPath**
- **Designing reusable scraping patterns**
- **Data extraction pipeline foundations**

---

## 📂 Project Structure

```
DYNAMIC_WEB_SCRAPER/
│
├── ajio_infinite_scroll.py        # Infinite scroll scraper
├── smartprix_load_more.py         # Load-more pagination scraper
├── google_search_navigation.py    # Search-based navigation automation
│
├── ajio.html                      # Extracted HTML output
├── smartprix.html                 # Extracted HTML output
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Architecture Overview

The project follows a **browser automation scraping pipeline**.

```
Target Website (Dynamic / JS-based)
        │
        ▼
Selenium WebDriver (ChromeDriver)
        │
        ▼
User Interaction Simulation
(scroll, click, search)
        │
        ▼
Rendered DOM Extraction
        │
        ▼
HTML Storage (Local Files)
        │
        ▼
Downstream Processing
(BeautifulSoup / Pandas)
```

### Design Principles

- **Simulation of real user behavior**
- **Pattern-based scraping (modular scripts)**
- **Separation of extraction and processing**
- **Focus on dynamic website handling**

---

## 🔄 Scraping Patterns Implemented

### 1️⃣ Infinite Scroll

- Continuously scrolls until no new content loads  
- Handles lazy-loaded elements  

📄 File: `ajio_infinite_scroll.py`

---

### 2️⃣ Load More Pagination

- Clicks "Load More" button repeatedly  
- Stops when no more data is available  

📄 File: `smartprix_load_more.py`

---

### 3️⃣ Search-Based Navigation

- Automates multi-step browsing flow:

```
Google → Search Query → Click Result → Navigate Target Page
```

📄 File: `google_search_navigation.py`

---

## 🛠 Installation

### Clone repository

```bash
git clone https://github.com/your-username/dynamic-web-scraper.git
cd dynamic-web-scraper
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run any script independently:

```bash
python ajio_infinite_scroll.py
python smartprix_load_more.py
python google_search_navigation.py
```

---

## ⚙️ Configuration

Update ChromeDriver path inside scripts:

```python
Service("path/to/chromedriver")
```

Ensure ChromeDriver version matches your browser.

---

## 📂 Output

Extracted HTML files are stored locally:

- `ajio.html`
- `smartprix.html`

These can be further processed using:

- **BeautifulSoup**
- **Pandas**
- **Custom data pipelines**

---

## ⚠️ Limitations

- Hardcoded XPath selectors (can break on UI changes)
- No proxy rotation or IP management
- No CAPTCHA handling
- Not optimized for large-scale scraping
- No structured data output (HTML only)

---

## 📈 Potential Improvements

Future enhancements could include:

- Convert into **modular scraping framework (`src/` structure)**
- Add **headless + stealth scraping (undetected-chromedriver)**
- Implement **retry logic and error handling**
- Add **proxy rotation and user-agent spoofing**
- Export structured data (**JSON / CSV / database**)  
- Integrate with **data pipelines (AWS S3, Lambda, ETL systems)**

---

## 🧰 Tech Stack

| Technology | Purpose |
|-----------|--------|
| Python | Programming language |
| Selenium | Browser automation |
| ChromeDriver | WebDriver engine |
| XPath | DOM interaction |
| HTML | Extracted data format |

---

## 🎯 Learning Outcomes

This project helped build understanding of:

- **Dynamic web scraping techniques**
- **Browser automation workflows**
- **Handling asynchronous page loads**
- **DOM navigation and interaction**
- **Building foundations for data pipelines**

---

## 👤 Author

**Rudra Tyagi**

B.Tech Final Year Student  
**ML Systems / MLOps / AI Infrastructure Engineer**