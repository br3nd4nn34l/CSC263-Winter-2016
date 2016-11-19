import random
import statistics


def FlipBiasedCoin(p):
    if random.random() < p:
        return 1
    else:
        return 0

def UnbiasedRNG(p):
    v1 = 0
    v2 = 0
    num_iterations = 0
    while (v1 == v2):
        v1 = FlipBiasedCoin(p)
        v2 = FlipBiasedCoin(p)
        num_iterations += 1
    num_steps = 4 + (3*(num_iterations - 1))
    return [v1, num_steps]

def Experiment(p, num_times):
    experiment_array = []
    for i in range(num_times):
        experiment_array += [UnbiasedRNG(p)[1]]
    sum_steps = 0
    for i in range(len(experiment_array)):
        sum_steps += experiment_array[i]
    return (sum_steps / len(experiment_array))

def Expected(p):
    x = 2*(p**2) - 2*p + 1
    not_x = 1 - x
    numerator = 4 - x
    denominator = (x-1)**2
    return (numerator / denominator) * not_x

def Discrepency(p):
    expected = Expected(p)
    actual = Experiment(p, 1000)
    discrepency = abs(expected - actual)
    return discrepency

def DiscrepencyLoop(p):
    trials = []
    for i in range(1, 100):
        trials += [Discrepency(p)]
    return statistics.mean(trials)