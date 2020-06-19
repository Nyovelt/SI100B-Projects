import math
import re

INTEGER, FLOAT, TERM, LPAR, RPAR = (
	'INTEGER', 'FLOAT', 'TERM', '(', ')'
)


class Syntax:
	'''
		return a list of Token(type, value)
		for example:
				[['(', '('], ['TERM', '+'], ['(', '('], ['TERM', 'sin'], ['(', '('], 
				['FLOAT', '1)'], [')', ')'], [')', ')'], ['(', '('], ['TERM', 'neg'], 
				['(', '('], ['INTEGER', '2))'], [')', ')'], [')', ')'], [')', ')']]
	'''

	def charsToSyntaxes(symbols: list):
        # print(symbols)
		tmp = list()
		res = list()
		for i in symbols:
			while( i[0] == '(' ):
				res.append([LPAR, '('])
				i = i[1:]
				if i in ['numi']:
					res.append([INTEGER, 'num'])
				elif i in ['numf']:
					res.append([FLOAT, 'num'])
				elif i in ['neg', 'cos', 'sin', 'exp', 'apply', 'lambda', '+', '-', '*', 'pow']:
					res.append([TERM, i])
				elif re.match(r'[a-z]+', i):
					res.append([TERM, i])
			while (i[-1] == ')'):
				tmp.append([RPAR, ')'])
				i = i[:-1]
				if (res[-1][1] == 'num'):
					res[-1][1] = i
				elif i in ['neg', 'cos', 'sin', 'exp', 'apply', 'lambda', '+', '-', '*', 'pow']:
					res.append([TERM, i])
				elif re.match(r'[a-z]+', i):
					res.append([TERM, i])
				res.extend(tmp)
				tmp = list()
		print(res)


class EvaluationContext:
    # implement your evaluation context here
    def __init__(self, prev):
        # implement your evaluation context initialization here
        self.prev = prev
        self.list = list()

    def store(self, name, value):
        # implement your variable store logic here
        self.list.append((name,value))

    def load(self, name):
        # implement your variable retrieve logic here
        # return None if no value is associated with the name
        for i in self.list:
            if i[0] == name:
                return i[1]
        if (self.prev):
            return self.prev.load(name)
        return None


    def push(self):
        # implement your context stacking logic here
        return EvaluationContext(self)

    def pop(self):
        # implement your context destacking logic here
        return EvaluationContext(self.prev)

class ASTNode:
        pass


class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.token = op

class UOp(ASTNode):
    def __init__(self, left, op):
        self.left = left
        self.token = op

class Num(ASTNode):
    def __init__(self, token):
        self.token = token[0]
        self.value = token[1]


class AST:
    # implement your AST here
	def syntaxesToAST(syntaxes:list):
		return AST.evaluate(list)

	def evaluate(self, eval_context): 
		if eval_context[0][0] == RPAR:
			return None
		if eval_context[0][0] == LPAR:
			return self.evaluate(eval_context[1:])
		if eval_context[0][0] == TERM:
			if eval_context[0][1] in ['+', '-', '*', 'pow']:
				node = self.evaluate(eval_context[1:]
				return BinOp(left=node, op=eval_context[0][1], right=None)
			if eval_context[0][1] in ['neg', 'cos', 'sin', 'exp']:
				return UOp(left=self.evaluate(eval_context[1:]), op=eval_context[0][1] )


class Evaluator:

    def getInputAsChars(self):
        ''' 
                return a list
        '''
        f = open("input.txt", "r+")
        input = f.readline().split(" ")
        print(input)
        return input

    def evaluate(self):
        chars = self.getInputAsChars()
        syntaxes = Syntax.charsToSyntaxes(chars)
        # ast = AST.syntaxesToAST(syntaxes)
        # ec = EvaluationContext(None)
        # return ast.evaluate(ec)
        return ast

    def stringifyResult(self, result: ASTNode):
        if result.token = '+':
            return self.stringifyResult(result.left) + self.stringifyResult(result.right)
        if result.token = '-':
            return self.stringifyResult(result.left) - self.stringifyResult(result.right)
        if result.token = '*':
            return self.stringifyResult(result.left) * self.stringifyResult(result.right)
        if result.token = 'pow':
            return self.stringifyResult(result.left)**self.stringifyResult(result.right)
        if result.token = 'neg':
            return - self.stringifyResult(result.left)
        if result.token = 'cos':
            return cos(self.stringifyResult(result.left))
        if result.token = 'sin':
            return sin(self.stringifyResult(result.left))

            

    def writeOutput(self, s):
        # store your output to required file here
        pass


if __name__ == "__main__":
    evaluator = Evaluator()
    result = evaluator.evaluate()
    s = evaluator.stringifyResult(result)
    evaluator.writeOutput(s)
