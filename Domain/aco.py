from Domain.ant import Ant
from Domain.problemParams import ProblemParams
from Domain.acoParams import ACOParams


class ACO:
    def __init__(self, acoParam: ACOParams, problemParam: ProblemParams):
        self.acoParam = acoParam
        self.problemParam = problemParam
        self.population = []

    def initialize(self, problemParam):
        self.population = []
        self.problemParam = problemParam
        for _ in range(self.acoParam.noOfAnts):
            ant = Ant(self.problemParam, self.acoParam)
            self.population.append(ant)

    def ants_one_step(self):
        for ant in self.population:
            ant.chooseNext()

    def ants_go_home(self):
        for ant in self.population:
            # le spunem furnicilor sa se intoarca in orasul de start
            ant.goHome()

    def update_feromons(self):
        # pentru fiecare oras actualizam feromonii (tinand cont si de drumul furnicilor si de evaporare)
        for i in range(self.problemParam.nrNodes):
            for j in range(self.problemParam.nrNodes):
                newPhero = 0
                for ant in self.population:
                    if ant.pheromoneLevel[i][j] == 1:
                        newPhero += 1 / ant.length
                self.problemParam.feromons[i][j] = (1 - self.acoParam.evaporation) * self.problemParam.feromons[i][j] + newPhero
        return self.problemParam.feromons

    def best_ant(self):
        best = self.population[0]
        for ant in self.population:
            if ant.length < best.length:
                best = ant
        return best

    def worst_ant(self):
        worst = self.population[0]
        for ant in self.population:
            if ant.length > worst.length:
                worst = ant
        return worst
