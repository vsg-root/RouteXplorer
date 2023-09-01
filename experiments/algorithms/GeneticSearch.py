import random, time



class GeneticSearch():
    """Class that contains methods to solve the TSP using the genetic algorithm"""

    def calculateFitness(self, route: list[str], coordinates: dict) -> float:
        """Calculates the total distance of a route.
            Args:
            route: list[str] -> Route to be analyzed.
            coordinates: dict -> Dictionary with points and their coordinates."""
        fitness = 0
        for index in range(len(route) - 1):
            fitness += self.calculateDistance(route[index], route[index+1], coordinates)
        return fitness
    
    def calculateDistance(self, firstVertex: str, secondVertex: str, coordinates: dict) -> float:
        """Calculates the distance between two points.
            Args:
            firstVertex: str -> First point.
            secondVertex: str -> Second point.
            coordinates: dict -> Dictionary with points and their coordinates."""
        firstVertexX, firstVertexY = coordinates[f'{firstVertex}']
        secondVertexX, secondVertexY = coordinates[f'{secondVertex}']
        distance = abs(firstVertexX - secondVertexX) + abs(firstVertexY - secondVertexY)
        return distance

    def tournamentWinner(self, population: list, coordinates: dict) -> list[str]:
        """Chooses two random routes to compete against each other and returns the one with the shortest route.
            Args:
            population: list -> List containing the current population.
            coordinates: dict -> Dictionary with points and their coordinates."""
        firstCompetitor, secondCompetitor = random.choice(population), random.choice(population)
        if self.calculateFitness(firstCompetitor, coordinates) < self.calculateFitness(secondCompetitor, coordinates):
            return firstCompetitor
        else:
            return secondCompetitor
        
    def crossover(self, firstIndividual: list[str], secondIndividual: list[str]) -> tuple:
        """Crosses two individuals to obtain two new routes.
            Args:
            firstIndividual: list[str] -> First chosen individual.
            secondIndividual: list[str] -> Second chosen individual."""
        separator = random.randint(2, len(firstIndividual)-2)
        firstIndividual, secondIndividual = self.PMX(firstIndividual, secondIndividual, separator)
        firstChild = firstIndividual[:separator] + secondIndividual[separator:]
        secondChild = secondIndividual[:separator] + firstIndividual[separator:]
        return (firstChild, secondChild)
    
    def PMX(self, firstIndividual: list[str], secondIndividual: list[str], separator: int) -> tuple:
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
    
    def createGeneration(self, currentPopulation: list[list[str]], crossoverRate: int, mutationRate: int, coordinates: dict) -> list[list[str]]:
        """Creates a new generation of individuals.
            Args:
            currentPopulation: list[list[str]] -> Current population.
            crossoverRate: int -> The rate at which crossover will occur.
            mutationRate: int -> The rate at which mutation can occur.
            coordinates: dict -> Dictionary with points and their coordinates."""
        newGeneration = []
        while len(newGeneration) < len(currentPopulation):
            firstParent, secondParent = self.tournamentWinner(currentPopulation, coordinates), self.tournamentWinner(currentPopulation, coordinates)
            if random.randint(1, 100) < crossoverRate:
                firstChild, secondChild = self.crossover(firstParent, secondParent)
            else:
                firstChild, secondChild = firstParent, secondParent
                
            firstChild = self.mutation(firstChild, mutationRate)
            secondChild = self.mutation(secondChild, mutationRate)
            newGeneration.append(firstChild)
            newGeneration.append(secondChild)
        return newGeneration
    
    def initialGeneration(self, points: dict, populationSize: int) -> list[list[str]]:
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
    
    def find_best_path(self, points: dict) -> str:
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
        population = self.initialGeneration(points, populationSize)
        
        while generation < maxGenerations:
            population = self.createGeneration(population, crossoverRate, mutationRate, points)
            for individual in population:
                if self.calculateFitness(individual, points) < lowestRouteCost:
                    lowestRouteCost = self.calculateFitness(individual, points)
                    bestRoute = individual

            generation += 1
        return f'Best route: {bestRoute}\nCost: {lowestRouteCost}'
    

pontosDeEntrega_52 = {
    '1': [565.0, 575.0],
    '2': [25.0, 185.0],
    '3': [345.0, 750.0],
    '4': [945.0, 685.0],
    '5': [845.0, 655.0],
    '6': [880.0, 660.0],
    '7': [25.0, 230.0],
    '8': [525.0, 1000.0],
    '9': [580.0, 1175.0],
    '10': [650.0, 1130.0],
    '11': [1605.0, 620.0],
    '12': [1220.0, 580.0],
    '13': [1465.0, 200.0],
    '14': [1530.0, 5.0],
    '15': [845.0, 680.0],
    '16': [725.0, 370.0],
    '17': [145.0, 665.0],
    '18': [415.0, 635.0],
    '19': [510.0, 875.0],
    '20': [560.0, 365.0],
    '21': [300.0, 465.0],
    '22': [520.0, 585.0],
    '23': [480.0, 415.0],
    '24': [835.0, 625.0],
    '25': [975.0, 580.0],
    '26': [1215.0, 245.0],
    '27': [1320.0, 315.0],
    '28': [1250.0, 400.0],
    '29': [660.0, 180.0],
    '30': [410.0, 250.0],
    '31': [420.0, 555.0],
    '32': [575.0, 665.0],
    '33': [1150.0, 1160.0],
    '34': [700.0, 580.0],
    '35': [685.0, 595.0],
    '36': [685.0, 610.0],
    '37': [770.0, 610.0],
    '38': [795.0, 645.0],
    '39': [720.0, 635.0],
    '40': [760.0, 650.0],
    '41': [475.0, 960.0],
    '42': [95.0, 260.0],
    '43': [875.0, 920.0],
    '44': [700.0, 500.0],
    '45': [555.0, 815.0],
    '46': [830.0, 485.0],
    '47': [1170.0, 65.0],
    '48': [830.0, 610.0],
    '49': [605.0, 625.0],
    '50': [595.0, 360.0],
    '51': [1340.0, 725.0],
    '52': [1740.0, 245.0]
}
pontosDeEntrega_3 = {
    '1': [3, 0],
    '2': [1, 1],
    '3': [0, 0],
    '4': [3, 2]
}
pontosDeEntrega_6 = {
    '1': [3, 0],
    '2': [1, 1],
    '3': [3, 2],
    '4': [2, 4],
    '5': [0, 4],
    '6': [0, 0],
    '7': [1, 3]
}
pontosDeEntrega_9 = {
    '1': [565.0, 575.0],
    '2': [25.0, 185.0],
    '3': [345.0, 750.0],
    '4': [945.0, 685.0],
    '5': [845.0, 655.0],
    '6': [880.0, 660.0],
    '7': [25.0, 230.0],
    '8': [525.0, 1000.0],
    '9': [580.0, 1175.0],
    '10': [2, 4]
}
c = 0
while c < 30:
    start_time = time.time()
    geneticSearch = GeneticSearch()
    resultado = geneticSearch.find_best_path(pontosDeEntrega_52)
    print(resultado)
    end_time = time.time()
    result = end_time - start_time
    print(f'tempo: {result:.4f} segundos')
    c += 1