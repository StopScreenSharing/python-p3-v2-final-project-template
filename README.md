
# Gardener Management App

This project runs a CLI menu that lets you interact with data related to gardeners. You may list gardenres, update, add, and delete gardeners that persist in the backend. 

When a single gardener is chosen, a list of their plants is displayed as well as the options to add, delete, and update each plant. 

## To Run 
To run the cli, please go into the lib folder and run cli.py from your terminal.
Type corresponding Numbers or letters to choose options.

## gardener.py and plant.py
The two models of this app. gardeners.py initializes the Gardener class and plant.py initializes the Plant class.

## helpers.py
Helper functions to run the CLI 

## cli.py
File where the cli loop is. Runs through options such as manage gardeners and exit, and then proceeds to other menus based on choices user inputs.