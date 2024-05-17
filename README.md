## Play around a bit with EDA and ML

In this repository I will collect some Jupyter notebooks with small Exploratory Data Analysis and Machine Learning projects that interest me.

---

### 01_take_me_home_challenge_EDA.ipynb ...
... contains a brief analysis of a data set about students. The main focus was on finding out which group of students passed an important test and which did not. I described my approach within the notebook. 

---

### 02_happiness_index_part1_basemodel.ipynb

Part of my final project. I calculated a model for the prediction of the Happiness Index. I tested a few algorithms to find out which models perform best for the model with only one feature. The test was done with loops, with the help of which I could change parameters to see the influence of these on the performance. At the end, I compare the best models with each other and decide which algorithm I will continue to use. I have provided the notebook with short notes on my procedure. 

---

### 03_happiness_index_part2_finalmodel.ipynb

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