# Downloading embedded private videos

Useful for a select few subscription websites. For Jane.

## Setting up the files.log file

This file is expected to contain the href links to a new line delimited file containing URLs (with quotations retained) to visit. To generate such a file, some simple bs4 and requests could be used. An example snippet is shown below and a files.log example is provided in the repository. Note that this step is website dependent.

```python
import requests
from bs4 import BeautifulSoup
sess = requests.Session()
r = sess.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
links = [ele['href'] for ele in soup.find_all('a', {'class':'browse-item-link'})]
```

## Installing dependencies

[BrowserMob Proxy](https://bmp.lightbody.net/) is required to examine network traffic to obtain the embedded video links. Extracting the binary from the zip is sufficient for use.

[youtube-dl](https://github.com/ytdl-org/youtube-dl) is capable of downloading videos from embedded vhx links. We can install it without sudo permissions in the manner below

```console
wget https://yt-dl.org/downloads/latest/youtube-dl .
chmod u+rx ./youtube-dl
```

We use Chrome Selenium, the webdriver can be found here: [ChromeDriver](https://chromedriver.chromium.org/downloads) please select one that systems your current system + browser.

## Downloading

One should adjust how the downloaded files should be named based on the url split. If desired, the hard coded video resolutions should be adjusted for size references. Upon running the line below, the system will open up a Chrome browser, monitor the relevant network traffic to obtain the required url and then download it with youtube-dl. This is done iteratively for each URL, with the browser and proxy server closing at the end of each loop. Note: youtube-dl may be throttled so speeds may vary.

```console
python3 download_embedded_private.py
```






