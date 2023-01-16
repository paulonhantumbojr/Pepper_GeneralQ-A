import io 
import requests
from datetime import datetime # Module to work with date and time

def toHTML(data): # toHTML(data, pages=None)

# The aim is to check whether a text box is checked and based on that add a score. Aim: Check whether it's impossible to interface between
  x1 = 0;
  if data['correct1'].checked:
    x1 += x1;

  x2 = 0;
  if data['correct2'].checked:
    x2 += x2;

  x3 = 0;
  if data['correct3'].checked:
    x3 += x3;

  x4 = 0;
  if data['correct4'].checked:
    x4 += x4;

  x5 = 0;
  if data['correct5'].checked:
    x5 += x5;

  x6 = 0;
  if data['correct6r'].checked or data['correct6'].checked:
    x6 += x6;

  x7 = 0;
  if data['correct7'].checked:
    x7 += x7;

  x8 = 0;
  if data['correct8r'].checked or data['correct8'].checked:
    x8 += x8;

  x9 = 0;
  if data['correct8r'].checked or data['correct8'].checked:
    x9 += x9;

  x10 = 0;
  if data['correct10r'].checked or data['correct10'].checked:
    x10 += x10;

  result = (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10) * 10; 

  replacements = {
    'result': result,
  }

  with open('index.html', 'U') as f:
    template = f.read()

    for key in replacements:
      template = template.replace('{' + key + '}', str(replacements[key]))

  return template

def send(html):
  f = io.StringIO(unicode(html, 'UTF-8'))
  files = { 'file': f }

  requests.post('http://cloudvis.qut.edu.au:8082',files=files) # unsure of what this means

if __name__ == '__main__':
  html = toHTML({
    "correct1": "0", # I think it would be 0 as when you increment it, it goes to 1 
    "correct2": "0", 
    "correct3": "0", 
    "correct4": "0", 
    "correct5": "0", 
    "correct6r": "0", 
    "correct6": "0", 
    "correct7r": "0", 
    "correct7": "0", 
    "correct8r": "0", 
    "correct8": "0", 
    "correct9r": "0", 
    "correct9": "0", 
    "correct10r": "0", 
    "correct10": "0", 
  })
  with open('out.html', 'w') as f:
    f.write(html)