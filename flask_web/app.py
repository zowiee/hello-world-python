# flask_web/app.py
import socket
import random
from flask import Flask

app = Flask(__name__)
colors = ['red', 'blue', 'green', 'cyan', 'yellow', 'brown']

@app.route('/')
def home():  
      color = random.choice(colors)
      f = open("/data/sharedfile.txt")
      contents = f.read()
      return "<div style='background:" + color + "'><h1>Hello world!</h1><br/>I am runnig on host '" + socket.gethostname() 
            + "' from MiniShift through Ultrahook!<br/><br/>Shared file content:<br/><br/>" + contents 
            + </div>

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
