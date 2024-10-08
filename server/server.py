from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

@app.route("/endpoint", methods=['POST'])
def codeFromEditor():
    if request.method == 'POST':
        print("POST")
        data = request.get_data()

        if data:
            response = {
                "message": "Data received successfully",
                "data": data
            }
            return response, 200
    else:
        print("GET")
        return "Received a GET request"

if __name__ == "__main__":
    app.run(debug=True)
