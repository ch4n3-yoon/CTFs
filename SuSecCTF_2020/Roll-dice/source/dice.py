import random


def get_de(de):
	if type(de) == int:
		return DiceNumber(de)
	return de


class DiceExpression:
	def __init__(self):
		pass

	def calc(self):
		raise Exception("Unknown Expression")

	def __add__(self, x):
		return DiceAdd(self, get_de(x))

	def __radd__(self, x):
		return DiceAdd(self, get_de(x))

	def __sub__(self, x):
		return DiceSub(self, get_de(x))

	def __rsub__(self, x):
		return DiceSub(self, get_de(x))

	def __mul__(self, x):
		return DiceMult(self, get_de(x))

	def __rmul__(self, x):
		return DiceMult(get_de(x), self)


class DiceNumber(DiceExpression):
	def __init__(self, num):
		self.num = num

	def calc(self):
		return self.num


class DiceOp(DiceExpression):
	def __init__(self, lhs, rhs):
		self.lhs = lhs
		self.rhs = rhs


class DiceAdd(DiceOp):
	def calc(self):
		return self.lhs.calc() + self.rhs.calc()


class DiceSub(DiceOp):
	def calc(self):
		return self.lhs.calc() - self.rhs.calc()


class DiceMult(DiceOp):
	def calc(self):
		return sum((self.rhs.calc() for _ in range(self.lhs.calc())))


class DiceRandom(DiceExpression):
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def calc(self):
		return random.randint(self.a, self.b)


class DiceList(DiceExpression):
	def __init__(self, ls):
		self.ls = ls


class DiceListMax(DiceList):
	def calc(self):
		return max([d.calc() for d in self.ls])


class DiceListMin(DiceList):
	def calc(self):
		return min([d.calc() for d in self.ls])


d4 = DiceRandom(1, 4)
d6 = DiceRandom(1, 6)
d8 = DiceRandom(1, 8)
d10 = DiceRandom(0, 9)
d12 = DiceRandom(1, 12)
d20 = DiceRandom(1, 20)
d100 = d10 * 10


def advantage(de, num=2):
	return DiceListMax([de for _ in range(num)])


def disadvantage(de, num=2):
	return DiceListMin([de for _ in range(num)])


def roll(de):
	return get_de(get_de(de).calc())
