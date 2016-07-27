#############################################################################################################
## THESE PARAMETERS ARE STANDARD, AND EITHER DO NOT CHANGE IN THE SENSITIVITY ANALYSIS, OR ARE NOT USED AT ALL
ROWS = 200

COLUMNS = 200

ITERATIONS = 5000


REFRESH_RATE = 1

SPECIES = 60

CONNECTANCE = 0.08

PROB_NICHE_MODEL = False

#number of iterations (interval) for the recalculation of network metrics
NETWORK_RECORD = 200

#fraction of iterations that will be considered for the species output
ITERATIONS_TO_RECORD = 0.1

#fraction of iterations before the end of the simulation when the network
#state will be reset in order to obtain a snapshot of the current network
NETWORK_RESET = 0.1

#whether to calculate the metrics for quantifying spatial variation among species
SPATIAL_VARIATION = True

RECORD_SPATIAL_VAR = ITERATIONS * 2 ## such that spatial aggreation metrics are never evaluated of saved (output_space_X.csv not exist)

#the fraction of points to remove that are farthest from the centroid of the population
#before calculating the population radius
DISPERSAL_KERNEL = 0.03

##whether to calculate the interaction strengths matrices
INT_STRENGTHS = True

#fraction of primary producer species in the network
PRIMARY_PRODS = 0.25

#percentage of herbivore species in the network
HERBIVORY = 0.25

#fraction of top predator species in the original network
TOP_PREDATORS = 0.05

#whether to double the number of herbivore individuals
DOUBLE_HERBIVORY = True

#minimum nestedness of the mutualistic sub-network
MIN_NESTEDNESS = 0.0

MAX_NESTEDNESS = 0.0

#fraction of herbivores that are mutualists
#MUTUALISM = 0.1

#minimum number of mutualists (in case number of herbivores is less than
#1/MUTUALISM number of mutualists desired)
MIN_MUTUALISTS = 0

#fraction of living expenditure applied exclusively to mutualistic animals
MUTUALISTIC_LOSS = 1.0

MUT_PRODUCER_LOSS = 1.0

#number of neighbour cells that a species can have to find a mate
MATING_SPATIAL_RATIO = 3

#number of cells, in each direction, an individual can move in a given iteration
MOVE_RADIUS = 1

#number of cells, in each direction, a mutualistic individual can move in a given iteration
MOVE_RADIUS_MUTUALISTS = 1


#####
#The next parameters are for the reproduction of plants (either via mutualism or by wind dispersal)

#minimum mutualistic dispersal efficiency after which no more dispersal of the plant
#partner is allowed
MIN_MUTUALISTIC_EFF = 0.1

#number of habitats present in the ecosystem
HABITATS = 1

#max number of habitats a given species is allowed to inhabit
#if the case of type 2 habitats this only applies to primary producers, since the 
#other species will get their distributions from the habitats inhabited by their prey
MAX_HABITATS = 1

#whether to apply a habitat loss event
HABITAT_LOSS = True

#it must be less than the number of iterations. It specifies the time step at which the 
#habitat loss is going to take place 
HABITAT_LOSS_ITER = 1000

# this number specifies the heuristic to be followed to destroy the habitat when HABITAT_LOSS = True
# 1 = contiguous (hole-like patch), 2 = random cells lost, 3 = TBA

#fraction of habitat that will become lost, which will produce habitat loss and fragmentation
#LOST_HABITAT = 0.5

#whether to apply an invasion event
INVASION = False

#iteration at which the invader is set to enter the network
INVASION_ITER = 200

#number of possible invader species
POSSIBLE_INVADERS = 0

#number of individuals of the invader species to introduce into the world
INVADER_NUMBER = 200


##########
#These parameters are used for the calculation of stability measures

#number of iteration at which the extinction event is going to happen
EXTINCTION_EVENT = 400

#number of iterations to be considered for the calculation of stability measures
TIME_WINDOW = 150

#level at which species will be removed; values: 'top', 'cons', 'herb', 'prod'
REMOVAL_LEVEL = 'top'

#fraction of species to be removed
REMOVAL_FRACTION = 1.0


##########
READ_FILE_NETWORK = False

SRC_NET_FILE = 'initial_network.graphml'

#############################################################################################################
## THESE PARAMETERS TO BE SET MANUALLY:
HABITAT_LOSS_TYPE = 2 


