from flask import Flask, jsonify, render_template
import os
import pickle

app = Flask(__name__)

@app.route("/")
def hello_world():
    home_directory = os.path.expanduser('~')
    active_containers = pickle.Unpickler(open(f'{home_directory}/deploy-juzam/deploy-on-branch-change/details-latest.txt', 'rb')).load()
    for container in active_containers:
        container['hostPort'] = str(container['hostPort'])
    cluster_host = os.getenv('CLUSTER_HOST')
    print(cluster_host)
    return render_template('home.html', containers=active_containers, cluster_host=f'{cluster_host}')

@app.route("/celery_error_logs")
def return_offers_errors_log():
    logfile = open("/home/ubuntu/juzam2/celery-logs.txt", "r")
    lines = []
    for line in logfile:
        if "Error" in line: lines.append(line)
    return render_template('logs.html', lines=lines)

@app.route("/celery_logs")
def return_offers_log():
    logfile = open("/home/ubuntu/juzam2/celery-logs.txt", "r")
    lines = []
    for line in logfile:
        lines.append(line)
    print(lines)
    return render_template('logs.html', lines=lines)
