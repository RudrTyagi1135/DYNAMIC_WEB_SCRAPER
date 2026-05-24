# 🤖 Dynamic Web Scraper — Selenium Automation System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green?style=for-the-badge&logo=selenium)
![ChromeDriver](https://img.shields.io/badge/ChromeDriver-Browser_Control-success?style=for-the-badge)
![Web Scraping](https://img.shields.io/badge/Web-Scraping-orange?style=for-the-badge)
![Automation](https://img.shields.io/badge/Browser-Automation-red?style=for-the-badge)

</p>

---

# 📌 Project Overview

The **Dynamic Web Scraper** is a Selenium-based browser automation system designed to scrape data from modern JavaScript-rendered websites.

Unlike static HTML scraping, this project focuses on handling:

- infinite scrolling
- dynamic DOM rendering
- asynchronous page loading
- load-more pagination
- search-driven navigation workflows

The system demonstrates real-world scraping patterns commonly used in modern data engineering and automation workflows.

---

# 🎯 Project Objective

Modern websites increasingly rely on:
- JavaScript rendering
- lazy loading
- client-side DOM updates
- asynchronous APIs

Traditional scraping tools often fail on such platforms.

This project was built to demonstrate how browser automation systems can simulate real user behavior to extract dynamically generated content.

---

# 🧠 What This Project Demonstrates

This repository demonstrates practical understanding of:

- Selenium browser automation
- JavaScript-rendered website scraping
- dynamic DOM interaction
- infinite scroll automation
- XPath-based element handling
- scraping workflow engineering
- extraction pipeline foundations
- downstream HTML processing preparation

---

# ✨ Core Features

## 🔄 Infinite Scroll Automation

Automatically:
- scrolls continuously
- waits for lazy-loaded content
- detects end-of-page conditions

Implemented in:

```text
ajio_infinite_scroll.py
```

---

## 🔘 Load-More Pagination Handling

Automates:
- repeated button clicking
- content expansion
- dynamic pagination workflows

Implemented in:

```text
smartprix_load_more.py
```

---

## 🔍 Search-Based Navigation Automation

Simulates:
- Google search workflows
- result navigation
- target page interaction

Implemented in:

```text
google_search_navigation.py
```

---

## 🌐 JavaScript-Rendered Content Extraction

Handles:
- dynamically generated DOMs
- delayed rendering
- AJAX-driven page updates

---

## 📄 Full HTML Capture

Exports:
- rendered HTML pages
- dynamically loaded content

for downstream:
- BeautifulSoup processing
- Pandas transformation
- ETL workflows
- structured dataset generation

---

# 🏗️ System Architecture

```text
Target Website
(Dynamic / JavaScript-based)
            ↓
 Selenium WebDriver
            ↓
 User Interaction Simulation
(scroll / click / search)
            ↓
Rendered DOM Extraction
            ↓
Local HTML Storage
            ↓
Downstream Data Processing
```

---

# ⚙️ Architecture Breakdown

---

# 🌐 Browser Automation Layer

Built using:
- Selenium WebDriver
- ChromeDriver

Responsibilities:
- browser control
- page interaction
- event simulation
- DOM rendering

---

# 🖱️ User Interaction Simulation Layer

Simulates:
- scrolling
- button clicks
- search queries
- navigation events

This allows the scraper to behave similarly to a real human user.

---

# 📄 DOM Extraction Layer

Extracts:
- rendered HTML
- lazy-loaded elements
- dynamically inserted content

after JavaScript execution completes.

---

# 💾 Storage Layer

Stores:
- raw HTML snapshots

for:
- downstream parsing
- data engineering workflows
- dataset generation

---

# 📂 Project Structure

```text
DYNAMIC_WEB_SCRAPER/
│
├── ajio_infinite_scroll.py
├── smartprix_load_more.py
├── google_search_navigation.py
│
├── ajio.html
├── smartprix.html
│
├── requirements.txt
└── README.md
```

---

# 🔄 Scraping Patterns Implemented

---

# 1️⃣ Infinite Scroll Scraping

### Workflow

```text
Open Website
      ↓
Scroll Down
      ↓
Wait For New Content
      ↓
Detect Page Height Change
      ↓
Repeat Until End
```

### Key Challenges Solved

- lazy loading
- asynchronous content rendering
- dynamic page growth

### File

```text
ajio_infinite_scroll.py
```

---

# 2️⃣ Load-More Pagination Scraping

### Workflow

```text
Open Website
      ↓
Locate "Load More" Button
      ↓
Click Button
      ↓
Wait For New Content
      ↓
Repeat Until Button Disappears
```

### Key Challenges Solved

- dynamic pagination
- DOM mutation handling
- repeated content expansion

### File

```text
smartprix_load_more.py
```

---

# 3️⃣ Search-Driven Navigation Automation

### Workflow

```text
Google Search
      ↓
Search Query Submission
      ↓
Result Selection
      ↓
Target Website Navigation
      ↓
Data Extraction
```

### Key Challenges Solved

- multi-page workflows
- browser navigation automation
- search-driven scraping pipelines

### File

```text
google_search_navigation.py
```

---

# ⚙️ Installation

---

# 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/dynamic-web-scraper.git

cd dynamic-web-scraper
```

---

# 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running The Project

Run any scraper independently:

```bash
python ajio_infinite_scroll.py
```

```bash
python smartprix_load_more.py
```

```bash
python google_search_navigation.py
```

---

# ⚙️ ChromeDriver Configuration

Update the ChromeDriver path inside scripts:

```python
Service("path/to/chromedriver")
```

Ensure:
- ChromeDriver version matches Chrome browser version

---

# 📂 Output Files

Generated outputs include:

```text
ajio.html
smartprix.html
```

These contain:
- fully rendered HTML
- dynamically loaded content
- browser-rendered DOM snapshots

---

# 🔄 Downstream Processing Possibilities

The extracted HTML can later be processed using:

| Tool | Purpose |
|---|---|
| BeautifulSoup | HTML parsing |
| Pandas | Data transformation |
| Regex | Pattern extraction |
| ETL Pipelines | Structured data workflows |

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Selenium | Browser automation |
| ChromeDriver | Browser control |
| XPath | DOM interaction |
| HTML | Raw extracted content |

---

# 📊 Engineering Highlights

- Dynamic website scraping
- Infinite scroll automation
- Browser interaction simulation
- DOM extraction workflows
- Selenium automation engineering
- Modular scraping patterns
- Real-world scraping problem handling
- JavaScript-rendered page support

---

# ⚠️ Current Limitations

Current constraints include:

- hardcoded XPath selectors
- no proxy rotation
- no CAPTCHA bypass support
- HTML-only extraction
- limited retry/error handling
- not optimized for large-scale distributed scraping

---

# 🚀 Planned Future Improvements

Planned enhancements include:

- modular scraping framework (`src/`)
- headless browser support
- stealth scraping
- proxy rotation
- user-agent spoofing
- retry and resilience systems
- structured data export
- JSON / CSV pipeline generation
- distributed scraping architecture
- AWS-integrated ETL workflows

---

# ☁️ Potential Cloud Architecture

```text
Target Websites
        ↓
Selenium Workers
        ↓
Extraction Queue
        ↓
S3 HTML Storage
        ↓
ETL Processing Pipeline
        ↓
Structured Dataset
```

Possible future technologies:
- AWS Lambda
- AWS S3
- SQS
- ECS
- Airflow

---

# 🎯 Learning Outcomes

This project helped build understanding of:

- Selenium automation
- dynamic content scraping
- asynchronous page interaction
- DOM navigation
- infinite scroll workflows
- scraping architecture design
- browser automation engineering

---

# 📌 Strategic Engineering Value

This project demonstrates stronger engineering depth than basic BeautifulSoup scraping projects because it handles:

- JavaScript-rendered websites
- browser interaction automation
- dynamic page rendering
- real-world scraping workflows
- user simulation systems

---

# 📸 Recommended Screenshot Section

Add screenshots for stronger recruiter impact:

```markdown
![Infinite Scroll Automation](your-image-link)

![Rendered HTML Output](your-image-link)

![Browser Automation Workflow](your-image-link)
```

---

# 👨‍💻 Author

## Rudra Tyagi

### Focus Areas

- ML Systems
- MLOps
- AI Infrastructure
- Automation Engineering
- Data Engineering Foundations

---

# ⭐ Recruiter Notes

This repository demonstrates:

- browser automation engineering
- Selenium-based scraping systems
- handling dynamic web architectures
- extraction workflow design
- foundational data pipeline thinking

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
