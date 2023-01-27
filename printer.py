import io
import requests

def toHTML(data, pages=None): #data variable represents the 'name' elements in index.html 
  quest = [
    data['q_a1'], #0 (Question 1)
    data['q_a2'], #1 (Question 2)
    data['q_a3'], #2 (Question 3)
    data['q_a4'], #3 (Question 4)
    data['q_a5'], #4 (Question 5)
    data['q_a6r'], #5 (Question 6 prior-rec)
    "", #6 data['q_a6'] (Question 6 after-rec)
    data['q_a7'], #7 (Question 7)
    data['q_a8r'], #8 (Question 8 prior-rec)
    data['q_a8'], #9 (Question 8 after-rec)
    data['q_a9r'], #10 (Question 9 prior-rec)
    data['q_a9'], #11 (Question 9 after-rec)
    data['q_a10r'], #12 (Question 10 prior-rec)
    data['q_a10'], #13 (Question 10 after-rec)
    "", #14 data['r_6'] (Y/N rec screen)
  ]

  # answ list holds the 'value' elements in the index.html file
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

# If the associated name of the answer corresponds to the value provided then increment 10pts
  s1 = 10 if quest[0] == answ[0] else 0 
  s2 = 10 if quest[1] == answ[1] else 0 
  s3 = 10 if quest[2] == answ[2] else 0 
  s4 = 10 if quest[3] == answ[3] else 0
  s5 = 10 if quest[4] == answ[4] else 0 
  # s6 = 10 if quest[5] == answ[5] or quest[6] == answ[5] else 0 (Original implementation)

  # NESTED IFs implementation
  # First Use Case: User gets the first answer correct
  if quest[5] == answ[5]: # If the chosen answer is correct (in the first attempt)
    s6 = 10  # Add 10pts to the score
    select6r = True # Trigger the selected answer (Line 97)
    tick6 = True # Trigger the tick (Line 122)

  # Second Use Case: User gets the first answer incorrect (subcases below)
  elif quest[5] != answ[5]: # Else if the chosen answer is incorrect in the first attempt
    quest[14] = data['r_6'] # Initialise the empty string (at line 20) to hold Y/N user prompts

    # Subcase 1: User denies the recommendation
    if quest[14] == rec[1]: # When the user selects 'No'
      s6 = 0 # Add 0pts to the score

    # Subcase 2: User accepts the recommendation (further subcases below)
    elif quest[14] == rec[0]: # When the user selects 'Yes'
      quest[6] = data['q_a6'] # Initialise the empty string (at line 12) to hold the answer to Question 6

      # Subcase 3: User gets the recommendation correct
      if quest[6] == answ[5]: # When the user selects the right answer (from the recommended)
        s6 = 10 # Add 10pts to the score
        select6r = True # Trigger the selected answer (Line 97)
        tick6 = True # Trigger the tick (Line 122)

      # Subcase 4: User gets the recommendation incorrect
      else: # When the user selects the wrong answer (from the recommended)
        s6 = 0 # Award no points

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

    # 'select6': quest[5] if quest[5] == answ[5] else quest[6],
    'select6': quest[5] if select6r == True else data['q_a6'],
    'correct6': answ[5],  

    'select7': quest[7], 
    'correct7': answ[6],  

    'select8': quest[8] if quest[8] == answ[7] else quest[9],
    # 'select8': quest[8] if select8r == True else data['q_a8'],
    'correct8': answ[7],    

    'select9': quest[10] if quest[10] == answ[8] else quest[11], 
    # 'select9': quest[10] if select9r == True else data['q_a9'],
    'correct9': answ[8],    

    'select10': quest[12] if quest[12] == answ[9] else quest[13], 
    # 'select10': quest[12] if select10r == True else data['q_a10'],
    'correct10': answ[9],    

    'tick1': '&#9989;' if quest[0] == answ[0] else '&#10060;',
    'tick2': '&#9989;' if quest[1] == answ[1] else '&#10060;',
    'tick3': '&#9989;' if quest[2] == answ[2] else '&#10060;',
    'tick4': '&#9989;' if quest[3] == answ[3] else '&#10060;',
    'tick5': '&#9989;' if quest[4] == answ[4] else '&#10060;',   

    # 'tick6': '&#9989;' if quest[5] == answ[5] or quest[6] == answ[5] else '&#10060;',  
    'tick6': '&#9989;' if tick6 == True else '&#10060;',

    'tick7': '&#9989;' if quest[7] == answ[6] else '&#10060;', 

    'tick8': '&#9989;' if quest[8] == answ[7] or quest[9] == answ[7] else '&#10060;', 
    # 'tick8': '&#9989;' if tick8 == True else '&#10060;',
    'tick9': '&#9989;' if quest[10] == answ[8] or quest[11] == answ[8] else '&#10060;', 
    # 'tick9': '&#9989;' if tick9 == True else '&#10060;',
    'tick10': '&#9989;' if quest[12] == answ[9] or quest[13] == answ[9] else '&#10060;',  
    # 'tick10': '&#9989;' if tick10 == True else '&#10060;',
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
    "": "", # "q_a6": "11th", # Declare the empty response for the recommendation if user gets the question right on the first attempt     
    "q_a7": "Lachlan River", 
    "q_a8r": "Fear of needles", 
    "q_a8": "Fear of heights", 
    "q_a9r": "A banana", 
    "q_a9": "An apple", 
    "q_a10r": "8", 
    "q_a10": "10",
    "":"", # Declare the Y/N variable
  })
  
  with open('out.html', 'w') as f:
    f.write(html)