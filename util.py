import requests
from bs4 import BeautifulSoup

url = "https://www.naeu.playblackdesert.com/en-US/GameInfo/Class/Main"  # Replace with the URL of the website you want to scrape
class_name = "class_name"  # Replace with the actual class name you're targeting

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <div> elements with the specified class
    div_elements = soup.find_all('div', class_=class_name)
    print(div_elements)
    # Loop through the list of div elements and print their content
    for div in div_elements:
        print(div.text)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
