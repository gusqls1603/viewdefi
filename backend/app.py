from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()

app = Flask('app')

@app.route('/', methods=['GET'])
def index():
    return 'Success'

@app.route('/currentList', methods=['GET'])
def currentList():
    return 'Success'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)