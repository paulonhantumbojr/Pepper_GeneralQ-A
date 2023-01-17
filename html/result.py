import io
import requests

# https://stackoverflow.com/questions/14442636/how-can-i-check-if-a-checkbox-is-checked-in-selenium-python-webdriver
# driver.find_element_by_name('<check_box_name>').is_selected()
# driver.find_element_by_id('<check_box_id>').is_selected()

def toHTML(data): 

  # answers = ["Footy", "I am still learning", "A cling", "A Civil Engineer", "Canberra", "14th", "Murray River", "Fear of dogs", "An orange", "11"]

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

  s1 = int("0")
  s2 = int("0")
  s3 = int("0")  
  s4 = int("0")
  s5 = int("0")
  s6 = int("0")
  s7 = int("0")    
  s8 = int("0")
  s9 = int("0")
  s10 = int("0")

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

  result = (s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10) * 10 

  replacements = {
    'result': result,
  } 

  with open('index.html', 'U') as f:
    mainhtml = f.read()

    for key in replacements:
      mainhtml = mainhtml.replace('{' + key + '}', str(replacements[key]))

      return mainhtml

def send(html): 
  f = io.StringIO(unicode(html, 'UTF-8')) # apply unicode
  files = { 'file': f }

  requests.post('http://cloudvis.qut.edu.au:8082',files=files) # unsure of where this address is

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
    "q_a10r": "11", 
  })

  with open('out.html', 'w') as f:
    f.write(html)