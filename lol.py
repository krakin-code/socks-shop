import requests
from bs4 import BeautifulSoup
import re
import os
import time
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://bankrot.cdtrf.ru/public/undef/card/tradel.aspx"
DETAIL_URL = "https://bankrot.cdtrf.ru/public/undef/card/trade.aspx?id={}"  # Для детальной страницы
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
SAVE_PATH = "data/parsed"
os.makedirs(SAVE_PATH, exist_ok=True)


def get_viewstate_params(session):
    """ Получает скрытые параметры страницы """
    response = session.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    return {
        '__VIEWSTATE': soup.find('input', {'id': '__VIEWSTATE'})['value'],
        '__EVENTVALIDATION': soup.find('input', {'id': '__EVENTVALIDATION'})['value'],
        '__VIEWSTATEGENERATOR': soup.find('input', {'id': '__VIEWSTATEGENERATOR'})['value'],
    }


def get_page(session, page_number):
    """ Получает HTML-код страницы с торгами """
    params = get_viewstate_params(session)
    params.update({
        '__EVENTTARGET': 'ctl00$MainContent$gvTradeL',
        'ctl00$MainContent$tbSearch': '',
        'ctl00$MainContent$ddlTradeLType': '-1',
        'ctl00$MainContent$ddlTradeLStatus': '-1',
        'ctl00$cph1$pgvTrades$ctl22$ddlPager': str(page_number)
    })
    response = session.post(BASE_URL, headers=HEADERS, data=params)
    return response.text


def extract_trade_codes(html):
    """ Извлекает коды торгов из таблицы """
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'id': 'ctl00_cph1_pgvTrades'})
    if not table:
        return []
    rows = table.find_all('tr')[2:]
    return [row.find_all('td')[2].text.strip() for row in rows if len(row.find_all('td')) == 14]


def get_trade_data(trade_id):
    """ Парсит страницу товара и ищет автомобили """
    url = DETAIL_URL.format(trade_id)
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find('table', class_="product-table-basic")
    if not table:
        return None

    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            text = cell.text.strip().lower()
            if 'автомобиль' in text:
                match = re.search(r'(\d+)\s+(год[а]?)', text) or re.search(r'(\d+)\s+(г\.в\.)', text)
                year = int(match.group(1)) if match else 0
                if year >= 2010 or year == 0:
                    return {"url": url, "description": text, "year": year}
    return None


def main(start_page=1, end_page=5):
    """ Основная функция для парсинга заданного диапазона страниц """
    session = requests.Session()
    trade_ids = []

    print(f"🔍 Получаем торговые коды с {start_page} по {end_page} страницу...")
    for page in range(start_page, end_page + 1):
        html = get_page(session, page)
        trade_ids.extend(extract_trade_codes(html))
        time.sleep(1)

    print(f"✅ Найдено {len(trade_ids)} торгов.")

    print("🚗 Ищем автомобили 2010+ года...")
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for data in executor.map(get_trade_data, trade_ids):
            if data:
                results.append(data)

    print(f"✅ Найдено {len(results)} автомобилей.")

    df = pd.DataFrame(results)
    df.to_csv(os.path.join(SAVE_PATH, "cars.csv"), index=False, encoding="utf-8-sig")
    print(f"📂 Данные сохранены в {SAVE_PATH}/cars.csv")


if __name__ == "__main__":
    main(1, 5)  # Укажите нужный диапазон страниц
