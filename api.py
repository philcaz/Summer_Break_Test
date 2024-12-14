from flask import Flask, request, jsonify
import csv
from io import StringIO

app = Flask(__name__)

HEADERS = ['Date', 'Type', 'Amount($)', 'Memo']
data = []

@app.route('/')
def home():
    return "<h1>Homepage placeholder</h1> <p>Use '/transactions' to POST data and '/report' to GET report.</p>"

@app.route('/report', methods=['GET'])
def get_report():
    # calculate and return the financial report
    global data
    try:    
        income = sum(item['amount'] for item in data if item['type'] == 'Income')
        expense = sum(item['amount'] for item in data if item['type'] == 'Expense')
        net_revenue = income - expense

        report = {
            "gross-revenue": round(income, 2),
            "expenses": round(expense, 2),
            "net-revenue": round(net_revenue, 2)
        }
        return jsonify(report), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/transactions', methods=['POST'])
def post_transactions():
    # receive and store transactions from a csv file.
    global data
    try:
        file = request.files['data']
        content = file.stream.read().decode('utf-8')
        reader = csv.reader(StringIO(content))
        rows = []
        for row in reader:
            if row and not row[0].startswith("#"):
                cleaned_row = [value.strip() for value in row]
                rows.append(dict(zip(HEADERS, cleaned_row)))
        
        #print(rows)
        for row in rows:
            # validate and parse each row
            date = row['Date']
            type_ = row['Type']
            amount = float(row['Amount($)'])
            memo = row['Memo'].strip('')
            
            # validate type values
            if type_ not in ['Income', 'Expense']:
                return jsonify({"error": "Invalid type in data."}), 400

            data.append({
                'date': date,
                'type': type_,
                'amount': amount,
                'memo': memo
            })

        #print("current data in memory after upload:", data)
        return jsonify({"message": "Transactions uploaded successfully."}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
