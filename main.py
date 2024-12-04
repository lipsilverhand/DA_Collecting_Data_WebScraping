from bs4 import BeautifulSoup
import requests
import csv

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"

response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.content, "html.parser")
else:
    print("Failed to fetch the website")
    soup = None

if soup:
    table = soup.find("table")
    rows = table.find_all("tr")[1:]

    data = []

    for row in rows:
        cols = row.find_all("td")
        language = cols[1].text.strip()
        avg_annual_salary = cols[3].text.strip()
        data.append([language,avg_annual_salary])

    with open("popular_langues.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Language", "Average Annual Salary"])  
        writer.writerows(data) 

    print("Data successfully saved to file")