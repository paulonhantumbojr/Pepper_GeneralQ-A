import qi
import os
import json
import uuid
import datetime
import printer
import base64

class SurveyService: 
    def __init__(self):
      if (not os.path.exists('/home/nao/data/health_survey')):
        os.makedirs('/home/nao/data/health_survey')

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

          with open(os.path.join('/home/nao/data/health_survey', fname), 'w') as f:
            f.write(json.dumps(data['follow_up'], indent=4, sort_keys=True) + '\n')

        if 'prize_draw' in data and data['prize_draw']['is_interested'] != '0':
          fname = '-'.join(['prize-draw', str(uuid.uuid1())]) + '.json'

          with open(os.path.join('/home/nao/data/health_survey', fname), 'w') as f:
            f.write(json.dumps(data['prize_draw'], indent=4, sort_keys=True) + '\n')

        if 'prize_draw' in data:
          del data['prize_draw']
        
        if 'follow_up' in data:
          del data['follow_up']

        ## Save santized responses
        fname = '-'.join(['response', str(now.year), str(now.month), str(now.day), str(uuid.uuid1())]) + '.json'
        keys.append(fname)
        
        with open(os.path.join('/home/nao/data/health_survey', fname), 'w') as f:
            f.write(json.dumps(data, indent=4, sort_keys=True) + '\n')

        if len(keys) > 1:
          with open(os.path.join('/home/nao/data/Paulo', '-'.join(['key', str(uuid.uuid1())]) + '.json'), 'w') as f:
            f.write(base64.b64encode(json.dumps(keys, indent=4) + '\n'))

        return True

    def print_data(self, data):
      '''
      Sends survey data to print queue
      '''
      html = self.get_html(data)
      printer.send(html)

    def get_html(self, data, sections=None):
      return printer.toHTML(json.loads(data), sections)

def main():
    app = qi.Application()
    app.start()
    session = app.session

    service = SurveyService()
    session.registerService('HealthAssessmentService', service)
    app.run()

if __name__ == '__main__':
    main()