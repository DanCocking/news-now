from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import  webbrowser
import re

def economist():
    url = 'https://www.economist.com/'
    req = Request(url, headers={'User-Agent': 'Mozilla'})
    file = urlopen(req)
    soup = BeautifulSoup(file.read(), "html.parser")

    i = 1
    main_links = []
    for link in soup.find_all('a'):
        if link.get('data-analytics') == f'top_stories:headline_{i}':
            i+=1
            main_links.append(link)


    html_economist = ("""
    <h1>
    <img src="pngegg.png" alt="The Economist" width="1066" height="327">
    </h1>
    <div class="link-group">
    """)
    

    for link in main_links:
        html_economist += "<div>"
        html_economist += (str(link))
        html_economist += "</div>"
    return html_economist

def smh():

    html_smh = """</div> 
    <h1 class="smh-head">
    <img src="smh-logo_New.png" alt="Sydney Mroning Herald" width="1184" height="182">
    </h1>
    <div class="link-group">
    """

    urlsmh = 'https://www.smh.com.au/'
    reqsmh = Request(urlsmh, headers={'User-Agent': 'Mozilla'})
    filesmh = urlopen(reqsmh)
    soupsmh = BeautifulSoup(filesmh.read(), "html.parser")

    i = 1
    main_links = []
    for link in soupsmh.find_all('a'):
        if link.get('data-testid') == "article-link" and not link.has_attr('tabindex') and not link.has_attr('target') and not re.findall("The Watchlist newsletter", str(link)):
            i+=1
            
            main_links.append(link)

    main_links_urld = []
    for link in main_links:
        link_split = str(link).split("href=")
        link_split[1] = "href=\"http://www.smh.com.au/" + link_split[1].lstrip('"')
        link_urld = link_split[0] + link_split[1]
        main_links_urld.append(link_urld)

    i = 0
    while i < 9:

        html_smh += "<div>"
        html_smh += main_links_urld[i]
        html_smh += "</div>"
        i += 1
    return html_smh

def file_open():
    html_begining = """
    <html>
    <head>
        <link rel="stylesheet" href="newsrn.css">
    </head>
    <body>"""

    return html_begining

def file_close():
    html_close = """</div></body>
    </html>"""
    return html_close

if __name__ == '__main__':
    html_file = open('/home/dan/Documents/python_projects/newsrn/newsrn.html', 'w')
    html_file.write(file_open() + smh() + economist() + file_close())
    html_file.close()
    webbrowser.open_new_tab('/home/dan/Documents/python_projects/newsrn/newsrn.html')