import numpy as np

# Define sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Initialize input features
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Initialize weights
W_input_hidden = np.array([[0.1, 0.2], [0.3, 0.4]])
W_hidden_output = np.array([[0.5], [0.6]])

# Forward pass through the neural network
for x in X:
    # Input to hidden layer
    hidden_input = np.dot(x, W_input_hidden)
    hidden_output = sigmoid(hidden_input)
    
    # Hidden to output layer
    output = sigmoid(np.dot(hidden_output, W_hidden_output))
    
    print("Input:", x)
    print("Output:", output)
    print()