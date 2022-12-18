def relu(x, derivative=False):
    if(derivative==False):
        return x*(x > 0)

    else:
        return 1*(x > 0)

def sigmoid(x):
    return 1.0/(1.0 + 2.71828**(-x))

def tanh(x):
    return (2.0/(1.0 + 2.71828**(-2 * x)) - 1)


def forward_activation(x, activation_function): 
    if activation_function == "sigmoid":
      return sigmoid(x)
    elif activation_function == "tanh":
      return tanh(x)
    elif activation_function == "relu":
      return relu(x)