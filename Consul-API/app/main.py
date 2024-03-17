from flask import Flask, jsonify
from consul_api import get_consul_status, get_cluster_summary, get_cluster_members, get_system_info
import logging

app = Flask(__name__)

# Configure logging
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

@app.route('/v1/api/consulCluster/status')
def status():
    return jsonify(get_consul_status())

@app.route('/v1/api/consulCluster/summary')
def summary():
    return jsonify(get_cluster_summary())

@app.route('/v1/api/consulCluster/members')
def members():
    return jsonify(get_cluster_members())

@app.route('/v1/api/consulCluster/systemInfo')
def system_info():
    return jsonify(get_system_info())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
