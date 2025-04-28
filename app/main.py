from flask import Flask, jsonify, request
from utils import fetch_earthquakes, filter_felt_reports, filter_tsunami_alerts
from cache import Cache

app = Flask(__name__)
cache = Cache()

@app.route('/earthquakes', methods=['GET'])
def get_earthquakes():
    starttime = request.args.get('starttime')
    endtime = request.args.get('endtime')
    if not starttime or not endtime:
        return jsonify({'error': 'starttime and endtime are required'}), 400
    data = fetch_earthquakes(starttime, endtime)
    return jsonify(data)

@app.route('/earthquakes/felt', methods=['GET'])
def get_earthquakes_felt():
    starttime = request.args.get('starttime')
    endtime = request.args.get('endtime')
    if not starttime or not endtime:
        return jsonify({'error': 'starttime and endtime are required'}), 400
    data = fetch_earthquakes(starttime, endtime)
    filtered = filter_felt_reports(data)
    return jsonify(filtered)

@app.route('/earthquakes/tsunami', methods=['GET'])
def get_earthquakes_tsunami():
    state = request.args.get('state')
    if not state:
        return jsonify({'error': 'state parameter is required'}), 400
    data = fetch_earthquakes('now-1day', 'now')
    filtered = filter_tsunami_alerts(data, state)
    return jsonify(filtered)

# Run with Gunicorn for production
if __name__ == '__main__':
    # Ensure this block runs only in development
    app.run(debug=False, host='0.0.0.0', port=5000)
