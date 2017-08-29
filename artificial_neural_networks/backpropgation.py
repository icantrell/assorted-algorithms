import numpy as np

class ANN:
    def _internal_net_update(self, weights):
        self.outputs = weights.copy()
        
        
    def __init__(self,learning_rate = 0.1,w=[]):
        self.learning_rate = learning_rate
        self.weights = w
    
    def random_weights(self, shape):
        weights = []
        for i in range(1,len(shape)):
            weights.append(np.random.random((shape[i],shape[i-1]+1))*2 - 1)
            
        self.set_weights(weights)
            
    def set_weights(self,w):
        '''
        Takes a three dimensional matrix.
        0 axis is the layers.
        1 axis is the neurons on that layer.
        2 axis is the incoming weights for each neuron. Including the bais at the end of vector(so each array is > 1 
             and n-1 inputs for the neuron given an array of size n).
        
        '''
        
        
        self.weights = w
       
    
    def _logistic_sigmoid(self,n):
        return 1/(1 + np.e**(-n))
    
    def forward(self, inputs):
        inputs = np.array(inputs)
        current_inputs = inputs
        
        self.outputs=[]
        for i in range(len(self.weights)):
            #there is one row for each neuron in the weight matrix the statement will produce output for each neuron. 
            self.outputs.append(self._logistic_sigmoid(\
                np.dot(self.weights[i][:,:-1],current_inputs) + self.weights[i][:,-1]))
            
            current_inputs = self.outputs[i]
        return self.outputs[-1]
    
    def _derivative_logistic_sigmoid(self,n):
        return n*(1.0 - n)
    
    def  backpropogation(self, expected, training_example):
        error = 0
        for i in reversed(range(len(self.outputs))):
            if i == len(self.outputs) -1:
                error = self.outputs[i] - expected
                
            else:
                #propogate error backwards through network (Multiply error by outgoing weights).
                #Then sum along columns(expect for bias column) in order to get the sum of error outgoing to each neuron in thep previous layer.
                error = np.sum(self.weights[i+1][:,:-1].T.dot(error),0)
            
            #multply by derivative of sigmoid function for each neuron. 
            error *= self._derivative_logistic_sigmoid(self.outputs[i])
            
            if i == 0:
                inputs = training_example
            else:
                inputs = self.outputs[i-1]
            
            
            
            
            self.weights[i][:,:-1] -= self.learning_rate*error.reshape((-1,1))*inputs
            #only get array after the bais weight, the last weight(returns a subarrray not an element).
            self.weights[i][:,-1:] -= self.learning_rate*error.reshape((-1,1))
            
        
            
    def train(self, training_set, expected_set, epochs=2000):
        error= 0 
        last_error=0
        
        for example, expected in zip(training_set, expected_set):
            error += np.sum(np.abs(expected - self.forward(example)))
                       
        last_error = error + 1
            
        for _ in range(epochs):
            last_error = error
            
            error= 0 
            
            for example, expected in zip(training_set, expected_set):
                self.backpropogation(expected, example)
                error += np.sum(np.abs(expected - self.forward(example)))
                
                

net = ANN(learning_rate=1)
net.random_weights((2,2,2,1))
net.train([(0,1),(1,0),(1,1),(0,0)],[1,1,0,0])


print(net.forward((0,1)))
print(net.forward((1,1)))
print(net.forward((1,0)))
print(net.forward((0,0)))
            
            
            
            
            
            
        
            
        
        
        
       
       
    
