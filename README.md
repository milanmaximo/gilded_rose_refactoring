# Gilded Rose Refactoring in Python

### Requirements

* **Python3** 

### Setup

Ensure virtualenv is installed.

```
$ pip install virtualenv
```
To set up a virtualenv with python 3.6:

```  
$ cd gilded_rose_refactoring
$ python3 -m venv myvenv
$ source myvenv/bin/activate
(myvenv)$ pip install unittest
(myvenv)$ pip install coverage
```
### Test

```
$ python test_gilded_rose.py
```
```
$ python texttest_fixture.py
```

### Run html coverage 

```
$ python3 -m coverage run --branch run test_gilded_rose.py
```
```
$ python3 -m coverage html
```



## Gilded Rose Kata instructions

* [Gilded Rose](https://github.com/emilybache/GildedRose-Refactoring-Kata)
* [Gilded Rose requirements](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/master/GildedRoseRequirements.txt)

