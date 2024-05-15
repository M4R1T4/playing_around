## Play around a bit with EDA and ML

In this repository I will collect some Jupyter notebooks with small EDA and ML projects that interest me.

---

### take_me_home_challenge_EDA.ipynb ...
... contains a brief analysis of a data set about students. The main focus was on finding out which group of students passed an important test and which did not. I described my approach within the notebook. 

---

### Setup

Use the requirements file in this repo to create a new environment.

```BASH
make setup

#or

pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

The `requirements.txt` file contains the libraries needed for deployment.. of model or dashboard .. thus no jupyter or other libs used during development.