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
    

# Create folder for MNIST.csv
mkdir -p home/data

wget -O home/data/MNIST_CSV.zip \
"https://www.dropbox.com/scl/fi/n6i5j75j5rgjez27qpw0n/MNIST_CSV.zip?rlkey=vc253rogq2gxdqearqrhv1ytf&dl=0"

unzip home/data/MNIST_CSV.zip -d home/data/MNIST_CSV

# Create folder challenge data
mkdir -p home/data/challenge

wget -O home/data/challenge/challenge_train.csv \
"https://www.dropbox.com/scl/fi/shp2qvk6yoia5wyp21gev/challenge_train.csv?rlkey=5v4yt1nj2fca5hqafhiu22444&st=pciyaa5b&dl=0"

wget -O home/data/challenge/challenge_test.csv \
"https://www.dropbox.com/scl/fi/gszitamicqvjv42esbgvu/challenge_test.csv?rlkey=0p20v2lpext07g5jqe6miamwf&st=pdaqaclz&dl=0"