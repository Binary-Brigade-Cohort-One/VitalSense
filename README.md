# VitalSense

Summer Project VitalSense

## Development - Initial Setup

This project is using Flask which requires python. Here are some general guidance on how to get the project set up locally to start developing.

### Setting up the virtual environment and installing Flask

Make sure you have python installed [^python]. This project uses python version: 3.10.11

Once you have cloned the repo locally. Go into the `VitalSense` project folder and run the following commands to set up the virtual environment. Most of the instructions are directly from [Flask intallation page](https://flask.palletsprojects.com/en/2.3.x/installation/).

First, you want to set up the virtual environment with the following command in the terminal (*I use gitbash as my termial*)[^git].

``` terminal
> py -3 -m venv .venv
```

this should result in a new folder being created in the main directory called `.venv`. Now to use the virtual environment run the following command. This can differ with different terminals used. List of different commands to activate listed [here](https://www.infoworld.com/article/3239675/virtualenv-and-venv-python-virtual-environments-explained.html).

``` terminal
source ./.venv/Scripts/activate
```

Once the virtual environment is working properly, you should be able to see either a indication at the beginning of the terminal like showing `.venv` or if you the following command you should be the file path of the virtual environment.

``` terminal
which pip
```

The should look something like this `...\VitalSense\.venv/Scripts/pip` at the end. Alright, now that the virtual environment is looking good. Now it is time to get the required libraries installed. It should all be listed in the `requirements.txt` file and you just need to run the following command. 

``` terminal
pip install -r requirements.txt
```

[^git]: Use the following link to download [git and gitbash](https://git-scm.com/downloads).
[^python]: Use the following link to download [python](https://www.python.org/downloads/). Download version 3.10.11.
