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
    
