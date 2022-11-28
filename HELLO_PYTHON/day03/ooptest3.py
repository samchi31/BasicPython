class Xi:
    def __init__(self):
        self.index_look = 10
        
    def corona(self):
        self.index_look -= 1
        
class Trump:
    def __init__(self):
        self.money = 2
        
    def youfire(self):
        self.money += 1
        
class Kim:
    def __init__(self):
        self.nuclear = 20
        
    def aoji(self):
        self.nuclear += 2
        
class Park(Xi,Trump,Kim):
    def __init__(self):
        # super().__init__()
        Xi.__init__(self)
        Trump.__init__(self)
        Kim.__init__(self)
        
        
        
if __name__ == '__main__':
    insu = Park()
    
    print(insu.index_look)
    print(insu.money)
    print(insu.nuclear)
    
    insu.corona()
    insu.youfire()
    insu.aoji()
    
    print(insu.index_look)
    print(insu.money)
    print(insu.nuclear)