# import basics
import os

# import stuff for our web server
from flask import Flask, request, redirect, url_for, render_template, session
from utils import get_base_url
import requests, model
import pandas as pd
import numpy as np

lawyers = pd.read_csv('static/lawyers.csv')

port = 12345
base_url = get_base_url(port)

# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
  app = Flask(__name__)
else:
  app = Flask(__name__, static_url_path=base_url + 'static')

app.secret_key = os.urandom(64)

# set up the routes and logic for the webserver


@app.route(f'{base_url}')
def home():
  return render_template('writer_home.html', generated=None)


@app.route(f'{base_url}', methods=['POST'])
def home_post():
  return redirect(url_for('results'))


@app.route(f'{base_url}/results/')
def results():
  if 'data' in session:
    data = session['data']
    return render_template('Write-your-story-with-AI.html', generated=data)
  else:
    return render_template('Write-your-story-with-AI.html', generated=None)


@app.route(f'{base_url}/generate_text/', methods=["POST"])
def generate_text():
  category = ''
  subcategory = ''
  error = ''

  attorney1 = {'ID': '', 'Hours Spent': 0, '% Match': ''}

  attorney2 = {'ID': '', 'Hours Spent': 0, '% Match': ''}

  attorney3 = {'ID': '', 'Hours Spent': 0, '% Match': ''}

  prompt = request.form['prompt']
  if prompt is not None:
    payload = {"inputs": prompt}

  generated_cat = model.query_cat(payload)
  generated_sub = model.query_sub(payload)

  if (len(generated_cat) < 2):
    error = 'Sorry! The model is still waking up (yawn). Please give it 30 seconds and try asking it again!'
    return render_template('results.html', error = error)
  else:
    try:
      category = generated_cat[0][0]['label']
      subcategory = generated_sub[0][0]['label']
    except:
      error = 'Sorry! The model is still waking up (yawn). Please give it 30 seconds and try asking it again!'
      return render_template('results.html', error = error)

  ethnicity = request.form['ethnicity']
  gender = request.form['gender']
  imprisoned = request.form['imprisoned']

  def score(category, subcategory, ethnicity, gender, imprisoned, row):
    if ethnicity in row['Ethnicities']:
      ethnicity_multiplier = 1
    else:
      ethnicity_multiplier = 0

    if (imprisoned == "Yes") & (row['Imprisoned'] != 0):
      imprisoned_multiplier = 1
    else:
      imprisoned_multiplier = 0

    if gender == 'Male':
      gender_multiplier = row['Male']
    elif gender == 'Female':
      gender_multiplier = row['Female']
    else:
      gender_multiplier = row['OtherGender']

    hours = row['Total Hours'] + 1

    sum1 = row[category] + row[subcategory]

    sum2 = ethnicity_multiplier + gender_multiplier

    sum3 = sum1 + sum2 + imprisoned_multiplier

    return sum3 / hours

  scores = np.array([
    score(category, subcategory, ethnicity, gender, imprisoned, row)
    for idx, row in lawyers.iterrows()
  ])

  top_indices = np.flip(np.argpartition(scores, -3)[-3:])
  attorney1['ID'] = lawyers['AttorneyUno'][top_indices[0]]
  attorney2['ID'] = lawyers['AttorneyUno'][top_indices[1]]
  attorney3['ID'] = lawyers['AttorneyUno'][top_indices[2]]
  attorney1['Hours Spent'] = lawyers['Total Hours'][top_indices[0]]
  attorney2['Hours Spent'] = lawyers['Total Hours'][top_indices[1]]
  attorney3['Hours Spent'] = lawyers['Total Hours'][top_indices[2]]
  top_scores = scores[top_indices] / np.max(scores)
  attorney1['% Match'] = top_scores[0]
  attorney2['% Match'] = top_scores[1]
  attorney3['% Match'] = top_scores[2]

  return render_template('results.html',
                         category=category,
                         subcategory=subcategory,
                         error=error,
                         attorney1=attorney1,
                         attorney2=attorney2,
                         attorney3=attorney3)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=port, debug=True)
