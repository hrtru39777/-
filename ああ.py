from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
import os


# Edgeのオプションを設定
options = EdgeOptions()
options.use_chromium = True  # ChromiumベースのEdgeを使用する
new_profile_path = os.path.expanduser('~/Library/Application Support/Microsoft Edge/SeleniumProfile')

options.add_argument(f'--user-data-dir={new_profile_path}')

path = '~/msedgedriver'
# WebDriverを起動
driver = webdriver.Edge(service=Service(), options=options)

# ウェブサイトを開く
driver.get('https://python-basic.com/')

# ユーザーの入力を待つ
input("結果を確認した後、何かキーを押してください...")

# ブラウザを閉じる
driver.quit()

