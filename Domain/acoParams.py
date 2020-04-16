
class ACOParams:
    def __init__(self, noAnts, noIterations, alpha, beta, evaporation, pseudo):
        self.noOfAnts = noAnts
        self.noOfIterations = noIterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation = evaporation
        self.pseudo = pseudo