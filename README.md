# Welcome to farm- produces

## Project Description

This is a project where gamers get to view a list of existing games in our collection, add reviews, edit (their own) reviews and also delete (their own) reviews.

## Requirements and Specifications

* node v20.0.0
* npm v9.8.1
* python v3.10
* pipenv v2023.9.8

## Setup instructions

To have this work running on your local machine:

* `git clone git@github.com:collinsln/farm-produces.git` on your terminal. Locate the folder, then open it in your preferred code editor. This walkthrough assumes you will be using Visual Studio Code.
* At the root of this directory, activate your virtual environment using `pipenv install && pipev shell` to install all the dependencies and create a virtual environment.
* Next, run the command `npm install --prefix client` to install the front end libraries
* cd into the `server` directory using the command `cd server`
* Create environment variables for your flask app by running `export FLASK_APP=app.py` and `export FLASK_RUN_PORT=5000` to have the flask application running on port 5000
* While still in the server directory, run `flask run` and this will have your back end running on port 5000
* Open another terminal instance, and run `npm start --prefix client`. This will have the front end running on port 4000

## Technologies used

* React JS for front end
* Flask for back end

## How to use

As a user, you can:

1. View a list of all the existing games in our collection
2. Sign up or sign in to get started
3. See more details of a specific game including a list of reviews for a specific game by clicking on the game card.
4. Add a review for a game upon clicking on it
5. Edit and Delete your review.
6. Sign out successfully by clicking the `Log Out` button

## Authors

collins 

## Contacts

Feel free to contact us at:

1. [collins]

## Licence

[![License:MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
Copyrigt (c) 2024 **farm produce**
