# Import Important Libraries.
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
import re
from nltk.tokenize import word_tokenize,sent_tokenize
nltk.download('punkt')


# Load input file.
df=pd.read_excel('input.xlsx')

# Load stopwords.
stopwords_folder='StopWords'
stopwords_files=os.listdir(stopwords_folder)

stopwords= set()
for file in stopwords_files:
    with open(os.path.join(stopwords_folder, file), 'r',encoding="ISO-8859-1") as f:
        stopwords.update(f.read().split())

# Load Positive and negative words.
def load_dictionary(file_path):
    with open(file_path, "r", encoding="ISO-8859-1") as f:  # Change encoding
        return set(f.read().split())
positive_words=load_dictionary("MasterDictionary/positive-words.txt")
negative_words=load_dictionary("MasterDictionary/negative-words.txt")


# Function to extract text from a URL.
def extract_text(url):
    try:
        response=requests.get(url,timeout=10)
        response.raise_for_status()
        soup=BeautifulSoup(response.text,'html.parser')
        
        # Extract title and article content.
        title= soup.find("h1").get_text(strip=True) if soup.find("h1") else "No Title"
        paragraphs=soup.find_all("p")
        content=" ".join([p.get_text(strip=True) for p in paragraphs])
        
        return title + "\n\n" + content
    except Exception as e:
        print(f"Error extracting {url}: {e}")
        return None
    
# Function to preprocess text from a URL.
def preprocess_text(text):
    # Tokenize.
    words=word_tokenize(text.lower())
    words=[w for w in words if w.isalnum() and w not in stopwords]
    return words

# Function to count syllabels in a word.
def count_syllables(word):
    vowels='aeiou'
    count= sum(1 for char in word if char in vowels)
    if word.endswith(('es','ed')):
        count-=1
    return max(count,1)

# function to analyze text and compute scores.
def analyze_text(text):
    # Tokenize and count words.
    words=preprocess_text(text)
    sentence=sent_tokenize(text)
    
    pos_score= sum(1 for w in words if w in positive_words)
    neg_score= sum(-1 for w in words if w in negative_words) * -1
    polarity_score= (pos_score - neg_score )/ ((pos_score + neg_score) + 0.000001)
    subjectivity_score= (pos_score + neg_score)/(len(words) + 0.000001)
    
    avg_sentence_length= len(words) / len(sentence)
    complex_word=[w for w in words if count_syllables(w) > 2]
    percentage_complex_words= len(complex_word) / len(words)
    fog_index= 0.4*(avg_sentence_length + percentage_complex_words)
    
    avg_words_per_sentence= len(words) / len(sentence)
    complex_word_count=  len(complex_word)
    word_count= len(words)
    syllables_per_word = sum(count_syllables(w) for w in words) / len(words) if words else 0
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.IGNORECASE))
    avg_word_length = sum(len(w) for w in words) / len(words) if words else 0
    
    return {
        "POSITIVE SCORE": pos_score,
        "NEGATIVE SCORE": neg_score,
        "POLARITY SCORE": polarity_score,
        "SUBJECTIVITY SCORE": subjectivity_score,
        "AVG SENTENCE LENGTH": avg_sentence_length,
        "PERCENTAGE OF COMPLEX WORDS": percentage_complex_words,
        "FOG INDEX": fog_index,
        "AVG NUMBER OF WORDS PER SENTENCE": avg_words_per_sentence,
        "COMPLEX WORD COUNT": complex_word_count,
        "WORD COUNT": word_count,
        "SYLLABLE PER WORD": syllables_per_word,
        "PERSONAL PRONOUNS": personal_pronouns,
        "AVG WORD LENGTH": avg_word_length
    }


# Process all urls and save result.
def process_all_urls():
    output_data=[]
    
    for index,row in df.iterrows():
        url_id=row["URL_ID"]
        url=row["URL"]
        
        print(f"Processing URL_ID: {url_id}")
        
        text=extract_text(url)
        if text:
            with open(f'{url_id}.txt','w',encoding='utf-8')as f:
                f.write(text)
            
            analysis=analyze_text(text)
            output_data.append({"URL_ID":url_id,
                                "URL":url,
                                **analysis
            })
    
    # Save result to Excel File.
    output_df=pd.DataFrame(output_data)
    output_df.to_excel("output.xlsx",index=False)
    
    print("Processing complete. Result saved to output.xlsx")

# Call the function to process all urls.

if __name__ == "__main__":
    process_all_urls()

