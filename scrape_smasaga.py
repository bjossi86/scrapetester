import importlib

# List of dependencies to check and install if needed
# dependencies = ['requests', 'beautifulsoup4']

# Check if each dependency is already installed
# for dependency in dependencies:
#     try:
#         importlib.import_module(dependency)
#     except ImportError:
#         # Install the dependency
#         import subprocess
#         import sys
        
#         subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependency])
#         importlib.import_module(dependency)

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
        ,
            ]

    data = [
        # {'url': 'https://smasaga.hsu.is/MobileServices/api/ping', 'count': 0},
        # {'url': 'https://smasaga.hss.is/MobileServices/api/ping', 'count': 0},
        # {'url': 'https://smasaga.hsa.is/MobileServices/api/ping', 'count': 0},
        # {'url': 'https://smasaga.hvest.is/MobileServices/api/ping', 'count': 0},
        # {'url': 'https://smasaga.hg.is/MobileServices/api/ping', 'count': 0}
    ]

    # Send a GET request to the webpage
    for url in urls:
        response = requests.get(url)

        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table on the page
        table = soup.find_all('table')

        # Find all rows in the table
        rows = table[1].find_all('tr')

        # Get the values from the rightmost column in each row and add them together
        total = 0
        for row in rows:
            # Find the rightmost cell in the row
            cells = row.find_all('td')
            if len(cells) > 0:
                rightmost_cell = cells[-1].text.strip()  # Adjust the index if needed

                # Check if the rightmost cell is not null
                if rightmost_cell:
                    # Convert the value to an integer and add it to the total
                    total += int(rightmost_cell) if rightmost_cell.isdigit() else 0

        # Add a label to the total
        label = url.split('.')[1].upper()
        data.append({'name': label, 'count': total})

        # Print the result
        # print(f'{label}: {total}')
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)