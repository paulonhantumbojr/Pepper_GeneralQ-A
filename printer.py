import io
import requests

def toHTML(data, pages=None): #data variable represents the inline 'name' elements of the different <tags> in index.html 
  quest = [
    data['q_a1'], #0 (Question 1)

    data['q_a2'], #1 (Question 2)

    data['q_a3'], #2 (Question 3)

    data['q_a4'], #3 (Question 4)

    data['q_a5'], #4 (Question 5)

    data['q_a6r'], #5 (Question 6 prompt)
    data['r_6'], #6 (Question 6 recommendation) 

    data['q_a7'], #7 (Question 7)

    data['q_a8r'], #8 (Question 8 prompt)
    data['r_8'], #9 (Question 8 recommendation)

    data['q_a9r'], #10 (Question 9 prompt)
    data['r_9'], #11 (Question 9 recommendation)

    data['q_a10r'], #12 (Question 10 prompt)
    data['r_10'], #13 (Question 10 recommendation)

    int(data['q_a11r']), #14 (Question 11 prompt)
    data['r_11'], #15 (Question 11 recommendation)

    int(data['q_a12r']), #16 (Question 12 prompt)
    data['r_12'] , #17 (Question 12 recommendation)

    int(data['q_a13r']), #18 (Question 13 prompt)
    data['r_13'], #19 (Question 13 recommendation)

    int(data['q_a14r']), #20 (Question 14 prompt)
    data['r_14'], #21 (Question 14 recommendation)

    int(data['q_a15r']), #22 (Question 15 prompt)
    data['r_15'], #23 (Question 15 recommendation)
  ]

  answ = [
    "An octagon", #0 (Answer to Q1)
    "I am still learning", #1 (Answer to Q2)
    "Canberra", #2 (Answer to Q3)
    "Red", #3 (Answer to Q4)
    "A Civil Engineer", #4 (Answer to Q5)
    "14th", #5 (Answer to Q6) 
    "Pacific", #6 (Answer to Q7)
    "Fear of dogs", #7 (Answer to Q8)
    "An orange", #8 (Answer to Q9)
    "11", #9 (Answer to Q10)
    16, #10 (Answer to Q11)
    15, #11 (Answer to Q12)
    15, #12 (Answer to Q13)
    9, #13 (Answer to Q14)
    9, #14 (Answer to Q15)
  ]

  rec = [
    "Keep my selected response", #0 (Keep user selection)
    "Change your response to match my recommendation", #1 (Change to robot's recommendation)
  ]

  suggest = [
    "18th", #0 (For Question 6)
    "Fear of needles", #1 (For Question 8)
    "An apple", #2 (For Question 9)
    "10", #3 (For Question 10)
    10, #4 (For Question 11)
    12, #5 (For Question 12)
    9, #6 (For Question 13)
    8, #7 (For Question 14)
    10, #8 (For Question 15)
  ]

  # Question 1
  s1 = 10 if quest[0] == answ[0] else 0 
  tickpts1 = True if s1 == 10 else False

  # Question 2
  s2 = 10 if quest[1] == answ[1] else 0 
  tickpts2 = True if s2 == 10 else False

  # Question 3
  s3 = 10 if quest[2] == answ[2] else 0 
  tickpts3 = True if s3 == 10 else False

  # Question 4
  s4 = 10 if quest[3] == answ[3] else 0
  tickpts4 = True if s4 == 10 else False

  # Question 5
  s5 = 10 if quest[4] == answ[4] else 0 
  tickpts5 = True if s5 == 10 else False

  # Question 6
  s6 = 10 if quest[5] == answ[5] and quest[6] == rec[0] else 0 if quest[5] == answ[5] and quest[6] == rec[1] else 10 if quest[5] != answ[5] and quest[6] == rec[1] else 0 if quest[5] != answ[5] and quest[6] == rec[0] else 0
  tickpts6 = True if s6 == 10 else False

  # Question 7
  s7 = 10 if quest[7] == answ[6] else 0 
  tickpts7 = True if s7 == 10 else False

  # Question 8
  s8 = 10 if quest[8] == answ[7] and quest[9] == rec[0] else 0 if quest[8] == answ[7] and quest[9] == rec[1] else 10 if quest[8] != answ[7] and quest[9] == rec[1] else 0 if quest[8] != answ[7] and quest[9] == rec[0] else 0
  tickpts8 = True if s8 == 10 else False

  # Question 9
  s9 = 10 if quest[10] == answ[8] and quest[11] == rec[0] else 0 if quest[10] == answ[8] and quest[11] == rec[1] else 10 if quest[10] != answ[8] and quest[11] == rec[1] else 0 if quest[10] != answ[8] and quest[11] == rec[0] else 0 
  tickpts9 = True if s9 == 10 else False

  # Question 10
  s10 = 10 if quest[12] == answ[9] and quest[13] == rec[0] else 0 if quest[12] == answ[9] and quest[13] == rec[1] else 10 if quest[12] != answ[9] and quest[13] == rec[1] else 0 if quest[12] != answ[9] and quest[13] == rec[0] else 0 
  tickpts10 = True if s10 == 10 else False

  # Question 11
  s11 = 10 if quest[14] == answ[10] and quest[15] == rec[0] else 0 if quest[14] == answ[10] and quest[15] == rec[1] else 10 if quest[14] != answ[10] and quest[15] == rec[1] else 0 if quest[14] != answ[10] and quest[15] == rec[0] else 0
  tickpts11 = True if s11 == 10 else False

  # Question 12
  s12 = 10 if quest[16] == answ[11] and quest[17] == rec[0] else 0 if quest[16] == answ[11] and quest[17] == rec[1] else 10 if quest[16] != answ[11] and quest[17] == rec[1] else 0 if quest[16] != answ[11] and quest[17] == rec[0] else 0 
  tickpts12 = True if s12 == 10 else False

  # Question 13
  s13 = 10 if quest[18] == answ[12] and quest[19] == rec[0] else 0 if quest[18] == answ[12] and quest[19] == rec[1] else 10 if quest[18] != answ[12] and quest[19] == rec[1] else 0 if quest[18] != answ[12] and quest[19] == rec[0] else 0 
  tickpts13 = True if s13 == 10 else False

  # Question 14
  s14 = 10 if quest[20] == answ[13] and quest[21] == rec[0] else 0 if quest[20] == answ[13] and quest[21] == rec[1] else 10 if quest[20] != answ[13] and quest[21] == rec[1] else 0 if quest[20] != answ[13] and quest[21] == rec[0] else 0 
  tickpts14 = True if s14 == 10 else False

  # Question 15
  s15 = 10 if quest[22] == answ[14] and quest[23] == rec[0] else 0 if quest[22] == answ[14] and quest[23] == rec[1] else 10 if quest[22] != answ[14] and quest[23] == rec[1] else 0 if quest[22] != answ[14] and quest[23] == rec[0] else 0 
  tickpts15 = True if s15 == 10 else False

  finsc = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12 + s13 + s14 + s15

  replacements = {

    # Final Score
    'finsc': finsc,

    # Question 1
    'select1': quest[0], 
    'correct1': answ[0],

    # Question 2
    'select2': quest[1], 
    'correct2': answ[1],

    # Question 3
    'select3': quest[2], 
    'correct3': answ[2],

    # Question 4
    'select4': quest[3], 
    'correct4': answ[3],

    # Question 5
    'select5': quest[4], 
    'correct5': answ[4],

    # Question 6
    'select6': quest[5] if quest[5] == answ[5] and quest[6] == rec[0] else suggest[0] if quest[5] == answ[5] and quest[6] == rec[1] else answ[5] if quest[5] != answ[5] and quest[6] == rec[1] else quest[5] if quest[5] != answ[5] and quest[6] == rec[0] else "undefined",
    'correct6': answ[5],  

    # Question 7
    'select7': quest[7], 
    'correct7': answ[6],  

    # Question 8
    'select8': quest[8] if quest[8] == answ[7] and quest[9] == rec[0] else suggest[1] if quest[8] == answ[7] and quest[9] == rec[1] else answ[7] if quest[8] != answ[7] and quest[9] == rec[1] else quest[8] if quest[8] != answ[7] and quest[9] == rec[0] else "N/A",
    'correct8': answ[7],    

    # Question 9
    'select9': quest[10] if quest[10] == answ[8] and quest[11] == rec[0] else suggest[2] if quest[10] == answ[8] and quest[11] == rec[1] else answ[8] if quest[10] != answ[8] and quest[11] == rec[1] else quest[10] if quest[10] != answ[8] and quest[11] == rec[0] else "N/A", 
    'correct9': answ[8],    

    # Question 10
    'select10': quest[12] if quest[12] == answ[9] and quest[13] == rec[0] else suggest[3] if quest[12] == answ[9] and quest[13] == rec[1] else answ[9] if quest[12] != answ[9] and quest[13] == rec[1] else quest[12] if quest[12] != answ[9] and quest[13] == rec[0] else "N/A", 
    'correct10': answ[9],    

    # Question 11
    'select11': quest[14] if quest[14] == answ[10] and quest[15] == rec[0] else suggest[4] if quest[14] == answ[10] and quest[15] == rec[1] else answ[10] if quest[14] != answ[10] and quest[15] == rec[1] else quest[14] if quest[14] != answ[10] and quest[15] == rec[0] else "N/A", 
    'correct11': answ[10],

    # Question 12
    'select12': quest[16] if quest[16] == answ[11] and quest[17] == rec[0] else suggest[5] if quest[16] == answ[11] and quest[17] == rec[1] else answ[11] if quest[16] != answ[11] and quest[17] == rec[1] else quest[16] if quest[16] != answ[11] and quest[17] == rec[0] else "N/A",
    'correct12': answ[11],

    # Question 13
    'select13': quest[18] if quest[18] == answ[12] and quest[19] == rec[0] else suggest[6] if quest[18] == answ[12] and quest[19] == rec[1] else answ[12] if quest[18] != answ[12] and quest[19] == rec[1] else quest[18] if quest[18] != answ[12] and quest[19] == rec[0] else "N/A",
    'correct13': answ[12],

    # Question 14
    'select14': quest[20] if quest[20] == answ[13] and quest[21] == rec[0] else suggest[7] if quest[20] == answ[13] and quest[21] == rec[1] else answ[13] if quest[20] != answ[13] and quest[21] == rec[1] else quest[20] if quest[20] != answ[13] and quest[21] == rec[0] else "N/A",
    'correct14': answ[13],

    # Question 15
    'select15': quest[22] if quest[22] == answ[14] and quest[23] == rec[0] else suggest[8] if quest[22] == answ[14] and quest[23] == rec[1] else answ[14] if quest[22] != answ[14] and quest[23] == rec[1] else quest[22] if quest[22] != answ[14] and quest[23] == rec[0] else "N/A",
    'correct15': answ[14],

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
    'tick11': '&#9989;' if tickpts11 == True else '&#10060;',
    'tick12': '&#9989;' if tickpts12 == True else '&#10060;',
    'tick13': '&#9989;' if tickpts13 == True else '&#10060;',
    'tick14': '&#9989;' if tickpts14 == True else '&#10060;',
    'tick15': '&#9989;' if tickpts15 == True else '&#10060;',

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
    'pts11': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts11 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
    'pts12': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts12 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
    'pts13': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts13 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
    'pts14': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts14 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
    'pts15': '<span style="color:green; font-weight:bold;">+10pts</span>' if tickpts15 == True else '<span style="color:red; font-weight:bold;">0pts</span>',
  }

  with open('template.html', 'U') as f:
    template = f.read()

    for key in replacements:
      template = template.replace('{' + key + '}', str(replacements[key]))

  return template

