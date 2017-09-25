This is an implementation of backpropogation for a feed-forward neural network. The algorithm uses calculus to determine how much to
shift the any given weight of the neural network by taking a derivative ofthe error with respect to the weight.
THIS ALOGIRHTM STILL HAS A BUG!
However, here's the equations

Given a neural network with n layers and m(i) neuron activations for layer i.
let W(i) be weight m(i+1) x m(i) matrix at layer i.
let A(i) be the activations at layer i including the output activations at layer n(which have no corresponding weight matrix). 
  Also the inputs, which are layer 0.
let T be the m(n) x 1 vector of target values.
let E be Error which is a  output is a 1 x m(n) vector.
Also let Sig be the sigmoid function.


i=0,1,..,n-1

A(i+1) = Sig(W(i) * A(i))

E = ((A(n) - T)**T * (A(n) - T)) /2

dE/dW(n-1) = (A(n) - T) * Sig'(W(n-1) * W(n-1)) * A(n) /dW(n-1) = (A(n) - T) * Sig'(W(n-1) * A(n-1)**T

Not Finished.
