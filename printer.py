import io
import requests

def toHTML(data, pages=None): #data variable represents the 'name' elements in index.html 
  quest = [
    data['q_a1'], #0 (Question 1)
    data['q_a2'], #1 (Question 2)
    data['q_a3'], #2 (Question 3)
    data['q_a4'], #3 (Question 4)
    data['q_a5'], #4 (Question 5)
    data['q_a6r'], #5 (Question 6 prior-recommendation)
    "", #6 data['r_6'] (Question 6 recommendation)
    "", #7 data['q_a6'] (Question 6 after-recommendation)
    data['q_a7'], #8 (Question 7)
    data['q_a8r'], #9 (Question 8 prior-recommendation)
    "", #10 data['r_8'] (Question 8 recommendation)
    "", #11 data['q_a8'] (Question 8 after-recommendation)
    data['q_a9r'], #12 (Question 9 prior-recommendation)
    "", #13 data['r_9'] (Question 9 recommendation)
    "", #14 data['q_a9'] (Question 9 after-recommendation)
    data['q_a10r'], #15 (Question 10 prior-recommendation)
    "", #16 data['r_10'] (Question 10 recommendation)
    "", #17 data['q_a10'] (Question 10 after-recommendation)
  ]

  answ = [
    "Footy", #0 (Answer to Q1)
    "I am still learning", #1 (Answer to Q2)
    "A cling", #2 (Answer to Q3)
    "A Civil Engineer", #3 (Answer to Q4)
    "Canberra", #4 (Answer to Q5)
    "14th", #5 (Answer to Q6) 
    "Murray River", #6 (Answer to Q7)
    "Fear of dogs", #7 (Answer to Q8)
    "An orange", #8 (Answer to Q9)
    "11", #9 (Answer to Q10)
  ]

  rec = [
    "Yes", #0
    "No", #1
  ]

  s1 = 10 if quest[0] == answ[0] else 0 
  tickpts1 = True if s1 == 10 else False

  s2 = 10 if quest[1] == answ[1] else 0 
  tickpts2 = True if s2 == 10 else False

  s3 = 10 if quest[2] == answ[2] else 0 
  tickpts3 = True if s3 == 10 else False

  s4 = 10 if quest[3] == answ[3] else 0
  tickpts4 = True if s4 == 10 else False

  s5 = 10 if quest[4] == answ[4] else 0 
  tickpts5 = True if s5 == 10 else False

  quest[6] = data['r_6'] if quest[5] != answ[5] else quest[6] == ""
  quest[7] = data['q_a6'] if quest[5] != answ[5] and quest[6] == rec[0] else quest[7] == ""
  s6 = 10 if quest[5] == answ[5] else 0 if quest[5] != answ[5] and quest[6] == rec[1] else 10 if quest[5] != answ[5] and quest[6] == rec[0] and quest[7] == answ[5] else 0 
  tickpts6 = True if s6 == 10 else False

  s7 = 10 if quest[8] == answ[6] else 0 
  tickpts7 = True if s7 == 10 else False

  quest[10] = data['r_8'] if quest[9] != answ[7] else quest[10] == ""
  quest[11] = data['q_a8'] if quest[9] != answ[7] and quest[10] == rec[0] else quest[11] == ""
  s8 = 10 if quest[9] == answ[7] else 0 if quest[9] != answ[7] and quest[10] == rec[1] else 10 if quest[9] != answ[7] and quest[10] == rec[0] and quest[11] == answ[7] else 0 
  tickpts8 = True if s8 == 10 else False

  quest[13] = data['r_9'] if quest[12] != answ[8] else quest[13] == ""
  quest[14] = data['q_a9'] if quest[12] != answ[8] and quest[13] == rec[0] else quest[14] == ""
  s9 = 10 if quest[12] == answ[8] else 0 if quest[12] != answ[8] and quest[13] == rec[1] else 10 if quest[12] != answ[8] and quest[13] == rec[0] and quest[14] == answ[8] else 0 
  tickpts9 = True if s9 == 10 else False

  quest[16] = data['r_10'] if quest[15] != answ[9] else quest[16] == ""
  quest[17] = data['q_a10'] if quest[15] != answ[9] and quest[16] == rec[0] else quest[17] == ""
  s10 = 10 if quest[15] == answ[9] else 0 if quest[15] != answ[9] and quest[16] == rec[1] else 10 if quest[15] != answ[9] and quest[16] == rec[0] and quest[17] == answ[9] else 0 
  tickpts10 = True if s10 == 10 else False

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

    'select6': quest[5] if quest[5] == answ[5] else quest[5] if quest[5] != answ[5] and quest[6] == rec[1] else quest[7] if quest[5] != answ[5] and quest[6] == rec[0] and quest[7] == answ[5] else quest[7],
    'correct6': answ[5],  

    'select7': quest[7], 
    'correct7': answ[6],  

    'select8': quest[9] if quest[9] == answ[7] else quest[9] if quest[9] != answ[7] and quest[10] == rec[1] else quest[11] if quest[9] != answ[7] and quest[10] == rec[0] and quest[11] == answ[7] else quest[11],
    'correct8': answ[7],    

    'select9': quest[12] if quest[12] == answ[8] else quest[12] if quest[12] != answ[8] and quest[13] == rec[1] else quest[14] if quest[12] != answ[8] and quest[13] == rec[0] and quest[14] == answ[8] else quest[14], 
    'correct9': answ[8],    

    'select10': quest[15] if quest[15] == answ[9] else quest[15] if quest[15] != answ[9] and quest[16] == rec[1] else quest[17] if quest[15] != answ[9] and quest[16] == rec[0] and quest[17] == answ[9] else quest[17], 
    'correct10': answ[9],    

    'tick1': '&#9989;' if tickpts1 == True else '&#10060;',
    'tick2': '&#9989;' if tickpts2 == True else '&#10060;',
    'tick3': '&#9989;' if tickpts3 == True else '&#10060;',
    'tick4': '&#9989;' if tickpts4 == True else '&#10060;',
    'tick5': '&#9989;' if tickpts5 == True else '&#10060;',   
    'tick6': '&#9989;' if tickpts6 == True else '&#10060;',
    'tick7': '&#9989;' if tickpts7 == True else '&#10060;', 
    'tick8': '&#9989;' if tickpts8 == True else '&#10060;', 
    'tick9': '&#9989;' if tickpts9 == True else '&#10060;', 
    'tick10': '&#9989;' if tickpts10 == True else '&#10060;',

    'pts1': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts1 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
    'pts2': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts2 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
    'pts3': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts3 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
    'pts4': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts4 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
    'pts5': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts5 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
    'pts6': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts6 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
    'pts7': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts7 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
    'pts8': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts8 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
    'pts9': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts9 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
    'pts10': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts10 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
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
  # Same callouts as in the quest[] list
  html = toHTML({
    "q_a1": "Basketball",
    "q_a2": "Shaping leaders",
    "q_a3": "A troop",
    "q_a4": "A Mechanic",
    "q_a5": "Brisbane", 
    "q_a6r": "14th", 
    "": "",      
    "": "",
    "q_a7": "Lachlan River", 
    "q_a8r": "Fear of needles", 
    "": "", 
    "": "",
    "q_a9r": "A banana", 
    "": "", 
    "": "",
    "q_a10r": "8", 
    "": "", 
    "": "", 
  })
  
  with open('out.html', 'w') as f:
    f.write(html)
