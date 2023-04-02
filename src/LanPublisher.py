import requests
import json
from env import API_PATH, serial, IS_LOCAL
from .Publisher import Publisher
from .Status import Status


class LanPublisher(Publisher):
    def __init__(self, status: Status):
        Publisher.__init__(self, status)

    def publish_status(self, args: list | None = None) -> None:
        try:
            r = requests.get(
                API_PATH,
                headers={'Authorization': serial()}
            )
            content = r.content.decode('utf-8')
            data = json.loads(content)
            r.close()
            if data['alarm']:
                alarm = data['alarm']
                if alarm == 'Yes':
                    self.notify(True)
                else:
                    self.notify(False)
        except Exception as e:
            if IS_LOCAL:
                print(e)
            print('Something went wrong')
            pass

