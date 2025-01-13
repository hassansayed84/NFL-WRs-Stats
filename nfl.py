import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

year= input(str("enter year:" ))

url = 'https://www.pro-football-reference.com/years/'+year+'/receiving.htm'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


div_container = soup.find('div', id='div_receiving')

if div_container is not None:

    table = div_container.find('table')

    if table:
        #Process the table rows and extract data
        top_players = []

        for row in table.find_all('tr'):
            cells = row.find_all('td')
            if cells:
                player_name = cells[0].get_text(strip=True)
                position = cells[3].get_text(strip=True)

                if position == "WR":
                    player_data = {
                        'Name': player_name,
                        'Receptions': cells[7].get_text(strip=True),
                        'Receiving Yards': cells[8].get_text(strip=True),
                        'Touchdowns' :cells[10].get_text(strip=True),
                    }
                    top_players.append(player_data)
                if len(top_players)==10:
                    break
print(top_players)

receptions = [int(player['Receptions']) for player in top_players]
receiving_yards = [int(player['Receiving Yards']) for player in top_players]
touch_downs= [int(player['Touchdowns']) for player in top_players]
names = [player['Name'] for player in top_players]


import matplotlib.pyplot as plt

# Create scatter plot
plt.scatter(receptions, receiving_yards, color='blue',label='(#) = TDs')

# Adding labels for each player with touchdowns included
for x in range(len(receptions)):
    label = f"{names[x]} ({touch_downs[x]})"
    plt.text(receptions[x], receiving_yards[x], label)

# Set x-axis and y-axis labels and title
plt.xlabel('Receptions')
plt.ylabel('Receiving Yards')
plt.title('Top 10 WRs: Receptions vs. Receiving Yards in ' + year)

plt.legend(loc='upper left') 

# Show plot
plt.show()




