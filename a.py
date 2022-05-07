import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
"""
https://andrew-muller.medium.com/getting-text-from-epub-files-in-python-fbfe5df5c2da
[2022.05.07]
"""

def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    return text

book = epub.read_epub(f'name.epub')
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
with open(f'name.txt', 'w') as f:
    for i in range(len(items)):
        text_l = chapter_to_str(items[i])
        for j in text_l:
            f.write(f'{j}\n')
