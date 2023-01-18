import io
import requests

def toHTML(data, pages=None):

  q1 = str(data['q_a1'])
  q2 = str(data['q_a2'])
  q3 = str(data['q_a3'])
  q4 = str(data['q_a4'])
  q5 = str(data['q_a5'])
  q6r = str(data['q_a6r'])
  q6 = str(data['q_a6'])  
  q7 = str(data['q_a7']) 
  q8r = str(data['q_a8r']) 
  q8 = str(data['q_a8']) 
  q9r = str(data['q_a9r']) 
  q9 = str(data['q_a9']) 
  q10r = str(data['q_a10r']) 
  q10 = str(data['q_a10']) 

  s1 = int('0')
  s2 = int('0')
  s3 = int('0')  
  s4 = int('0')
  s5 = int('0')
  s6 = int('0')
  s7 = int('0')    
  s8 = int('0')
  s9 = int('0')
  s10 = int('0')

  if q1 == "Footy":
    s1 = s1 + 1

  if q2 == "I am still learning":
    s2 = s2 + 1

  if q3 == "A cling":
    s3 = s3 + 1    

  if q4 == "A Civil Engineer":
    s4 = s4 + 1

  if q5 == "Canberra":
    s5 = s5 + 1    

  if (q6r or q6) == "14th":
    s6 = s6 + 1  

  if q7 == "Murray River":
    s7 = s7 + 1  

  if (q8r or q8) == "Fear of dogs":
    s8 = s8 + 1  

  if (q9r or q9) == "An orange":
    s9 = s9 + 1  

  if (q10r or q10) == "11":
    s10 = s10 + 1 

  finalscore = str((s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10) * 10)

  replacements = {
    'finalscore': finalscore,
    'Section1': 'display:block' if not pages or 1 in pages else 'display: none;',
    'Page1': 'display:block' if not pages or 1 in pages or 2 in pages else 'display: none;',
    'Footer': 'display:block' if not pages else 'display: none;'
  }

  with open('score.html', 'U') as f:
    score = f.read()

    for key in replacements:
      score = score.replace('{' + key + '}', str(replacements[key]))

  return score

# Send html data/complete file to a QUT(Queensland University of Technology) local server
def send(html):
  f = io.StringIO(unicode(html, 'UTF-8')) # unicode is for Python 2, str is for Python 3
  files = { 'file': f }

  requests.post('http://cloudvis.qut.edu.au:8082',files=files)

if __name__ == '__main__':
  html = toHTML({
    "q_a1": "Footy",
    "q_a2": "I am still learning", 
    "q_a3": "A cling", 
    "q_a4": "A Civil Engineer", 
    "q_a5": "Canberra", 
    "q_a6r": "14th", 
    "q_a6": "14th", 
    "q_a7": "Murray River", 
    "q_a8r": "Fear of dogs", 
    "q_a8": "Fear of dogs", 
    "q_a9r": "An orange", 
    "q_a9": "An orange", 
    "q_a10": "11", 
    "q_a10r": "11"
  })
  
  with open('out.html', 'w') as f:
    f.write(html)