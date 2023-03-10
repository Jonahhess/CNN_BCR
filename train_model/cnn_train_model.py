"""
@author: Jonah Hess. 2022. All rights reserved.
"""

import argparse
import json
import os
import matplotlib.pyplot as plt
import numpy as np
import sys

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PROJECT_PATH)

from train_model_methods.cnn_train_classifier import CNNTrainClassifier


def main():
    """
    Description: This method is used to train the model.
    :return: None
    """

    # Parse the arguments
    parser = argparse.ArgumentParser(description='Train the model.')
    parser.add_argument('--load_path', default=(PROJECT_PATH + '\\output\\dataset\\'))
    parser.add_argument('--save_path', default=(PROJECT_PATH + '\\output\\model\\'))

    # Arguments
    args = parser.parse_args()
    load_path = os.path.normpath(args.load_path)
    save_path = os.path.normpath(args.save_path)

    # Load dataset
    x = np.load(os.path.join(load_path, 'cnn_dataset.npy'))
    y = np.load(os.path.join(load_path, 'cnn_labels.npy'))
    print(x.ndim,x.shape,y.ndim,y.shape)

    # Instantiate TrainClassifier
    cnn_train_classifier = CNNTrainClassifier(x=x, y=y)

    # Train classifier
    performance, history = cnn_train_classifier.train_classifier()

    # Save model
    print("Saving the model...")

    # Save model performance
    #with open(os.path.join(save_path, 'cnn_model_performance.json'), 'w') as fp:
        #json.dump(performance, fp)
        
    plt.plot(history.history['accuracy'], label='accuracy')
    plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0.5, 1])
    plt.legend(loc='lower right')

if __name__ == '__main__':
    main()
