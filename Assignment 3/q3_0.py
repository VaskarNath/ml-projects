'''
Question 3.0 Skeleton Code

Here you should load the data and plot
the means for each of the digit classes.
'''

import data
import numpy as np
# Import pyplot - plt.imshow is useful!
import matplotlib.pyplot as plt


def plot_means(train_data, train_labels):
    means = []
    for i in range(0, 10):
        i_digits = data.get_digits_by_label(train_data, train_labels, i)
        arr = np.sum(i_digits/700, axis=0)
        arr = np.reshape(arr, (8, 8))
        means.append(arr)

    # Plot all means on same axis
    all_concat = np.concatenate(means, 1)
    plt.imshow(all_concat, cmap='gray')
    plt.savefig("Mean of Handwritten Digits")


if __name__ == '__main__':
    train_data, train_labels, _, _ = data.load_all_data_from_zip('a3digits.zip', 'data')
    plot_means(train_data, train_labels)