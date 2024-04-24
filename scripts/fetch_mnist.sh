# see docs



# http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz" "
BASE_SOURCE="http://yann.lecun.com/exdb/mnist"
BASE_DEST="datasets/mnist"

echo "downloading subsets from $BASE_SOURCE"
for MNIST_SUBSET in "train-images-idx3-ubyte.gz" "train-labels-idx1-ubyte.gz" "t10k-images-idx3-ubyte.gz" "t10k-labels-idx1-ubyte.gz" 
do
  wget -P $BASE_DEST/gz $BASE_SOURCE/$MNIST_SUBSET && tar -xvf "$BASE_DEST/gz"
  rm $BASE_DEST/gz
done


echo "finished, exiting..."
