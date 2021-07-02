# flask_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   colors = ['\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m', '\033[91m', '\033[0m', '\033[1m', '\033[4m']
   myColor = random.choice(colors)
   return myColor + "hello world from MiniShift through Ultrahook!" + myColor

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
