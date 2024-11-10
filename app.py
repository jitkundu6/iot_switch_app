from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# ThingSpeak API Details
THING_SPEAK_WRITE_API_KEY = '25NW11L7I3VXTI7O'
THING_SPEAK_READ_API_KEY = '882ZHLEJ3HS50QNB'
CHANNEL_ID = '2725686'
BASE_URL = "https://api.thingspeak.com"

# Route to the main interface
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to send a message to ThingSpeak
@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json.get('message')
    url = f"{BASE_URL}/update"
    params = {
        'api_key': THING_SPEAK_WRITE_API_KEY,
        'field1': message  # assuming field1 is where the message is stored
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return jsonify({"status": "Message sent successfully!"})
    else:
        return jsonify({"status": "Failed to send message"}), 500

# Endpoint to read the latest message from ThingSpeak
@app.route('/read_message', methods=['GET'])
def read_message():
    url = f"{BASE_URL}/channels/{CHANNEL_ID}/fields/1.json"
    params = {
        'api_key': THING_SPEAK_READ_API_KEY,
        'results': 1  # Get only the latest result
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        message = data['feeds'][0]['field1']
        return jsonify({"message": message})
    else:
        return jsonify({"status": "Failed to read message"}), 500

# Endpoint to control switches (using field2 for the switch)
@app.route('/control_switch', methods=['POST'])
def control_switch():
    switch_status = request.json.get('status')  # "on" or "off"
    value = 1 if switch_status == 'on' else 0  # assuming 1 = on, 0 = off
    url = f"{BASE_URL}/update"
    params = {
        'api_key': THING_SPEAK_WRITE_API_KEY,
        'field1': value  # assuming field2 is the switch control
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return jsonify({"status": f"Switch turned {switch_status}!"})
    else:
        return jsonify({"status": "Failed to control switch"}), 500

if __name__ == '__main__':
    app.run(debug=True)
