Image upload with Flask
=======================

No database, no additional features. Plain and simple image upload.

Use the Docker image
--------------------

Simply allocate a data directory and create the thumbnails
sub-directory:

    mkdir -p /path/to/data/thumbnails

Then run the image server:

    docker run --name=tedimg -d -v /path/to/data:/data kaiyou/tedimg

Build from source
-----------------

NodeJS and NPM are required to build from source :

    git clone git@github.com:kaiyou/tedimg.git
    cd tedimg
    npm install
    gulp
    docker build
