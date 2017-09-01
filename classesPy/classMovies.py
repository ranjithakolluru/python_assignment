
class movies:
    def __init__(self,moviename,runtime,Genres,lang):
        self.moviename=moviename
        self.runtime=runtime
        self.Genres=Genres
        self.lang=lang
    
    def famous(self):
        if self.lang=='Telugu':
            print "Ultimate BlockBuster"
        else:
            print "Marvel Movie"
    def croresTurnover(self):
        if self.moviename=='Bahubali':
            print "croresTurnover"
        else:
            print "High BudgetMovie"
        
        
    def displaymovies(self):
        print "moviename:",self.moviename
        print "runtime:",self.runtime
        print "Genres:",self.Genres
        print "language:",self.lang