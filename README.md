
# Gardener Management App

This project runs a CLI menu that lets you interact with data related to gardeners. You may list gardenres, update, add, and delete gardeners that persist in the backend. 

When a single gardener is chosen, a list of their plants is displayed as well as the options to add, delete, and update each plant. 

## To Use
Clone the repository git clone https://github.com/StopScreenSharing/python-p3-v2-final-project-template
cd to python-p3-v2-final-project-template/lib
pipenv install
pipence shell

run python cli.py

from main menu:
-Manage gardeners(add, update, delete, or select one)
-Manage plants associated with a gardener



## cli.py
File where the cli loop is. Runs through options such as manage gardeners and exit, and then proceeds to other menus based on choices user inputs.

## helpers.py
Helper functions to run the CLI 

## gardener.py and plant.py
The two models of this app. gardeners.py initializes the Gardener class and plant.py initializes the Plant class.



