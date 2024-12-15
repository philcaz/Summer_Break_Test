# simple curl test of 2 endpoints assuming default port for Flask, adjust as needed

# ensure Flask is running before executing
echo "Test starting for API endpoints"

# test POST /transactions
echo "Testing POST /transactions with data.csv..."
curl -X POST http://127.0.0.1:5000/transactions -F "data=@./tests/data.csv"
echo -e "\n"

# test GET /report
echo "Testing GET /report..."
curl http://127.0.0.1:5000/report
echo -e "\n"

echo "Tests completed."
