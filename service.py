import qi
import os
import json
import uuid
import datetime
import result # importing result.py file
import base64

class SurveyService:
    def __init__(self):
      if (not os.path.exists('/home/nao/data/survey')):
        os.makedirs('/home/nao/data/survey')

    def save(self, data):
        '''
        Saves survey data to unique json files
        '''
        now = datetime.datetime.now()
        data = json.loads(data)

        keys = []

        if 'follow_up' in data and data['follow_up']['is_interested'] != '0':
          fname = '-'.join(['follow_up', str(uuid.uuid1())]) + '.json'
          keys.append(fname)

          with open(os.path.join('/home/nao/data/survey', fname), 'w') as f:
            f.write(json.dumps(data['follow_up'], indent=4, sort_keys=True) + '\n')

        if 'prize_draw' in data and data['prize_draw']['is_interested'] != '0':
          fname = '-'.join(['prize-draw', str(uuid.uuid1())]) + '.json'

          with open(os.path.join('/home/nao/data/survey', fname), 'w') as f:
            f.write(json.dumps(data['prize_draw'], indent=4, sort_keys=True) + '\n')

        if 'prize_draw' in data:
          del data['prize_draw']
        
        if 'follow_up' in data:
          del data['follow_up']

        ## Save santized responses
        fname = '-'.join(['response', str(now.year), str(now.month), str(now.day), str(uuid.uuid1())]) + '.json'
        keys.append(fname)
        
        with open(os.path.join('/home/nao/data/survey', fname), 'w') as f:
            f.write(json.dumps(data, indent=4, sort_keys=True) + '\n')

        if len(keys) > 1:
          with open(os.path.join('/home/nao/data/Paulo', '-'.join(['key', str(uuid.uuid1())]) + '.json'), 'w') as f: # Change directory to save files on specific folder
            f.write(base64.b64encode(json.dumps(keys, indent=4) + '\n'))

        return True

    # Send data from result.py file to the html folder
    def print_data(self, data):
      '''
      Sends survey data to print queue
      '''
      html = self.get_html(data)
      result.send(html)

    def get_html(self, data, sections=None): # sections callout refers to the same sections as the template.html file
      return result.toHTML(json.loads(data), sections)

def main():
    app = qi.Application()
    app.start()
    session = app.session

    service = SurveyService() # print_data is part of the class
    session.registerService('SurveyService', service)
    app.run()

if __name__ == '__main__':
    main()