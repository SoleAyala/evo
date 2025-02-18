from src.geneticalgorithm.restriction.ConsistencyAndDiversityRestriction import ConsistencyAndDiversityRestriction
from src.geneticalgorithm.restriction.UserPreferencesRestriction import UserPreferencesRestriction
from src.geneticalgorithm.restriction.HealthyFoodRestriction import HealthyFoodRestriction
from src.geneticalgorithm.restriction.PARestriction import PARestriction
from src.ontology.user.PAPreferenceData import PAPreferenceData
from src.ontology.user.FoodPreferenceData import FoodPreferenceData
from src.ontology.user.PhysicalData import PhysicalData
import random
import copy

class RandomAlgorithm:
    NUMBER_OF_MEALS_PER_DAY = 3

    def __init__(self, user_data, most_similar_user_data):
        self.number_of_individuals = 250
        self.number_of_generations = 150
        self.physical_data = PhysicalData(*user_data[:5], user_data[29])
        self.food_preferences = FoodPreferenceData(*user_data[5:19])
        self.pa_preferences = PAPreferenceData(*user_data[19:29])
        self.food_items = {}
        self.pa_items = []
        self.restrictions = []
        self.mutation_dictionary = {}

        self.__configure_data(user_data, most_similar_user_data)

    def execute_random_algorithm(self):
        population = self.create_random_population()
        best_individual = self.evaluate_population(population)

        for _ in range(self.number_of_generations):
            population = self.create_random_population()
            current_best = self.evaluate_population(population)
            if current_best.fitness < best_individual.fitness:
                best_individual = current_best
        self.__print_phenotype(best_individual.phenotype)
        return best_individual.phenotype

    def create_random_population(self):
        population = []
        for _ in range(self.number_of_individuals):
            individual = self.create_random_individual()
            population.append(individual)
        return population

    def create_random_individual(self):
       #VER CON MONI COMO CREA LS INDIVIDUOS
        return create_individual(self.physical_data, self.food_preferences, self.pa_preferences, self.food_items, self.pa_items)

    def evaluate_population(self, population):
        best_individual = None
        for individual in population:
            fitness = self.calculate_fitness(individual)
            individual.fitness = fitness
            if not best_individual or fitness < best_individual.fitness:
                best_individual = individual
        return best_individual

    def calculate_fitness(self, individual):
        # Compute fitness based on restrictions and preferences
        fitness = 0
        for restriction in self.restrictions:
            fitness += restriction.evaluate(individual)
        return fitness

    def __configure_data(self, user_data, most_similar_user_data):
        # Method configurations as in the original genetic algorithm
        pass

    def __print_phenotype(self, phenotype):
        # Printing details about the phenotype as in the original genetic algorithm
        pass

# This function is assumed to exist, creating an individual based on given data
def create_individual(physical_data, food_preferences, pa_preferences, food_items, pa_items):
    # Implement the logic to create a random individual based on given parameters
    pass

# PONER ACA COMO SE LLAMA AL ALGORIMO PREUNGTAR MONI
user_data =
most_similar_user_data =
ra = RandomAlgorithm(user_data, most_similar_user_data)
recommendations = ra.execute_random_algorithm()
