from __future__ import print_function
from inputs import get_gamepad


class PlaystationService:

    def getInformation(self):
        events = get_gamepad()
        for event in events:
            print(event.ev_type, event.code, event.state)
