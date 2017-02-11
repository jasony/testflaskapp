#from src.app import app
import os

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World!"
		
__author__ = 'jslvtr'

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(hfost='0.0.0.0', port=port)
