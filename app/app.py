from flask import Flask, jsonify
import requests
import socket

app = Flask(__name__)

@app.route('/')
def get_server_info():
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()

    hostname = socket.gethostname()

    response_data = {
        "IP": ip_data["ip"],
        "hostname": hostname
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8087, debug=True)
