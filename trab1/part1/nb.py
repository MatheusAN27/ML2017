#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-

from sklearn import cross_validation
from sklearn.datasets import load_svmlight_file
from sklearn.naive_bayes import BernoulliNB
import matplotlib.pyplot as plt
import numpy as np


def main(X_data, y_data, test_size):
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(
        X_data, y_data, test_size=test_size
    )

    X_train = X_train.toarray()
    # cria o classificador
    gnb = BernoulliNB()

    gnb.fit(X_train, y_train)

    # mostra o resultado do classificador na base de teste
    return gnb.score(X_test, y_test)


if __name__ == "__main__":
    sizes = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    X_data, y_data = load_svmlight_file('./data')
    accuracies = []
    for x in sizes:
        accuracies.append(main(X_data, y_data, x))

    y_pos = np.arange(len(sizes))
    plt.ylim(0, 1)
    plt.bar(y_pos, accuracies, align='center', alpha=0.5)
    plt.xticks(y_pos, sizes)
    plt.xlabel('Test size')
    plt.ylabel('Accuracy')
    plt.title('Accuracy over test size')

    plt.savefig('nb_result.png', bbox_inches='tight')
