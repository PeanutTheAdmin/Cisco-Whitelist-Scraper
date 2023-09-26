# pip install beautifulsoup4
# pip install requests

import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://www.cisco.com/c/en/us/support/docs/security/sourcefire-amp-appliances/118121-technote-sourcefire-00.html"

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

     # Find all tables with class 'sptable' and select the 9th one (index 8)
    ip_tables = soup.find_all('table', class_='sptable')
    if len(ip_tables) >= 9:
        ip_table = ip_tables[8]
        
         # Find all tables with class 'sptable' and select the 9th one (index 8)
    ip_tables = soup.find_all('table', class_='sptable')
    if len(ip_tables) >= 9:
        ip_table = ip_tables[8]
        
        # Find the fifth <td> section and extract the IP addresses
        ip_addresses = []
        td_elements = ip_table.find_all('td')
        if len(td_elements) >= 4:
            fifth_td = td_elements[3]
            for p_tag in fifth_td.find_all('p'):
                # IP addresses are separated by <br/> tags, so we split the text using <br/>
                ip_addresses.extend(p_tag.stripped_strings)
            
            # Save the extracted IP addresses to a text file
            with open('cisco_US_whitelisted_ips.txt', 'w') as file:
                for ip in ip_addresses:
                    file.write(ip + '\n')
        else:
            print("Less than 5 <td> elements found in the 9th table with class 'sptable'.")
    else:
        print("Less than 9 tables with class 'sptable' found on the webpage.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")