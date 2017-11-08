class Plants:
    def __init__(self, payload):
        ''' Constructor for this class. '''
        self.payload = payload

    def handle_plants(self):
        if (('water' in self.payload['plants'] ) and (self.payload['plants']['water'] == True)):
            print ("watering plants now") #water the plants
        if (('moisture' in self.payload['plants']) and (self.payload['plants']['moisture'] == True)):
            print ("checking moisture") #check the moisture
            print ("reccording moisture") #reccord the moisture
