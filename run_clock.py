"""
Function to both load in data from a Beta CSV File
and run the clock returning a list of predictions for each
sample
"""
import csv
import numpy as np
import scipy

def read_file(beta_file, probes):
    """
    Function to read in beta file as CSV.
    Returns a tuple of:
        1. 2D Numpy array filtered for model probes
        2. List of samples
    """
    samples = None
    data = []
    for _ in probes:
        data.append([])
    with open(beta_file, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in csv_reader:
            if not samples:
                samples = list(row.keys())[1:]
            if row[""] in probes:
                drow = []
                for sample in samples:
                    drow.append(float(row[sample]))
                indx = int(np.where(probes == row[""])[0])
                data[indx] = drow

    newx = np.transpose(np.array(data))
    return (newx, samples)

def run_clock(beta_file):
    """
    Function to run clock given the path to a CSV
    file containing the normalised beta values
    """
    probes = np.load("model/probes.npy")
    newx, samples = read_file(beta_file, probes)

    nbeta = np.load("model/nbeta.npy")
    result = scipy.dot(scipy.column_stack((scipy.ones([newx.shape[0], 1]), newx)), nbeta)[:, 0]
    return scipy.row_stack((samples, result.flatten()))
