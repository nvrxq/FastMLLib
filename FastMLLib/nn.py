def relu(x, derivative=False):
  '''
  Rectified Linear Unit (ReLU) activation function
  '''
  if(derivative==False):
      return x*(x > 0)

  else:
      return 1*(x > 0)

def sigmoid(x):
  '''
  The Sigmoid Function curve looks like a S-shape.
  '''
  return 1.0/(1.0 + 2.71828**(-x))

def tanh(x):
  '''
  Hyperbolic tangent activation function
  '''
  return (2.0/(1.0 + 2.71828**(-2 * x)) - 1)


def forward_activation(x, activation_function): 
  '''
  Function for choosing activation function
  '''
  if activation_function == "sigmoid":
    return sigmoid(x)
  elif activation_function == "tanh":
    return tanh(x)
  elif activation_function == "relu":
    return relu(x)



def calc_grad(delta, x_batch):
  return [delta * item for item in x_batch.array]