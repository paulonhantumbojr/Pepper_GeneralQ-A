import io
import requests
from datetime import datetime

def toHTML(data, pages=None):
  quest = [
    data['q_a1'], #0
    data['q_a2'], #1
    data['q_a3'], #2
    data['q_a4'], #3
    data['q_a5'], #4
    data['q_a6r'], #5
    data['q_a6'], #6
    data['q_a7'], #7
    data['q_a8r'], #8
    data['q_a8'], #9   
    data['q_a9r'], #10
    data['q_a9'], #11  
    data['q_a10r'], #12
    data['q_a10'], #13  
  ]

  answ = [
    "Footy", #0
    "I am still learning", #1
    "A cling", #2
    "A Civil Engineer", #3
    "Canberra", #4
    "14th", #5 
    "Murray River", #6
    "Fear of dogs", #7
    "An orange", #8
    "11", #9
  ]

# If the associated name of the answer corresponds to the value provided then increment 10pts
  s1 = 10 if quest[0] == answ[0] else 0 
  s2 = 10 if quest[1] == answ[1] else 0 
  s3 = 10 if quest[2] == answ[2] else 0 
  s4 = 10 if quest[3] == answ[3] else 0
  s5 = 10 if quest[4] == answ[4] else 0 
  s6 = 10 if quest[5] == answ[5] or quest[6] == answ[5] else 0 
  s7 = 10 if quest[7] == answ[6] else 0 
  s8 = 10 if quest[8] == answ[7] or quest[9] == answ[7] else 0
  s9 = 10 if quest[10] == answ[8] or quest[11] == answ[8] else 0
  s10 = 10 if quest[12] == answ[9] or quest[13] == answ[9] else 0

  finsc = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10

  replacements = {
    'finsc': finsc,
    'select1': quest[0], 
    'correct1': answ[0],
    'select2': quest[1], 
    'correct2': answ[1],
    'select3': quest[2], 
    'correct3': answ[2],
    'select4': quest[3], 
    'correct4': answ[3],
    'select5': quest[4], 
    'correct5': answ[4],
    'select6': quest[5] if quest[5] == answ[5] else quest[6],
    'correct6': answ[5],    
    'select7': quest[7], 
    'correct7': answ[6],  
    'select8': quest[8] if quest[8] == answ[7] else quest[9], 
    'correct8': answ[7],    
    'select9': quest[10] if quest[10] == answ[8] else quest[11], 
    'correct9': answ[8],    
    'select10': quest[12] if quest[12] == answ[9] else quest[13], 
    'correct10': answ[9],    

    'tick1': '&#9989;' if quest[0] == answ[0] else '&#10060;',
    'tick2': '&#9989;' if quest[1] == answ[1] else '&#10060;',
    'tick3': '&#9989;' if quest[2] == answ[2] else '&#10060;',
    'tick4': '&#9989;' if quest[3] == answ[3] else '&#10060;',
    'tick5': '&#9989;' if quest[4] == answ[4] else '&#10060;',    
    'tick6': '&#9989;' if quest[5] == answ[5] or quest[6] == answ[5] else '&#10060;',  
    'tick7': '&#9989;' if quest[7] == answ[6] else '&#10060;', 
    'tick8': '&#9989;' if quest[8] == answ[7] or quest[9] == answ[7] else '&#10060;',  
    'tick9': '&#9989;' if quest[10] == answ[8] or quest[11] == answ[8] else '&#10060;',  
    'tick10': '&#9989;' if quest[12] == answ[9] or quest[13] == answ[9] else '&#10060;',  
  }

  with open('template.html', 'U') as f:
    template = f.read()

    for key in replacements:
      template = template.replace('{' + key + '}', str(replacements[key]))

  return template

def send(html):
  f = io.StringIO(unicode(html, 'UTF-8'))
  files = { 'file': f }

  requests.post('http://cloudvis.qut.edu.au:8082',files=files)

if __name__ == '__main__':
  html = toHTML({
    "q_a1": "Basketball",
    "q_a2": "Shaping leaders",
    "q_a3": "A troop",
    "q_a4": "A Mechanic",
    "q_a5": "Brisbane", 
    "q_a6r": "14th", 
    "q_a6": "11th",              
    "q_a7": "Lachlan River", 
    "q_a8r": "Fear of needles", 
    "q_a8": "Fear of heights",
    "q_a9r": "A banana", 
    "q_a9": "An apple",
    "q_a10r": "8", 
    "q_a10": "10",
  })
  
  with open('out.html', 'w') as f:
    f.write(html)