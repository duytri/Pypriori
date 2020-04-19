# Pypriori
An inplementation of Apriori algorithm [1] in Python.

## Installation

```bash
git clone https://github.com/duytri/Pypriori.git
cd Pypriori
python setup.py install
```
or using pip
```bash
cd Pypriori
pip install ./
```

## How to use
1. Input dataset

```python
data = [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
```

2. Initialize Apriori class

```python
alg = APRIORI(data, minSupport=0.5)
```

3. Discover frequent pattern

```python
freqItems, suppData = alg.apriori()
```

4. Generate rules

```python
assocRules = AssociationRules(freqItems, suppData, minConfidence=0.5)
ruleList = assocRules.generateRules()
assocRules.printRules(ruleList)

Output: 
>>> Rule: [3] ==> [5] [0.5, 0.6666666666666666]
>>> Rule: [5] ==> [3] [0.5, 0.6666666666666666]
>>> Rule: [2] ==> [5] [0.75, 1.0]
>>> Rule: [5] ==> [2] [0.75, 1.0]
>>> Rule: [2] ==> [3] [0.5, 0.6666666666666666]
>>> Rule: [3] ==> [2] [0.5, 0.6666666666666666]
>>> Rule: [1] ==> [3] [0.5, 0.6666666666666666]
>>> Rule: [3] ==> [1] [0.5, 1.0]
>>> Rule: [2] ==> [3, 5] [0.5, 1.0]
>>> Rule: [3] ==> [2, 5] [0.5, 0.6666666666666666]
>>> Rule: [5] ==> [2, 3] [0.5, 1.0]
>>> Rule: [2, 3] ==> [5] [0.5, 0.6666666666666666]
>>> Rule: [2, 5] ==> [3] [0.5, 0.6666666666666666]
>>> Rule: [3, 5] ==> [2] [0.5, 0.6666666666666666]
```

# Reference
1. Rakesh Agrawal and Ramakrishnan Srikant Fast algorithms for mining association rules. Proceedings of the 20th International Conference on Very Large Data Bases, VLDB, pages 487-499, Santiago, Chile, September 1994.
