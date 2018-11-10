from flask import Flask, render_template
import socket
app = Flask(__name__)

@app.route('/')
def map_main():
    ip = socket.gethostbyname(socket.gethostname())
    return render_template('map.html', ip=ip)

@app.route('/<node_name>')
def show_node_pings(node_name):
    ip = socket.gethostbyname(socket.gethostname())
    return render_template('node_pings.html', ip=ip, node_name=node_name)
