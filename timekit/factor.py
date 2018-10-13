class TimeKitFactor:

    def __init__(self, timekit):
        self.timekit = timekit

    def get(self, timestr):
        return self.timekit.fromtimestr(timestr)

    def now(self):
        return self.timekit.now()

    def utimekitnow(self):
        return self.timekit.utimekitnow()