def send(html):
  f = io.StringIO(unicode(html, 'UTF-8'))
  files = {'file': f}

  requests.post('http://cloudvis.qut.edu.au:8082',files=files)

if __name__ == '__main__':
  html = toHTML({
    "q_a1": "A hexagon",
    
    "q_a2": "Shaping leaders",

    "q_a3": "Canberra",

    "q_a4": "Blue",

    "q_a5": "A Mechanic", 

    "q_a6r": "14th", 
    "r_6": "Change your response to match my recommendation",      

    "q_a7": "Atlantic", 

    "q_a8r": "Fear of needles", 
    "r_8": "Keep my selected response", 

    "q_a9r": "A banana", 
    "r_9": "Change your response to match my recommendation", 

    "q_a10r": "8", 
    "r_10": "Keep my selected response", 

    "q_a11r": "4", 
    "r_11": "Change your response to match my recommendation", 

    "q_a12r": "6", 
    "r_12": "Keep my selected response", 

    "q_a13r": "10", 
    "r_13": "Change your response to match my recommendation", 

    "q_a14r": "14", 
    "r_14": "Keep my selected response", 
    
    "q_a15r": "12", 
    "r_15": "Change your response to match my recommendation", 
  })
  
  with open('out.html', 'w') as f:
    f.write(html)