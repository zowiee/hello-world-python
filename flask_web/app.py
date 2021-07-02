# flask_web/app.py
import socket

from flask import Flask
app = Flask(__name__)
      
@app.route('/')
def home():  
   f = open("/data/sharedfile.txt")
   contents = f.read()
   return "<h1>Hello world!</h1><br/>I am runnig on host '" + socket.gethostname() + "' from MiniShift through Ultrahook!<br/><br/>Shared file content:<br/><br/>" + contents 

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
