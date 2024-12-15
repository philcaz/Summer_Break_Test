# Overview
This is a simple Flask-based web service that helps process summer mowing revenue and expense data to generate a tax-friendly financial report. It supports:
- Uploading transaction data in CSV format via a POST /transactions endpoint.
- Querying the summary of gross revenue, expenses, and net revenue via a GET /report endpoint.

# Environment Setup
## Prerequistes
1. Python 3.8 or above.
2. pip for package management.
## Installation Steps
0. MacOS and Linux: Use Default Terminal. Windows: Use Git Bash
1. Open a terminal (T1), clone this repository

    - ```git clone https://github.com/philcaz/Summer_Break_Test.git```
  
    - ```cd Summer_Break_Test```
  
2. Install dependencies
    - ```pip install -r requirements.txt```

3. Run the application
    - ```python api.py```

4. Open a new terminal (T2), test API Endpoints
    - if not under /Summer_Break_Test, ```cd Summer_Break_Test```
    - ```./tests/test.sh```

5. Stop the application in T1
    - ```Ctrl + C```

# Solution Approach
1. Used Python's builtin ```csv``` library for lightweight data parsing
2. Used a global list ```data``` to hold in-memory transactions, avoiding persistence for the MVP 
# Assumptions
1. The CSV data does not have headers ```Date, Type, Amount($), Memo```
2. Type can only be ```Income``` or ```Expense```
3. All amounts are in valid numeric formats

# Shortcomings
1. Data is stored in memory, which is hard to scale for large datasets
2. Insufficient data quality check, such as for invalid dates and duplicate entries

# Improvements if time allowed
1. Connect the application to a database to persist data storage
2. Implement more comprehensive data validation and deduplication
3. Add more detailed reporting such as monthly summaries
