import random
import math

NUMBER_OF_INDIVIDUALS = 10
APPROXIMATE_NUMBER_MATED = 5
MUTATION_RATE = 0.02
NUMBER_OF_WIEGHTS = 0
MAX_PERCENTAGE_OF_FIRE = 0.9

#the first layers is number of inputs
network_dim = [10,10,1]

for x in xrange(len(network_dim)):
        if x > 0 :
            #creating a feedforward network
            for y in xrange(network_dim[x -1] * network_dim[x]):
                NUMBER_OF_WIEGHTS += 1  
            #if not input layer add one more wieght for the bais of each node
            NUMBER_OF_WIEGHTS += network_dim[x]
            

TOTAL_NUMBER_OF_WIEGHTS = NUMBER_OF_WIEGHTS * NUMBER_OF_INDIVIDUALS
#list of list representing the list of wieghts for each individuals artificial neural network
wieght = []

#add random values to list of wieghts
for i in xrange(TOTAL_NUMBER_OF_WIEGHTS):
        wieght.append(random.random() - 0.5)
        
#outer loop scoring and mutation loop
#Scoring
individual_score = [0 for i in xrange(NUMBER_OF_INDIVIDUALS)]
individual_times_fired = [0 for i in xrange(NUMBER_OF_INDIVIDUALS)]

p = 0 #number of times we will loop in main loop
#Main loop
p += 1
#list to capture individual's outputs
individual_output = [[] for i in xrange(NUMBER_OF_INDIVIDUALS)]

    
#initialize input layer from foriegn source
input_layer = [1,1,1,1,1, 1,1,1,1,1]

###Trying to keep this next section of code very resuseable
current_wieght_number = 0
#propogate each neural network on input and get their outputs
for i in xrange(NUMBER_OF_INDIVIDUALS):
    feed_layer =[]
    feed_layer.append(input_layer)

    #for each layer in the network
    for x in xrange(len(network_dim)):
        if x == len(network_dim) - 1:
            for output in feed_layer[x]:
                individual_output[i].append(output)
        else:
            feed_layer.append([])
            #for each neuron on the next layer (writing)
            for y in xrange(network_dim[x + 1]):
                summation = 0
                #for each neuron on the current layer (reading)
                for k in xrange(network_dim[x] + 1):  #extra loop(+1) for bais
                    
                    #get the next wieght to use for the current edge                                              
                    if k==network_dim[x]:
                        #add wieght for bais
                       
                        summation += wieght[current_wieght_number]
                    else:
                        #add wieght for current edge for bais
                        summation += wieght[current_wieght_number] * feed_layer[x][k]
                    current_wieght_number += 1

                #Add neuron output to next feed_layer for input to next iteration
                feed_layer[x + 1].append(1/(1 + math.e**(-summation)))

#after propogation make sure number of wieghts used is not less expected
if TOTAL_NUMBER_OF_WIEGHTS != current_wieght_number:
    print 'error'

#using threshold and binary logic
fired_net_index = []
for index, output in enumerate(individual_output):
    if output[0] > 0.5:
        fired_net_index.append(index)
        individual_times_fired[index] += 1

#reward each individual that has fired with the total number of individuals that have simultaneously fired if more than one has fired.
if len(fired_net_index) > 1:       
    for index in fired_net_index:
        individual_score[index] += len(fired_net_index)
    

#end Main loop



#use old population mate over individuals
#Make scoring for each individual
#Get each score by subtracting the percentage of times it fired from 1.
#Such that each gets a higher score for firing less to make firing have a survival cost.
individual_times_fired_score = [1 - float(i)/p for i in individual_times_fired]

if sum(individual_times_fired_score) > 0:
    individual_times_fired_score = [float(i)/sum(individual_times_fired_score) for i in individual_times_fired_score] #populate and normalize individual_times_fired vector
    
#make list of synchronization scores for each ANN
synchronization_score = []

if(sum(individual_score) > 0):
    synchronization_score = [individual_score[i] / sum(individual_score) for i in xrange(NUMBER_OF_INIDIVIDUALS)]#populate and normalize synchronization_score vector


#add each individuals score together from each list and divide it by 2(to keep the sum of thresold == 1).
threshold = [sum(pair)/2 for pair in zip(individual_times_fired_score, synchronization_score)]
if sum(threshold) != 1:
    print 'sum of threshold values is not 1.'
    break
    
#do mating and mutation code
#for each individual select two half genes from each individual in the old population.
new_wieght = []
for i in xrange(NUMBER_OF_INDIVIDUALS):
    
    
    summation = 0
    first_half=[]
    second_half=[]
    #select one for first half of gene
    roulette= random.random()
    for x in xrange(len(threshold)):
        summation += threshold[x]
        if summation >= roulette:
            first_half = [x: x + NUMBER_OF_WIEGHTS/2]
            break
            
    #select second half       
    roulette= random.random()
    for x in xrange(len(threshold)):
        summation += threshold[x]
        if summation >= roulette:
            second_half = [x + NUMBER_OF_WIEGHTS/2: x + NUMBER_OF_WIEGHTS]
            break
    
    new_wieght += first_half + second_half
        
        
if len(wieght) != len(new_wieght):
    print 'error new_wieght does not equal wieght'
    break

#replace old wieght list
wieght = new_wieght
#since it's a random process mutation can and is done seperately from mating.
#mutation makes sure new wieght values entire the system PER INDIVIDUAL.
for i in xrange(int(TOTAL_NUMBER_OF_WIEGHTS * MUTATION_RATE)):
        wieght[int(random.random()*NUMBER_OF_INDIVIDUALS)] = random.random() - 0.5


#end outer loop

        
print 'individual_output : \n'
print individual_output
print 'fired_net_index : \n'
print fired_net_index
print 'individual_times_fired : \n'
print individual_times_fired
