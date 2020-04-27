#coding: utf-8
from numpy import *
from itertools import combinations
from . import Rule

class APRIORI(object):
	def __init__(self, dataSet):
		self.dataSet = dataSet



	def createC1(self):
		C1 = []
		for transaction in self.dataSet:
			for item in transaction:
				if not [item] in C1:
					C1.append([item])
					
		C1.sort()
		return list(C1)


	def scanD(self, D, Ck):
		ssCnt = {}
		for tid in D:
			for can in Ck:
				if set(can).issubset(tid):
					if not tuple(can) in ssCnt: ssCnt[tuple(can)]=1
					else: ssCnt[tuple(can)] += 1
		numItems = float(len(D))
		retList = []
		supportData = {}
		for key in ssCnt:
			support = ssCnt[key]/numItems
			if support >= self.minSupport:
				retList.insert(0,key)
			supportData[key] = support
		return retList, supportData


	def checkSubsetFrequency(self, candidate, Lk, k):
		if k > 1:
			subsets = list(combinations(candidate, k))
		else:
			return True
		for elem in subsets:
			if not elem in Lk:
				return False
		return True


	def aprioriGen(self, Lk, k): #creates Ck
		resList = [] #result set
		candidatesK = [] 
		lk = sorted(set([item for t in Lk for item in t])) #get and sort elements from frozenset
		candidatesK = list(combinations(lk, k))
		for can in candidatesK:
			if self.checkSubsetFrequency(can, Lk, k-1):
				resList.append(can)
		return resList


	def apriori(self, minSupport):
		self.minSupport = minSupport
		C1 = self.createC1()
		D = list(self.dataSet)
		L1, supportData = self.scanD(D, C1)
		L = [L1]
		k = 2
		while (len(L[k-2]) > 0):
			Ck = self.aprioriGen(L[k-2], k)
			Lk, supK = self.scanD(D, Ck) #scan DB to get Lk
			supportData.update(supK)
			L.append(Lk)
			k += 1
		return L, supportData


class AssociationRules(object):
	def __init__(self, largeItemSet, supportData, minConfidence):
		self.largeItemSet = largeItemSet
		self.supportData = supportData
		self.minConf = minConfidence

	def generateRules(self):  #supportData is a dict coming from scanD
		bigRuleList = []
		for i in range(1, len(self.largeItemSet)): #only get the sets with two or more items
			for item in self.largeItemSet[i]: #for each item in a level
				for j in range(1, i+1): # i+1 equal to length of an item
					lhsList = list(combinations(item, j))
					for lhs in lhsList:
						rhs = set(item).difference(lhs)
						conf = self.supportData[item]/self.supportData[lhs]
						if conf >= self.minConf:
							bigRuleList.append(Rule(list(lhs),list(rhs), self.supportData[item], conf))
		return bigRuleList

	def printRules(self, ruleList):
		for rule in ruleList:
			print(rule)