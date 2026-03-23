# Addressing the lusophone technological wishlist proposals - Create a Python script to get and print the `status code` of the response of a list of URLs from a `.csv` file.

## Description
This python script read URLs from a csv file and checks their HTTP status code

## Objective
Create a python script to get and print the status code of the response of a list of URLs fro a .csv file

## Task Details
-**program**: Outreachy Internship
-**project**: Addressing the lusophone technological wishlist proposals
-**Organization**: Wikimedia

## Requirements

**Python Version:**
- Python 3.6 or higher

**Dependencies:**
This project requires the `requests` library for making HTTP requests.

### Installation Steps

1. **Check if Python is installed:**
```bash
   python --version
```

2. **Install the required library:**
```bash
   pip install requests
```

   Or if you're using Python 3 specifically:
```bash
   pip3 install requests
```

3. **Verify installation:**
```bash
   python -m pip show requests
```

## How to Run
```bash
python index.py
```

## Output Format
````
(200) https://example.com
(404) https://example.com/not-found
