#!/usr/bin/env python3
"""
EPUB Word Frequency Analyzer
Extracts all words from an EPUB file and analyzes their frequency.
Outputs results to both TXT and CSV formats.

Made for analyzing vocabulary in ebooks.
"""

import re
import csv
from collections import Counter
from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
import argparse
import os

# Common CET-4 words (sample list - you can expand this)
CET4_WORDS = {
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
    'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their',
    'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him',
    'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only',
    'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want',
    'because', 'any', 'these', 'give', 'day', 'most', 'us', 'is', 'water', 'long', 'find', 'here', 'thing', 'great', 'man', 'world', 'life',
    'still', 'public', 'human', 'read', 'keep', 'write', 'follow', 'around', 'change', 'play', 'spell', 'found', 'study', 'learn', 'should',
    'american', 'small', 'another', 'never', 'system', 'too', 'any', 'help', 'through', 'much', 'before', 'line', 'right', 'old', 'try', 'same',
    'tell', 'boy', 'follow', 'came', 'want', 'show', 'also', 'around', 'farm', 'three', 'small', 'set', 'put', 'end', 'why', 'again', 'turn',
    'ask', 'went', 'men', 'land', 'here', 'must', 'big', 'high', 'such', 'follow', 'act', 'why', 'ask', 'men', 'change', 'went', 'light',
    'kind', 'off', 'need', 'house', 'picture', 'try', 'us', 'again', 'animal', 'point', 'mother', 'world', 'near', 'build', 'self', 'earth'
}

# Common CET-6 words (sample list - you can expand this)
CET6_WORDS = {
    'abandon', 'ability', 'abroad', 'absence', 'absolute', 'absorb', 'abstract', 'abuse', 'academic', 'accelerate', 'accent', 'accept',
    'access', 'accident', 'accompany', 'accomplish', 'accord', 'account', 'accurate', 'accuse', 'achieve', 'acid', 'acknowledge',
    'acquire', 'across', 'action', 'active', 'activity', 'actor', 'actual', 'acute', 'adapt', 'add', 'addition', 'adequate', 'adjust',
    'administration', 'admire', 'admit', 'adopt', 'adult', 'advance', 'advantage', 'adventure', 'adverse', 'advertise', 'advice',
    'advocate', 'affair', 'affect', 'afford', 'afraid', 'african', 'agency', 'agent', 'aggressive', 'agree', 'agreement', 'agriculture',
    'aid', 'aim', 'aircraft', 'airline', 'airport', 'alarm', 'album', 'alcohol', 'alert', 'alien', 'alike', 'alive', 'alliance',
    'allow', 'almost', 'alone', 'along', 'alphabet', 'alter', 'alternative', 'although', 'altitude', 'altogether', 'always',
    'amateur', 'amaze', 'ambition', 'ambulance', 'american', 'among', 'amount', 'ample', 'amuse', 'analyse', 'analysis', 'analyze',
    'ancestor', 'anchor', 'ancient', 'anger', 'angle', 'angry', 'animal', 'ankle', 'anniversary', 'announce', 'annoy', 'annual',
    'another', 'answer', 'anticipate', 'anxiety', 'anxious', 'apart', 'apartment', 'apologize', 'apparatus', 'apparent', 'appeal',
    'appear', 'appetite', 'apple', 'appliance', 'applicable', 'application', 'apply', 'appoint', 'appreciate', 'approach',
    'appropriate', 'approve', 'approximate', 'april', 'arbitrary', 'arch', 'architect', 'area', 'argue', 'argument', 'arise',
    'arithmetic', 'army', 'around', 'arouse', 'arrange', 'array', 'arrest', 'arrival', 'arrive', 'arrow', 'article', 'artificial',
    'artist', 'artistic', 'ascend', 'ashamed', 'asian', 'aside', 'assembly', 'assert', 'assess', 'asset', 'assign', 'assist',
    'assistant', 'associate', 'association', 'assume', 'assure', 'astonish', 'astronaut', 'athlete', 'atlantic', 'atmosphere',
    'atom', 'atomic', 'attach', 'attack', 'attain', 'attempt', 'attend', 'attention', 'attitude', 'attract', 'attractive',
    'attribute', 'audience', 'august', 'aunt', 'author', 'authority', 'auto', 'automatic', 'automobile', 'autumn', 'available',
    'average', 'avoid', 'awake', 'award', 'aware', 'away', 'awful', 'awkward', 'axis'
}

def extract_text_from_epub(epub_path):
    """Extract all text content from an EPUB file."""
    try:
        book = epub.read_epub(epub_path)
        text_content = []
        
        # Get all document items (XHTML pages)
        for item in book.items:
            if item.get_type() == ITEM_DOCUMENT:
                # Parse HTML content
                soup = BeautifulSoup(item.get_content(), 'html.parser')
                # Extract text, removing HTML tags
                text = soup.get_text()
                text_content.append(text)
        
        return '\n'.join(text_content)
    except Exception as e:
        print(f"Error reading EPUB file: {e}")
        return ""

