#!/bin/bash

# Create folder if it does not exist
mkdir -p home/models

# Download model from dropbox
wget \
    -O home/models/best_candidate.ckpt \
    "https://www.dropbox.com/scl/fi/272x8cxlsevkpnn40mgnk/best_candidate.ckpt?rlkey=uokxm82dzm825xj58ry36n5ux&st=bxzkpftu&dl=1" \ 
    

# Create folder for fonts
mkdir -p home/fonts

# Download font from dropbox
wget -O home/fonts/Helvetica-Bold-Font.ttf \
    "https://www.dropbox.com/s/wad32grfxvhtamp/Helvetica-Bold-Font.ttf?dl=1" \
    

# Create home for MNIST.csv
mkdir -p home/data

wget -O home/data/MNIST_CSV.zip \
"https://www.dropbox.com/scl/fi/n6i5j75j5rgjez27qpw0n/MNIST_CSV.zip?rlkey=vc253rogq2gxdqearqrhv1ytf&dl=0"

unzip home/data/MNIST_CSV.zip -d home/data/MNIST_CSV