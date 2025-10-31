from pypdf import PdfReader
from collections import Counter
import re


# reader = PdfReader("sample.pdf")
# page = reader.pages[0]
# print(page.extract_text())

def get_number_of_pages(pdf_path: str) -> int:
    pdf_reader = PdfReader(pdf_path)
    no_of_pages: int = pdf_reader.get_num_pages()
    return no_of_pages

def extract_text_from_pdf(pdf_path: str):
    pdf_reader = PdfReader(pdf_path)
    no_of_pages = pdf_reader.get_num_pages()
    full_text: str = ""

    for num in range(no_of_pages):
        extracted_text = pdf_reader.pages[num]
        full_text += extracted_text.extract_text() + "\n"
    return full_text

def count_words_in_text(texts: str):
    list_of_words: list[str] = re.findall(r'\b\w+\b', texts.lower())
    word_count = Counter(list_of_words)
    # print(list_of_words)
    # print(word_count)
    return word_count

def main():
    no_of_pages = get_number_of_pages("sample.pdf")
    print(f'Number of pages: {no_of_pages}')
    full_text_in_pdf: str = extract_text_from_pdf("sample.pdf")
    # print(full_text_in_pdf)

    word_count: Counter = count_words_in_text(full_text_in_pdf)
    print("Most common words:")
    for word, count in word_count.most_common(5):
        print(f'{word:10}: {count}')

if __name__ == '__main__':
    main()



