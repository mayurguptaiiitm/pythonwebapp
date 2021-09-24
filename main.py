from flask import Flask, render_template
import psutil,os,socket,platform
app = Flask(__name__)

@app.route("/")

def index():
    return render_template('index.html', cores=psutil.cpu_count(), ramused=psutil.virtual_memory()[2], osversion=platform.platform(),hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0')

