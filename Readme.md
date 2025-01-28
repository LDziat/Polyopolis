
# Polyopolis Readme
This is the source code to the tool [Polyopolis](https://ldziat.pythonanywhere.com/), a basic web hosting tool with a built in theme editor.
Please feel free to push edits and make forks, but do be mindful of licensing if you wish to use the code for your own project.
## What Is This?
Honestly, I'm not too sure. I guess it's a tool to simplify web hosting for some folks, but realistically it's more a toy.

## Requirements
- Python 3
- Django
- Django Extensions
- SQLite3
- Beautiful Soup 4
- Patience

## How to get going
You should be able to simply extract the project to a directory, then use [manage.py](manage.py) to migrate, and then run the server. Ideally you would use this in conjunction with Gunicorn and Nginx, but you can use Django's built in runserver (or runsslserver if you uncomment the blocks in [settings.py](polyopolis/settings.py)) to run the server.

## Issues
The code is currently not the most well documented. Some functionality is not described correctly or clearly. There are some very sloppy portions of code that seem to work fine at a small scale but will likely cause issues at greater scales. There are also several stubs from planned functionality that may or may not be added in the future.

Overall, things work, but they don't necessarily work well. 
