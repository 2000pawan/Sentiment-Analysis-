---

# **Sentiment Analysis Project**

## **📌 Project Overview**
This project performs **sentiment analysis** on text extracted from URLs using **Natural Language Processing (NLP)** techniques. It analyzes the sentiment and readability of the extracted content and saves the results in an Excel file.

---

## **1. Approach to the Solution**

### **🔹 Step 1: Load Necessary Data**
- The input file `input.xlsx` contains **URLs** with their corresponding **URL_IDs**.
- Stopwords are loaded from the [`StopWords`](https://github.com/2000pawan/Sentiment-Analysis-/tree/main/StopWords) folder to filter out unnecessary words.
- A **positive** and **negative** words dictionary is loaded from [`MasterDictionary`](https://github.com/2000pawan/Sentiment-Analysis-/tree/main/MasterDictionary).

### **🔹 Step 2: Extract Text from URLs**
- The script fetches the webpage content using `requests` and **BeautifulSoup**.
- It extracts the **title** and **article text** from `<h1>` and `<p>` tags.
- The extracted text is stored in the `url_text/` folder as a `.txt` file for each URL.

### **🔹 Step 3: Preprocessing the Extracted Text**
- Tokenization is performed using `nltk.word_tokenize()`.
- Stopwords and non-alphanumeric words are removed.

### **🔹 Step 4: Sentiment Analysis & Text Complexity Metrics**
For each extracted text, the script computes:
✔ **Positive Score** (count of positive words)  
✔ **Negative Score** (count of negative words)  
✔ **Polarity Score** (positive vs. negative balance)  
✔ **Subjectivity Score** (extent of opinion-based content)  
✔ **Complexity Measures**:
   - **Fog Index** (readability metric)
   - **Syllables per word**
   - **Complex word count** (words with >2 syllables)
   - **Personal Pronoun Count** (e.g., "I", "we", "my")
✔ **General Statistics**:
   - **Average sentence length**
   - **Average word length**

### **🔹 Step 5: Save Output to Excel**
- The computed scores and metrics are saved in `output.xlsx`.
- Each row contains a **URL_ID, URL, and sentiment analysis results**.

---

## **2. How to Run the Script**

### **💻 Prerequisites**
Ensure you have **Python 3.x** installed on your system.

### **📌 Steps to Run the Script**

1️⃣ **Clone the Repository**  
Run the following command to download the project:
```sh
git clone https://github.com/2000pawan/Sentiment-Analysis-
```

2️⃣ **Install Dependencies**  
Run the following command in your terminal or command prompt:
```sh
pip install pandas requests beautifulsoup4 nltk openpyxl
```

3️⃣ **Prepare the Input File**  
- Place `input.xlsx` in the same directory as the script.
- Ensure it has **two columns: `URL_ID` and `URL`**.

4️⃣ **Download Master Dictionary & Stopwords**  
- **Master Dictionary:** [Download Here](https://github.com/2000pawan/Sentiment-Analysis-/tree/main/MasterDictionary)  
- **Stopwords:** [Download Here](https://github.com/2000pawan/Sentiment-Analysis-/tree/main/StopWords)  
Make sure these are placed in their respective folders.

5️⃣ **Run the Script**  
Navigate to the project folder and execute:
```sh
python Sentiment_analysis.py
```

6️⃣ **View the Output**  
- Extracted webpage text is saved in `url_text/`.
- The final **sentiment analysis report** is saved as `output.xlsx`.

---

## **3. Required Dependencies**
Ensure you have the following Python libraries installed:

| **Library**        | **Purpose**  | **Installation Command** |
|--------------------|-------------|-------------------------|
| `pandas`          | Handling Excel data  | `pip install pandas` |
| `requests`        | Fetching webpage content  | `pip install requests` |
| `beautifulsoup4`  | Parsing HTML  | `pip install beautifulsoup4` |
| `nltk`            | Natural Language Processing  | `pip install nltk` |
| `openpyxl`        | Handling Excel files  | `pip install openpyxl` |

Additionally, download the **NLTK tokenizer data** by running:
```python
import nltk
nltk.download('punkt')
```

---

## **4. Import Commands**
Ensure your script includes the following imports at the beginning:
```python
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('punkt')
```

---

## **📌 Notes**
✅ If an error occurs due to a missing directory (`url_text/`), manually create it or ensure the script includes:
```python
os.makedirs("url_text", exist_ok=True)
```
✅ Ensure your input Excel file (`input.xlsx`) is correctly formatted.
✅ If you face encoding issues, use `ISO-8859-1` while reading text files.

---
License

This project is open-source and available for modification and enhancement.

**🎯 Project Completed 🚀**
