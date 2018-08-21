from flask import Flask, render_template, request
from tinydb import TinyDB, Query
import music
import json

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('kiosk.html')

@app.route('/music/start', methods=['POST'])
def start_music():
  music.start()
  return 'Success'

@app.route('/music/stop', methods=['POST'])
def stop_music():
  music.stop()
  return 'Success'

@app.route('/music/toggle', methods=['POST'])
def toggle_music():
  music.toggle()
  return 'Success'

@app.route('/wakes/list')
def list_wakes():
  # db = TinyDB('/Users/sage/Documents/GitHub/goto_sleep/app_storage.json')
  # wakes = db.table('wakes')
  return 'Success'

@app.route('/wakes/create', methods=['GET', 'POST'])
def create_wake():
  if request.method == 'GET':
    return render_template('create.html')

  