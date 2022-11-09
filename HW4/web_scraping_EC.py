import json
import urllib.request
import pandas as pd
import requests
from bs4 import BeautifulSoup
import webbrowser

#-------------------------------------------------------------
#                 Part 1: UCDenver departments
#-------------------------------------------------------------
def ucdenver_webscrape():

    url = 'http://www.ucdenver.edu/pages/ucdwelcomepage.aspx'

    headers = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.3'}

    # accessing the url
    request = urllib.request.Request(url,headers=headers)

    # parsing html
    html = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(html, 'html.parser')

    # finding all scripts
    main_table = soup.findAll("script", {"type": "application/ld+json"})

    # creating container with data loaded in json for first element in containers, stripping the text
    dept_containers = json.loads(main_table[0].text.strip())

    # scraping department from dept_container
    departments = dept_containers["department"]

    new_list = []
    i = 0
    # for each element inside departments we are storing the name, telephone, and url into department {}
    for dep in departments:
        i += 1
        department = {"No.": i, "name": dep.get("name", "Not available"),
                      "telephone": dep.get("telephone", "Not found"),
                      "url": dep.get("url", "Not found")}
        new_list.append(department)  # creating dictionary


    # Save to file 'links.json'
    with open('links.json', 'w') as links:
        json.dump(new_list, links, indent=1)


# REF:https://www.scrapehero.com/a-beginners-guide-to-web-scraping-part-2-build-a-scraper-for-reddit/

#-------------------------------------------------------------
#                  Part 2: COVID-19 stats table
#-------------------------------------------------------------

def covid_webscrape():

    pd.pandas.set_option('display.max_columns', None)

    url= 'https://covid19.colorado.gov/data'


    # Make a GET request to fetch the raw HTML content
    html_content = requests.get(url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, 'html.parser')


    # Get the table
    table = soup.find("table")
    table_rows = table.find_all('tr')

    # Create empty lists for column headings & table rows
    headings = []
    rows = []

    # For each table row found, find all "td" cells
    for tr in table_rows:
        td = tr.find_all('td')

        # In the Covid data table, the columns are really the first cell in every row
        # So we grab the text for every cell in a row, then use index to save the header/row text separately
        full_row = [tr.text for tr in td]
        header = full_row[0]
        row = full_row[1]

        # Add the text to the lists
        headings.append(header)
        rows.append(row)

    # Create a Pandas DataFrame object, and set the headings[] as indices (it won't work using columns= for some reason)
    # Transpose ().T  the DataFrame since it will be sideways otherwise (i.e. the headings will be in the 1st column)
    df = pd.DataFrame(rows, index=headings).T


    # save the DataFrame as html table in file
    with open('covid_data.html', 'w') as f:
        print(df.to_html(), file=f)

    # Open the html file as a web browser tab
    webbrowser.open_new_tab('covid_data.html')


# REF: https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup



#-------------------------------------------------------------
#                      Driver Code
#-------------------------------------------------------------

ucdenver_webscrape()
covid_webscrape()