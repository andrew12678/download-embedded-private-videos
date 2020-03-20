from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess

def download_file(url, file_name):
    server = Server('./browsermob-proxy') #Local path to BMP
    server.start()
    proxy = server.create_proxy() #Proxy is used to generate a HAR file containing the connection URLS that the MP3s are loaded from.
    chrome_options = Options()
    chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy)) #Configure chrome options
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path='./chromedriver', options=chrome_options)
    proxy.new_har('filename') 
    driver.get(url)
    save = proxy.har
    server.stop()
    driver.quit()
    results = [entry['request']['url'] for entry in save['log']['entries']]
    embedded_link = [res for res in results if "https://embed.vhx.tv/videos" in res][0]
    subprocess.call(["./youtube-dl",
                 "-f" "best[height=540]",
                 "-o" "{}.mp4".format(file_name),
                 "--ignore-errors",
                 embedded_link])
    
with open('files.log', 'r') as f:
    for line in f:
        url = line.strip()[1:-1]
        file_name = url.split('videos/')[1]
        print(file_name)
        download_file(url, file_name)
