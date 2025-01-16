#!/bin/bash

FILES_LIST="home/models/best_candidate.ckpt home/fonts/Helvetica-Bold-Font.ttf home/data/MNIST_CSV/mnist_test.csv home/data/MNIST_CSV/mnist_train.csv home/data/challenge/challenge_train.csv home/data/challenge/challenge_test.csv"

for f in $FILES_LIST; do
    if [ -f $f ]; then
        echo "✅ $f exists"
    else
        echo "❌ !!! $f DOES NOT EXIST"
    fi
done