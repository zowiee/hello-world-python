# flask_web/app.py
import socket

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return "Hello world! I am runnig on host '" + socket.gethostname() + "' from MiniShift through Ultrahook!"

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
