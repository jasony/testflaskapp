from src.app import app
import os

__author__ = 'jslvtr'

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=Fal,host='0.0.0.0', port=port)
