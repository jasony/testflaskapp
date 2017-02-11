from src.app import app
import os

__author__ = 'jslvtr'

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
