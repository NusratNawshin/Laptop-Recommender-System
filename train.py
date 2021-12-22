from numpy import exp, dot, array, random
import pandas as pd
import json
import numpy as np
import pickle


class neuralNetwork():
    def __init__(self):
        # Seed the random number generator, so it generates the same numbers
        # every time the program runs.
        random.seed(0)

        # 4 input connections and 1 output connection.
        # We assign random weights to a 4 x 1 matrix
        self.synaptic_weights = random.random((4, 1))

    # We pass the weighted sum of the inputs through this function to
    # normalise them between 0 and 1.
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # matrix multiplication of input matrix and weight matrix for forward propagation
    def think(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

        # train the model through backward propagation by trail and error
        # we adjust synaptic weights in each time

    def train(self, training_set_inputs, training_set_outputs, iteration_time):
        for iteration in range(iteration_time):
            output = self.think(training_set_inputs)
            error = training_set_outputs - output
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))
            self.synaptic_weights += adjustment


if __name__ == "__main__":
    neural_net = neuralNetwork()
    indata = pd.read_excel('project.xlsx', header=None)
    indata = indata.iloc[:, 0:4]
    Input = indata.to_string(index=False, header=False)
    Minput = indata.as_matrix()

    outRead = pd.read_excel('project.xlsx', header=None)
    outData = outRead.iloc[:, -1]
    output = outData.to_string(index=False)
    Moutput = outData.as_matrix()

    training_set_inputs = array(Minput)
    training_set_outputs = array([Moutput]).T

    # Train the neural network using a training set inputs and outputs
    # which are split from project.xlsx file .
    # Do it 10,000 times and make small adjustments each time
    neural_net.train(training_set_inputs, training_set_outputs, 1200)

    f = open('weight.pickle', 'wb')
    pickle.dump(neural_net.synaptic_weights, f, pickle.HIGHEST_PROTOCOL)
    f.close()