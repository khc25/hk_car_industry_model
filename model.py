import numpy as np

class Model:
    def __init__(self, new, old):
        self.new = new
        self.old = old
        self.price_ratio = 0
        self.FirstChange = 0
        self.SecondChange = 0
        self.Z = 0
        self.corr = 0
        self.sd = 0
        self.ma = 0


    def getFirstChange( self, new, old):
        result = (new-old)/100
        return result

    def getSecondChange(self, new, old):
        result = (new-old)/100
        return result

    def getPriceRatio(self, first, second):
      
        if first > second:
            return second/first
        elif first == second:
            return 1
        else:
            return first/second
        

    def getZ(self):
        return (self.price_ratio - self.ma) / self.sd
    
    def getCorr(self, data_first, data_second):
        return np.corrcoef(data_first, data_second)

    def getSD(self, data):
        return np.std(data, ddof = 1)

    def getMA(self, data):
        return np.mean(data)

