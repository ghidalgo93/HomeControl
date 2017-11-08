class Lights:
    def __init__(self,payload):
        ''' Constructor for this class. '''
        self.payload = payload

    def handle_lights(self):
        if (('on' in self.payload['lights']) and (self.payload['lights']['on'] == True)):
            print ("turning lights on")
        if (('on' in self.payload['lights']) and (self.payload['lights']['on'] == False)):
            print ("turning lights off")