def clean_and_extract_words(text):
    """Clean text and extract individual words."""
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters and keep only letters, numbers, and apostrophes
    # This preserves contractions like "don't", "won't", etc.
    text = re.sub(r"[^a-zA-Z0-9'\s]", " ", text)
    
    # Split into words
    words = text.split()
    
    # Further clean each word (remove leading/trailing apostrophes)
    cleaned_words = []
    for word in words:
        word = word.strip("'")
        if word and len(word) > 1:  # Only keep words with more than 1 character
            cleaned_words.append(word)
    
    return cleaned_words

def categorize_word(word):
    """Categorize a word based on CET levels."""
    word_lower = word.lower()
    if word_lower in CET4_WORDS:
        return "CET-4"
    elif word_lower in CET6_WORDS:
        return "CET-6"
    else:
        return "Other"

def analyze_epub_words(epub_path, output_prefix="word_analysis"):
    """Analyze words in an EPUB file and generate reports."""
    print(f"Analyzing EPUB file: {epub_path}")
    
    # Extract text from EPUB
    text = extract_text_from_epub(epub_path)
    if not text:
        print("No text extracted from EPUB file.")
        return
    
    print(f"Extracted {len(text)} characters of text.")
    
    # Extract and clean words
    words = clean_and_extract_words(text)
    print(f"Found {len(words)} total words.")
    
    # Count word frequencies
    word_counts = Counter(words)
    print(f"Found {len(word_counts)} unique words.")
    
    # Categorize words
    word_analysis = []
    for word, count in word_counts.most_common():
        category = categorize_word(word)
        word_analysis.append({
            'word': word,
            'count': count,
            'category': category
        })
    
    # Generate TXT report
    txt_filename = f"{output_prefix}.txt"
    with open(txt_filename, 'w', encoding='utf-8') as f:
        f.write(f"Word Frequency Analysis Report\n")
        f.write(f"{'='*50}\n")
        f.write(f"EPUB File: {epub_path}\n")
        f.write(f"Total words: {len(words):,}\n")
        f.write(f"Unique words: {len(word_counts):,}\n\n")
        
        # Summary by category
        category_counts = Counter(item['category'] for item in word_analysis)
        f.write("Category Summary:\n")
        f.write("-" * 20 + "\n")
        for category, count in category_counts.most_common():
            f.write(f"{category}: {count:,} unique words\n")
        f.write("\n")
        
        # Top words overall
        f.write("Top 50 Most Frequent Words:\n")
        f.write("-" * 30 + "\n")
        f.write(f"{'Rank':<6} {'Word':<20} {'Count':<10} {'Category':<10}\n")
        f.write("-" * 50 + "\n")
        
        for i, item in enumerate(word_analysis[:50], 1):
            f.write(f"{i:<6} {item['word']:<20} {item['count']:<10} {item['category']:<10}\n")
        
        f.write("\n" + "="*50 + "\n")
        f.write("Complete Word List (Alphabetical):\n")
        f.write("="*50 + "\n")
        
        # Sort alphabetically for complete list
        sorted_words = sorted(word_analysis, key=lambda x: x['word'])
        for item in sorted_words:
            f.write(f"{item['word']:<25} {item['count']:<8} times  [{item['category']}]\n")
    
    # Generate CSV report
    csv_filename = f"{output_prefix}.csv"
    with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['word', 'count', 'category', 'rank_by_frequency']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for i, item in enumerate(word_analysis, 1):
            writer.writerow({
                'word': item['word'],
                'count': item['count'],
                'category': item['category'],
                'rank_by_frequency': i
            })
    
    print(f"\nAnalysis complete!")
    print(f"Reports generated:")
    print(f"  - {txt_filename} (detailed text report)")
    print(f"  - {csv_filename} (CSV data for further analysis)")
    
    # Print summary statistics
    print(f"\nSummary Statistics:")
    print(f"  Total words: {len(words):,}")
    print(f"  Unique words: {len(word_counts):,}")
    
    category_counts = Counter(item['category'] for item in word_analysis)
    print(f"  CET-4 words: {category_counts.get('CET-4', 0):,}")
    print(f"  CET-6 words: {category_counts.get('CET-6', 0):,}")
    print(f"  Other words: {category_counts.get('Other', 0):,}")
    
    # Show top 10 words as example
    print(f"\nTop 10 most frequent words:")
    for i, item in enumerate(word_analysis[:10], 1):
        print(f"  {i:2}. {item['word']:<15} - {item['count']:,} times [{item['category']}]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze word frequency in EPUB files")
    parser.add_argument("epub_file", help="Path to the EPUB file to analyze")
    parser.add_argument("-o", "--output", default="word_analysis", 
                       help="Output filename prefix (default: word_analysis)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.epub_file):
        print(f"Error: EPUB file '{args.epub_file}' not found.")
        exit(1)
    
    analyze_epub_words(args.epub_file, args.output)