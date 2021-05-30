# rock-paper-scissors-exercise

## Installation

Download this repo locally.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd my-first-python-app
```

## Setup

Setup an virtual environment:

```sh
conda create -n my-rps-game-env python=3.8
conda activate my-rps-game-env
```

Install some packages:

```sh
pip install -r requirements.txt
```

### Configuring Environment Variables

You will have to create your own local .env file. So you should add a new ".env" file to this repo, and put the following inside:


```
PLAYER_NAME="Guest 1"
```

## Usage

Run the game:

```sh
python game.py
```