from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os

def get_web_text(url):
    driver = webdriver.Chrome()
    driver.get(url)

    html_text = driver.page_source
    driver.quit()

    return html_text

def get_rows(text):
    soup = BeautifulSoup(text, 'lxml')
    table = soup.find('table', tabindex='0').tbody
    rows = table.find_all('tr')
    return rows

def parse_data(rows):
    entries = []

    for row in rows:

        data_list = row.find_all('td')
        company = data_list[0].text
        
        location = data_list[2].text
        if "locations" in location:
            location = (location.split('locations')[1]).split(',')
        
        entry = {
            'company': entries[-1]['company'] if company == '↳' else company,
            'role': data_list[1].text,
            'locations': location,
            'date_posted':data_list[4].text,
        }
        entries.append(entry)
    
    return entries

def save_data(data_list, path):
    df = pd.DataFrame(data_list)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)

def main():
    url = 'https://github.com/SimplifyJobs/Summer2026-Internships/blob/dev/archived/README-2024.md'
    text = get_web_text(url)
    rows = get_rows(text)
    data_list = parse_data(rows)

    output_path = 'test.csv'
    save_data(data_list, output_path)

if __name__=="__main__":
    main()
