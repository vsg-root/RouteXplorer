import random, time



class GeneticSearch():
    """Class that contains methods to solve the TSP using the genetic algorithm"""
    
    @staticmethod
    def calculateFitness(route: list[str], coordinates: dict) -> float:
        """Calculates the total distance of a route.
            Args:
            route: list[str] -> Route to be analyzed.
            coordinates: dict -> Dictionary with points and their coordinates."""
        fitness = 0
        for index in range(len(route) - 1):
            fitness += GeneticSearch.calculateDistance(route[index], route[index+1], coordinates)
        return fitness

    @staticmethod
    def calculateDistance(firstVertex: str, secondVertex: str, coordinates: dict) -> float:
        """Calculates the distance between two points.
            Args:
            firstVertex: str -> First point.
            secondVertex: str -> Second point.
            coordinates: dict -> Dictionary with points and their coordinates."""
        firstVertexX, firstVertexY = coordinates[firstVertex]
        secondVertexX, secondVertexY = coordinates[secondVertex]
        distance = sqrt((firstVertexX - secondVertexX)**2 + (firstVertexY - secondVertexY)**2)) 
        return distance
    @staticmethod
    def tournamentWinner(population: list, coordinates: dict) -> list[str]:
        """Chooses two random routes to compete against each other and returns the one with the shortest route.
            Args:
            population: list -> List containing the current population.
            coordinates: dict -> Dictionary with points and their coordinates."""
        firstCompetitor, secondCompetitor = random.choice(population), random.choice(population)
        if GeneticSearch.calculateFitness(firstCompetitor, coordinates) < GeneticSearch.calculateFitness(secondCompetitor, coordinates):
            return firstCompetitor
        else:
            return secondCompetitor
    @staticmethod     
    def crossover(firstIndividual: list[str], secondIndividual: list[str]) -> tuple:
        """Crosses two individuals to obtain two new routes.
            Args:
            firstIndividual: list[str] -> First chosen individual.
            secondIndividual: list[str] -> Second chosen individual."""
        separator = random.randint(2, len(firstIndividual)-2)
        firstIndividual, secondIndividual = GeneticSearch.PMX(firstIndividual, secondIndividual, separator)
        firstChild = firstIndividual[:separator] + secondIndividual[separator:]
        secondChild = secondIndividual[:separator] + firstIndividual[separator:]
        return (firstChild, secondChild)
    @staticmethod
    def PMX(firstIndividual: list[str], secondIndividual: list[str], separator: int) -> tuple:
        """The PMX method ensures that there is no repetition of vertices in a route.
            Args:
            firstIndividual: list[str] -> First chosen individual.
            secondIndividual: list[str] -> Second chosen individual.
            separator: int -> Location where the crossing of the two chosen individuals will occur."""
        firstIndividual = firstIndividual[1:-1]
        secondIndividual = secondIndividual[1:-1]
        for principalIndex, i in enumerate(firstIndividual[:separator]):
            for secondaryIndex, j in enumerate(secondIndividual):
                if i == j:
                    secondIndividual[principalIndex], secondIndividual[secondaryIndex] = secondIndividual[secondaryIndex], secondIndividual[principalIndex]
        firstIndividual = ['1'] + firstIndividual + ['1']
        secondIndividual = ['1'] + secondIndividual + ['1']
        return (firstIndividual, secondIndividual)
    
    @staticmethod
    def mutation(individual: list[str], mutationRate: int) -> list[str]:
        """Analyzes each vertex's chance of mutation. If mutation occurs, two vertices swap places, representing a mutation.
           Args:
           individual: list[str] -> Individual to be analyzed.
           mutationRate: int -> The mutation rate of the algorithm."""
        for index in range(1, len(individual) - 2):
            if random.randint(1, 100) <= mutationRate:
                individual[index], individual[index+1] = individual[index+1], individual[index]
        return individual
    @staticmethod
    def createGeneration(currentPopulation: list[list[str]], crossoverRate: int, mutationRate: int, coordinates: dict) -> list[list[str]]:
        """Creates a new generation of individuals.
            Args:
            currentPopulation: list[list[str]] -> Current population.
            crossoverRate: int -> The rate at which crossover will occur.
            mutationRate: int -> The rate at which mutation can occur.
            coordinates: dict -> Dictionary with points and their coordinates."""
        newGeneration = []
        while len(newGeneration) < len(currentPopulation):
            firstParent, secondParent = GeneticSearch.tournamentWinner(currentPopulation, coordinates), GeneticSearch.tournamentWinner(currentPopulation, coordinates)
            if random.randint(1, 100) < crossoverRate:
                firstChild, secondChild = GeneticSearch.crossover(firstParent, secondParent)
            else:
                firstChild, secondChild = firstParent, secondParent
                
            firstChild = GeneticSearch.mutation(firstChild, mutationRate)
            secondChild = GeneticSearch.mutation(secondChild, mutationRate)
            newGeneration.append(firstChild)
            newGeneration.append(secondChild)
        return newGeneration
    @staticmethod
    def initialGeneration(points: dict, populationSize: int) -> list[list[str]]:
        """Constructs the initial population that will be used in the algorithm.
            Args:
            points: dict -> Dictionary with points and their coordinates.
            populationSize: int -> The number of individuals the population will have."""
        firstGeneration = []
        points = list(points.keys())
        points = points[1:]
        for _ in range(populationSize):
            randomPoints = points.copy()
            random.shuffle(randomPoints)
            newElement = ['1'] + randomPoints + ['1']
            firstGeneration.append(newElement)
        return firstGeneration
    @staticmethod
    def find_best_path(points: dict) -> str:
        """Main method of the genetic algorithm responsible for finding the best route. Variables will be initialized here, and other methods will be used to achieve a good result.
            Args:
            points: dict -> Dictionary with points and their coordinates."""
        generation = 1
        populationSize = 30
        maxGenerations = 1500
        crossoverRate = 95
        mutationRate = 2
        lowestRouteCost = float('inf')
        bestRoute = []
        population = GeneticSearch.initialGeneration(points, populationSize)
        
        while generation < maxGenerations:
            population = GeneticSearch.createGeneration(population, crossoverRate, mutationRate, points)
            for individual in population:
                if GeneticSearch.calculateFitness(individual, points) < lowestRouteCost:
                    lowestRouteCost = GeneticSearch.calculateFitness(individual, points)
                    bestRoute = individual

            generation += 1
        return bestRoute[1:-1], lowestRouteCost
    
