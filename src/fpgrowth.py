# -*- encoding:utf-8 -*-

from optparse import OptionParser
import csv

class FPTree(object):
	def __init__(self):
		self.root = FPNode(self, None, None)	

	def root(self):
		return self.root

	def add(self, transaction):
		current = self.root


class FPNode(object):
	def __init__(self, tree, item, count=1):
		self.tree = tree
		self.item = item
		self.count = count
		self.parent = None
		self.children = {}

	def addChild(self, child):
		if not child.item in self.children:
			self.children[child.item] = child
			child.parent = self

	def search(self, item):	
		if item in self.children.keys():
			return self.children[item]
		else 
			return None

	@property
	def get_item(self):
		return self.item

	@property
	def get_count(self):
		return self.count

	def inc_count(self):
		self.count += 1

	@property
	def is_root(self):
		return self.item is None and self.count is None

	@property
	def is_leaf(self):
		return len(self.children) == 0

if __name__ == '__main__':
