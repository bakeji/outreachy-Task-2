import csv
import requests

# open and read the csv file using python csv module imported
with open ('Task 2 - Intern.csv', 'r') as file:
    csv_reader = csv.reader(file)
    # skip the header row-the csv file has a 'url' header role
    next(csv_reader, None)

    # loop throught the csv row, get the url from the row, send a request and get the status code.
    for row in csv_reader:
        url = row[0]

        try:
            response = requests.get(url, timeout=10 )
            status_code =response.status_code
            print(f"({status_code}) {url}")

        except requests.exceptions.RequestException as e:
            print(f"(ERROR) {url} - {e} ")
