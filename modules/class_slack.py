""""
CLASS SLACK SEND ERROR TO CHANNEL #DEVOPS
"""

import requests

class Slack:
    def __init__(self,report):
        webhook = 'https://hooks.slack.com/services/<TOKEN>'
        response = requests.post(webhook, json=report, headers={'Content-Type': 'application/json'})
        if response.ok:
            json_data = response.text
            self.result = json_data
