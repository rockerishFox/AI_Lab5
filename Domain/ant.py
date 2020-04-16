from random import *
from Domain.problemParams import ProblemParams
from Domain.acoParams import ACOParams

class Ant:
    def __init__(self, problemParam: ProblemParams, acoParams: ACOParams):
        self.problemParam = problemParam
        self.acoParam = acoParams
        self.representation = [randint(0, self.problemParam.nrNodes - 1)]
        self.length = 0
        self.pheromoneLevel = [[0 for _ in range(self.problemParam.nrNodes)] for _ in range(self.problemParam.nrNodes)]

    def chooseNext(self):
        options = []
        total = 0.0
        for cityIndex in range(self.problemParam.nrNodes):
            options.append(0)
            if cityIndex not in self.representation:
                if self.problemParam.feromons[self.representation[-1]][cityIndex] == 0:
                    t = 1
                else:
                    t = self.problemParam.feromons[self.representation[-1]][cityIndex] ** self.acoParam.alpha

                # formula (din curs) dupa care se alege urmatorul oras
                n = (1 / self.problemParam.network[self.representation[-1]][cityIndex])**self.acoParam.beta
                options[-1] = t*n
                total += options[-1]

        q = random()
        # probabilitatea dupa care se alege orasul cel mai "optim"
        if q < self.acoParam.pseudo:
            max = 0
            chosenCity = 0
            for index in range(self.problemParam.nrNodes):
                if options[index] > max:
                    max = options[index]
                    chosenCity = index
        else:
            probs = []
            cityList = []
            weights = []
            for j in range(self.problemParam.nrNodes):
                if options[j] != 0:
                    probs.append([j, options[j] / total])
                    cityList.append(j)
                    weights.append(options[j] / total)

            chosenCity = choices(cityList, weights=weights)[0]

        # marcam orasul ca vizitat si facem modificarile necesare
        self.representation.append(chosenCity)
        self.pheromoneLevel[self.representation[-2]][self.representation[-1]] = 1
        self.pheromoneLevel[self.representation[-1]][self.representation[-2]] = 1
        self.length += self.problemParam.network[self.representation[-2]][self.representation[-1]]

    def goHome(self):
        # ne intoarcem la primul oras (de unde am plecat)
        self.representation.append(self.representation[0])
        self.pheromoneLevel[self.representation[-2]][self.representation[-1]] = 1
        self.pheromoneLevel[self.representation[-1]][self.representation[-2]] = 1
        self.length += self.problemParam.network[self.representation[-2]][self.representation[-1]]

    def __str__(self):
        # return "Ant: " + str(self.representation) + " Length: " + str(self.length)
        return " Length: " + str(self.length)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.representation == other.representation