# https://www.scaler.com/academy/mentee-dashboard/class/417088/homework/problems/25793?navref=cl_tt_nv

import numpy as np

dataset = eval(input())
dataset = np.asarray(dataset)


# It returns the mean of numbers list
def mean(numbers):
    return sum(numbers) / float(len(numbers))


# printing the mean of the dataset
print('True Mean: %.3f' % mean(dataset))


# It returns a 2d list consisting of the observations from the dataset
# representing the subsamples used in bootstrap sampling
def subsample(dataset, ratio=1.0):
    sample = list()
    # 1. Number of observations to draw, rounded to the nearest integer
    n_sample = round(len(dataset) * ratio)

    while len(sample) < n_sample:
        # 2. Pick a random index from the dataset (0 to len-1)
        index = np.random.randint(0, len(dataset))
        # 3. Append the observation at that index to the sample list
        sample.append(dataset[index])
    return sample


np.random.seed(1)

# ratio of the dataset we will be using to create bootstrap samples
ratio = 0.10
for n_bootstrap in [1, 10, 100]:
    sample_means = list()  # list consisting of the mean of the bootstrap samples
    for i in range(n_bootstrap):
        # Draw a sample from the dataset
        sample = subsample(dataset, ratio)
        # 4. Find the mean of the newly created sample
        sample_mean = mean(sample)
        sample_means.append(sample_mean)

    # Printing the mean of the collection of bootstrap sample means
    print('Samples=%d, Estimated Mean: %.3f' % (n_bootstrap, mean(sample_means)))