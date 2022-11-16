class Counter(object):
    def __init__(self):
        self.count = 0
    
    def click(self):
        self.count += 1
    
    def getValue(self):
        print(self.count)
    
    def setValue(self, new_value):
        self.count = new_value

    def reset(self):
        self.count = 0
    

tally = Counter()
tally.click()
tally.getValue()
tally.setValue(5)
tally.getValue()