import demo.Common.Event

class EventTable:
    'Read and Write the Event Table'
    #The path of the file storing log event table
    def __init__(self):
        self.filePath = 'demo/RelevantFiles/EventTable.txt';

    def _TransformFormat(self):
    #TODO: transfrom the log events' format of other log parsing method into our log event format
        pass

    def ReadEventByID(self, index):
    #TODO: read the log event from the event table according to the ID of log event
        pass