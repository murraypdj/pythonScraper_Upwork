import requests
import pandas as pd

def scrape_data():
    # 望ましいパラメータを使用してAPI URLを指定します
    url = 'https://api.aia.org/firm-directory?filter[country]=&filter[state]=&page[number]=1&page[size]=22936&q=&sort[criteria]=firm_name&sort[order]=asc'

    # APIエンドポイントにGETリクエストを送信します
    response = requests.get(url)

    if response.status_code == 200:
        # レスポンスからJSONデータを抽出します
        json_data = response.json()

        # JSONから企業データを抽出します
        firms_data = json_data.get('data', [])

        # 各企業エントリから関連する情報を抽出します
        data = []
        for firm in firms_data:
            firm_attributes = firm.get('attributes', {})
            firm_name = firm_attributes.get('firm_name', '')
            firm_address = firm_attributes.get('address_line_1', '')
            firm_city_state = f"{firm_attributes.get('city', '')}, {firm_attributes.get('state', '')}"
            firm_country = firm_attributes.get('country', '')
            firm_website = firm_attributes.get('firm_url', '')

            data.append([firm_name, firm_address, firm_city_state, firm_country, firm_website])

        # データをExcelファイルに保存します
        file_name = 'firm_directory.xlsx'
        df = pd.DataFrame(data, columns=['Company Name', 'Address', 'City/State', 'Country', 'Website'])
        df.to_excel(file_name, sheet_name='Firm Data', index=False)

        print(f'Saved data to {file_name}.')
    else:
        print('APIからデータを取得できませんでした。')

# 関数を呼び出してデータをスクレイピングします
scrape_data()
