from flask import Flask, render_template
import psutil,os,socket,platform
app = Flask(__name__)

@app.route("/")

def index():
    return render_template('index.html', cores=psutil.cpu_count(), ramused=psutil.virtual_memory()[2], osversion=platform.platform(),hostname=socket.gethostname(), cpupercent=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2)))

if __name__ == "__main__":
    app.run(host='0.0.0.0')

