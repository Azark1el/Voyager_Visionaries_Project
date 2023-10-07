import fitz
import requests
import tabula
import certifi
import ssl
import io
import os
import re
import numpy as np
from bs4 import BeautifulSoup
from datetime import datetime
from io import BytesIO

def date_extractor(pdf_url, date_pattern):
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()

        pdf_document = fitz.open(stream=BytesIO(response.content))

        match_dates = []

        page = pdf_document.load_page(0)

        page_text = page.get_text()

        dates_found = re.findall(date_pattern, page_text)

        if dates_found:
            match_dates = dates_found

        pdf_document.close()

        return match_dates
    
    except requests.exceptions.RequestException as e:
        return []
    except Exception as e:
        return []

def page_extractor(pdf_url, searchword):
    try:
        response = requests.get(pdf_url, verify=False)
        response.raise_for_status()

        pdf_document = fitz.open(stream=BytesIO(response.content))

        pages = []

        for pagenum in range(pdf_document.page_count):
            page = pdf_document.load_page(pagenum)

            if searchword in page.get_text():
                pages.append(pagenum + 1)

        pdf_document.close()

        return pages
    
    except requests.exceptions.RequestException as e:
        return []

def table_extractor(pdf_path, target_pages):
    try:
        numbers = []

        for page in target_pages:
            tables = tabula.read_pdf(pdf_path, pages = page, multiple_tables=True)

            if len(tables) > 0:
                table = tables[0]
            else:
                continue
        
            for row_index, row in table.iterrows():
                for col_index, cell_value in enumerate(row):
                    try:
                        data = cell_value.split()

                        for substring in data:
                            try:
                                number = float(substring)

                                if not np.isnan(number):
                                    numbers.append(number)
                            except ValueError:
                                pass
                    except AttributeError:
                        pass
            
        return numbers
        
    except Exception as e:
        return []

url = 'https://sdup.esoc.esa.int/discosweb/statistics/'

datepattern = r'\d{1,2}(?:st|nd|rd|th)?\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}'

prefix = 'https://www.sdo.esoc.esa.int/publications/Space_Environment_Report'

word_list = ['Table 3.1:','Table 3.3:','Table 3.5:']

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
pdf_links = []

for link in links:
    href = link.get('href')
    if href and href.startswith(prefix) and href.endswith('.pdf'):
        pdf_links.append(href)

pdf_links.append('https://www.sdo.esoc.esa.int/environment_report/Space_Environment_Report_latest.pdf')

for link in pdf_links:
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    dates = date_extractor(link, datepattern)

    date_obj = datetime.strptime(dates[0], '%d %B %Y')

    year = date_obj.year

    pages = []

    for word in word_list:
        page_with_word = page_extractor(link, word)
        pages.append(page_with_word)

    all_list = []
    local_pdf_path = 'space_environment_report.pdf'

    response = requests.get(link, verify=False)
    
    with open(local_pdf_path, 'wb') as pdf_file:
        pdf_file.write(response.content)  

    for page in pages:
        extracted_num = table_extractor(local_pdf_path, page)
        text_file_path = str(year) + word_list[pages.index(page)] + '.txt'

        rowdata = [extracted_num[i:i+10] for i in range(0, len(extracted_num), 10)]

        all_list.extend(rowdata)

        with open(text_file_path, 'w') as text_file:
            column_width = 12
            for list in all_list[:11]:
                for number in list:
                    column_num = "{:<{width}.2f}".format(number, width = column_width)
                    text_file.write(column_num)

                text_file.write('\n')

        rowdata.clear()
        all_list.clear()
    

    os.remove(local_pdf_path)