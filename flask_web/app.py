# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return "hello world from MiniShift through Ultrahook!"

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
