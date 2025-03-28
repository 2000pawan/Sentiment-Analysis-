# **Sentiment Analysis Project.

## **1. Approach to the Solution**

The project performs **sentiment analysis** on text extracted from URLs using **Natural Language Processing (NLP)** techniques. Below is the step-by-step approach:

### **🔹 Step 1: Load Necessary Data**

- The input file `input.xlsx` contains **URLs** with their corresponding **URL\_IDs**.
- Stopwords are loaded from the `StopWords` folder to filter out unnecessary words.
- A **positive** and **negative** words dictionary is loaded from `MasterDictionary/`.

### **🔹 Step 2: Extract Text from URLs**

- The script fetches the webpage content using `requests` and **BeautifulSoup**.
- It extracts the **title** and **article text** from `<h1>` and `<p>` tags.
- The extracted text is stored in the `url_text/` folder as a `.txt` file for each URL.

### **🔹 Step 3: Preprocessing the Extracted Text**

- Tokenization is performed using `nltk.word_tokenize()`.
- Stopwords and non-alphanumeric words are removed.

### **🔹 Step 4: Sentiment Analysis & Text Complexity Metrics**

For each extracted text, the script computes:
✔ **Positive Score** (count of positive words)\
✔ **Negative Score** (count of negative words)\
✔ **Polarity Score** (positive vs. negative balance)\
✔ **Subjectivity Score** (extent of opinion-based content)\
✔ **Complexity Measures**:

- **Fog Index** (readability metric)
- **Syllables per word**
- **Complex word count** (words with >2 syllables)
- **Personal Pronoun Count** (e.g., "I", "we", "my")\
  ✔ **General Statistics**:
- **Average sentence length**
- **Average word length**

### **🔹 Step 5: Save Output to Excel**

- The computed scores and metrics are saved in `output.xlsx`.
- Each row contains a **URL\_ID, URL, and sentiment analysis results**.

---

## **2. How to Run the Script**

### **💻 Prerequisites**

Ensure you have **Python 3.x** installed on your system.

### **📌 Steps to Run the Script**

1️⃣ **Install Dependencies**\
Run the following command in your terminal or command prompt:

```sh
pip install pandas requests beautifulsoup4 nltk openpyxl
```

2️⃣ **Prepare the Input File**

- Place `input.xlsx` in the same directory as the script.
- Ensure it has **two columns: ****`URL_ID`**** and ****`URL`**.

3️⃣ **Run the Script**\
Navigate to the project folder and execute:

```sh
python Sentiment_analysis.py
```

4️⃣ **View the Output**

- Extracted webpage text is saved in `url_text/`.
- The final **sentiment analysis report** is saved as `output.xlsx`.

---

## **3. Required Dependencies**

Ensure you have the following Python libraries installed:

| **Library**      | **Purpose**                 | **Installation Command**     |
| ---------------- | --------------------------- | ---------------------------- |
| `pandas`         | Handling Excel data         | `pip install pandas`         |
| `requests`       | Fetching webpage content    | `pip install requests`       |
| `beautifulsoup4` | Parsing HTML                | `pip install beautifulsoup4` |
| `nltk`           | Natural Language Processing | `pip install nltk`           |
| `openpyxl`       | Handling Excel files        | `pip install openpyxl`       |

Additionally, download the **NLTK tokenizer data** by running:

```python
import nltk
nltk.download('punkt')
```

---

## **📌 Notes**

✅ If an error occurs due to a missing directory (`url_text/`), manually create it or ensure the script includes:

```python
os.makedirs("url_text", exist_ok=True)
```

✅ Ensure your input Excel file (`input.xlsx`) is correctly formatted.\
✅ If you face encoding issues, use `ISO-8859-1` while reading text files.

---
PAWAN YADAV
