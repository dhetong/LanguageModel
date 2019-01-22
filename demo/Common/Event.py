class LogEvent:
    'a class for log Event'
    #Log events are represented as tokens, which are stored as lists
    #index is the index of the log event in log event table, stored as a integer
    #timestamp is the timestamp of the event
    def _init_(self, event, index, timestamp):
        self.event = event;
        self.index = index;
        self.timestamp = timestamp;

    def getIndex(self):
        return self.index;

    def getTime(self):
        return self.timestamp;

    def getEvent(self):
        return self.event;