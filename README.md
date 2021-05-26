# MLProjectTemplate

This is the Cortex Logic project directory template for machine learning projects.

Give an overview of this project and the basic usage of the code.

## Overview

```
.
├── config                       <- project configuration files
│   └── github_labels.yaml       <- labels for github issues
├── data
│   ├── external                 <- third party data
│   ├── interim                  <- intermediate data
│   ├── processed                <- data ready for modelling
│   └── raw                      <- original, immutable data
├── dev
│   ├── notebooks
│   │   ├── notebook2script.py   <- paste notebook cells to script
│   │   ├── run_notebook.py      <- run notebook from command line
│   │   └── *.ipynb              <- Jupyter Notebook for exploring, dev or reporting
│   └── *.py                     <- dev code
├── docs                         <- documentation files
├── models                       <- place to store trained models and associated files.
├── README.md                    <- Overview of project
├── reports                      <- Generated content from analysis
│   └── figures                  <- graphics used for reporting
├── requirements.txt             <- minimal set of dependencies required to use `src`
├── setup.py                     <- Instructions to make `src` code pip installable
├── src                          <- Source code for use in this project and outside
│   └── __init__.py              <- Makes a Python module
├── tools                        <- Software utilities
│   └── label_config.py          <- Add labels to github script
└── .pre-commit-config.yaml      <- Pre-commit hooks configuration file
```

### Extras

- `dev` can further be divided into useful directories, *e.g.* for specific experiments or explorations.
- `models` and `data` won't be version controlled by git. See DVC.

## Usage

To create a new repo in Github with this structure, all you need to do is to select `cortexlogic/template` under *Repository template* when in the *Create a new repository* screen. Another option is to click on the green *use this template* button at the home screen of this repo and follow the steps.

### Labels setup

To configure the repo with predefined labels run:

```
python tools/label_config.py
```

This will look for the remote url, grab the repo name and populate that repo with the labels defined in [config/github_labels.yaml](config/github_labels.yaml). Note that you will need the `python-dotenv`, `requests` and `pyyaml` libraries installed (with pip).

The github authentication is done with the token (`GITHUB_TOKEN`) specified in the `.env` file. So please change it to yours (you can find it under your github user developer settings). The `.env` file is part of the gitignore but we did a add a `.env.example` than can be used as a template.

### Branch Naming and Pre-Commit Hooks

Branches should be named in the following format: `branch_goal-ABC-123-03` where `ABC-123` is a Jira-tag and `03` is a Github issue.

We use git pre-commit hooks to enable JIRA integration. JIRA tags and git issue numbers (retrieved from branch name) gets appended to commit messages on a new line. To set this up for the first time, run in the base of your project:

```
pip install pre-commit
pre-commit install --hook-type commit-msg
pre-commit autoupdate
```
And then you can start committing. For more info see [here](https://github.com/cortexlogic/git-hooks).
