import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Define the URL of the webpage you want to scrape
    urls = [
        'https://smasaga.hsu.is/MobileServices/api/ping' 
        ,'https://smasaga.hss.is/MobileServices/api/ping'
        ,'https://smasaga.hsa.is/MobileServices/api/ping'
        ,'https://smasaga.hvest.is/MobileServices/api/ping'
        ,'https://smasaga.hg.is/MobileServices/api/ping'
        ,'https://smasaga.hsn.is/MobileServices/api/ping'
        # ,'https://sagaapp.lsh.is/MobileServices/api/ping'
        ,'https://hve-smasaga.hve.is/MobileServices/api/ping'
        ,'https://smasaga.hvest.is/MobileServices/api/ping'
        ,
            ]

    # Send a GET request to the webpage
    highest_counts = {}
    for url in urls:
        response = requests.get(url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the second table on the page
        tables = soup.find_all('table')
        if len(tables) < 2:
            print("No second table found.")
            exit(1)

        table = tables[1]

        # Initialize a dictionary to store the highest count for each label

        # Iterate over the rows in the table
        for row in table.find_all('tr'):
            # Extract the cells from the row
            cells = row.find_all('td')
            if len(cells) < 3:
                continue

            # Extract the date, label, and counter from the cells
            date = cells[0].text.strip()
            label = cells[1].text.strip()
            institution = url.split('.')[1].upper()
            # label = institution + ' - ' + label if label != '' else label
            counter = int(cells[2].text.strip()) if cells[2].text.strip().isdigit() else 0

            # Update the highest count, date, and label if necessary
            if label != '':
                if label in highest_counts:
                    if counter > highest_counts[label][0]:
                        highest_counts[label] = (counter, date, institution)
                else:
                    highest_counts[label] = (counter, date, institution)

        # Print the result
        # print(f'{label}: {total}')
    return render_template('index.html', highest_counts=highest_counts)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)