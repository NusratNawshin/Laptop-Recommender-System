from numpy import exp, dot, array, random
import pandas as pd
import json
import numpy as np
import pickle
import pandas as pd


def sigmoid(x):
    return 1 / (1 + exp(-x))


def think(inputs):
    return sigmoid(dot(inputs, synaptic_weights))


# make prediction for new data
synaptic_weights = random.random((4, 1))

f = open('weight.pickle', 'rb')
synaptic_weights = pickle.load(f)