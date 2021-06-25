import random
import time

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution

def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i - 1]][solution[i]]
    return routeLength

def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours

def getBestNeighbour(tsp, neighbours):
    bestRouteLength = routeLength(tsp, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(tsp, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    return bestNeighbour, bestRouteLength

def hillClimbing(tsp):
    currentSolution = randomSolution(tsp)
    currentRouteLength = routeLength(tsp, currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tsp, neighbours)

    return currentSolution, currentRouteLength
def problemGenerator(nCities):
    tsp = []
    for i in range(nCities):
        distances = []
        for j in range(nCities):
            if j == i:
                distances.append(0)
            elif j < i:
                distances.append(tsp[j][i])
            else:
                distances.append(random.randint(10, 1000))
        tsp.append(distances)
    return tsp
def main():

    start = time.time()
    tsp =     [[0, 82, 34, 127, 118, 46, 110, 127, 52, 44],
                  [82, 0, 76, 83, 99, 89, 106, 83, 84, 33],
                  [34, 76, 0, 127, 74, 44, 56, 106, 94, 86],
                  [127, 83, 127, 0, 37, 51, 118, 106, 124, 99],
                 [118, 99, 74, 37, 0, 91, 37, 132 ,49, 37],
                 [46, 89, 44, 51, 91, 0, 112, 131, 66, 85],
                  [110, 106, 56, 118, 37, 112, 0, 64, 121, 71],
            [127, 83, 106, 106, 132, 131, 64, 0, 43, 107],
            [52, 84, 94, 124, 49, 66, 121, 43, 0, 89],
            [44, 33, 86, 99, 37, 85, 71, 107, 89, 0]]

    print(hillClimbing(tsp))
    end = time.time_ns()
    print("time",end - start)

if __name__ == "__main__":
    main()