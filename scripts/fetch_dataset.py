import os
import argparse
from keras.datasets import mnist

assert os.environ["KERAS_BACKEND"] == "torch", "make sure you run 'source .env'"

LOADERS = {"mnist": mnist.load_data}
parser = argparse.ArgumentParser("data importer")
parser.add_argument("-d", "--dataset", choices=LOADERS)

if __name__ == "__main__":
    args = parser.parse_args()
    LOADERS[args.dataset]()
    print(f"downloading {args.dataset} into ~/.keras/datasets")
