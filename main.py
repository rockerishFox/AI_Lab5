from utils import *
from random import *
from Domain.acoParams import ACOParams
from Domain.problemParams import ProblemParams
from Domain.aco import ACO
from Domain.ant import Ant


def main():
    files = ['input/easy1.txt', 'input/easy2.txt', 'input/easy3.txt', 'input/mediumF.txt', 'input/hardE.txt']
    input_file = files[3]

    graph = read_graph_from_file(input_file)  # cititre normala
    # graph = read_graph_from_file_with_coordinates(files[4]) # cititre euclid

    # ACOParams ( nr furnici , nr iteratii, coeficient 1, coeficient 2, constanta evaporare, constanta alegere oras nou)
    acoParams = ACOParams(50, 100, 1, 10, 0.2, 0.6)
    # ProblemParams ( matricea de adiacenta, nr noduri, matricea cu feromoni
    problemParams = ProblemParams(graph, len(graph), [[0] * len(graph)] * len(graph))

    generalBest = Ant(problemParams, acoParams)
    bestiteration = 0

    aco = ACO(acoParams, problemParams)

    firstStep = True

    for gen in range(acoParams.noOfIterations):
        aco.initialize(problemParams)

        for step in range(problemParams.nrNodes - 1):
            # fiecare furnica face o mutare/un pas
            aco.ants_one_step()

        aco.ants_go_home()
        problemParams.feromons = aco.update_feromons()
        bestAnt = aco.best_ant()

        print('Generatia: ' + str(gen) + ' cu reprezentarea ' + str(bestAnt.representation) + ' si costul ' + str(
            bestAnt.length))

        if firstStep:
            firstStep = False
            generalBest = bestAnt
            bestiteration = gen
        elif bestAnt.length <= generalBest.length:
            generalBest = bestAnt
            bestiteration = gen


    # dinamizare = > alegem doua orase random si marcam drumulor dintre ele ca nevizitat (asta la un set de pasi)
    # index1 = randint(0, problemParams.nrNodes-1)
    # index2 = randint(0, problemParams.nrNodes-1)
    #
    # varianta lui Pascu : in for 
    # if dynamic:
    #     for a in range(problemParams.nrNodes):
    #         for b in range(problemParams.nrNodes):
    #             if problemParams.pheroNetwork[a][b] > acoParams.maxTraffic:
    #                 if doubledNetwork[a][b] == False:
    #                     problemParams.network[a][b] *= 2
    #                     doubledNetwork[a][b] = True
    #                     problemParams.pheroNetwork[a][b] = 1
    #     if iteration == acoParams.noOfIterations / 2:
    #         for a in range(problemParams.nrNodes):
    #             for b in range(problemParams.nrNodes):
    #                 if doubledNetwork[a][b] == True:
    #                     problemParams.network[a][b] /= 2
    #                 else:
    #                     doubledNetwork[a][b] = True


    print('\033[1;34;48m Generatia ' + str(bestiteration) + ' cu reprezentarea ' + str(
        generalBest.representation) + ' si costul ' + str(generalBest.length))


main()
