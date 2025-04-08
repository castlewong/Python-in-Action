# For many way large epubs, this func can split it into two parts
# Made by @wilburwong hulkbuster0114@gmail.com
# 2025-04-08 11:28:01

from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup
import math

def split_epub_latter_half(original_epub_path, output_epub_path):
    # Load the original book
    book = epub.read_epub(original_epub_path)

    # Extract all "document" items (usually XHTML pages)
    doc_items = [item for item in book.items if item.get_type() == ITEM_DOCUMENT]

    # Get the latter half of the documents
    split_index = len(doc_items) // 2
    latter_docs = doc_items[split_index:]
    # First half
    # latter_docs = doc_items[:split_index]

    # Create a new EPUB
    new_book = epub.EpubBook()
    new_book.set_identifier('latter-half-id')
    new_book.set_title('Latter Half of Book BATTLE HEAVENS')
    new_book.set_language('en')

    # (Optional) set author or metadata
    new_book.add_author('Unknown')

    # Add each document to the new book
    new_spine = ['nav']
    new_toc = []

    for i, item in enumerate(latter_docs):
        new_book.add_item(item)
        new_spine.append(item)
        new_toc.append(item)

    # Add required navigation files
    new_book.add_item(epub.EpubNcx())
    new_book.add_item(epub.EpubNav())

    # Set spine and TOC
    new_book.spine = new_spine
    new_book.toc = tuple(new_toc)

    # Write the new book
    epub.write_epub(output_epub_path, new_book)
    print(f"Saved latter half of the book to: {output_epub_path}")


# Example usage
split_epub_latter_half('/Users/wilburwong/Downloads/ebook-web/The-Great-Ruler.epub',
                       '/Users/wilburwong/Downloads/ebook-web/The-Great-Ruler-HALF1.epub')
