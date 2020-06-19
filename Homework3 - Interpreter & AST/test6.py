from math import sin, cos
import re

INTEGER, FLOAT, TERM, LPAR, RPAR = (
	'INTEGER', 'FLOAT', 'TERM', '(', ')'
)

NUMI, NUMF = (
    0,1
)

datatype = NUMI

class Syntax:
    # implement your syntaxes here
    # ... or derive subclasses and implement there
    def charsToSyntaxes(symbols):
        # tmp = list()
        # res = list()
        # for i in symbols:
        #     while( i[0] == '(' ):
        #         res.append([LPAR, '('])
        #         i = i[1:]
        #         if i in ['numi']:
        #             res.append([INTEGER, 'num'])
        #         elif i in ['numf']:
        #             res.append([FLOAT, 'num'])
        #         elif i in ['neg', 'cos', 'sin', 'exp', 'apply', 'lambda', '+', '-', '*', 'pow']:
        #             res.append([TERM, i])
        #         elif re.match(r'[a-z]+', i):
        #             res.append([TERM, i])
        #     while (i[-1] == ')'):
        #         tmp.append([RPAR, ')'])
        #         i = i[:-1]
        #         if (res[-1][1] == 'num'):
        #             res[-1][1] = i
        #         elif i in ['neg', 'cos', 'sin', 'exp', 'apply', 'lambda', '+', '-', '*', 'pow']:
        #             res.append([TERM, i])
        #         elif re.match(r'[a-z]+', i):
        #             res.append([TERM, i])
        #         res.extend(tmp)
        #         tmp = list()
        print(symbols)
        return symbols

class EvaluationContext:
    # implement your evaluation context here
    def __init__(self, prev):
        # implement your evaluation context initialization here
        pass
    def store(self, name, value):
        # implement your variable store logic here
        pass
    def load(self, name):
        # implement your variable retrieve logic here
        # return None if no value is associated with the name
        pass
    def push(self):
        # implement your context stacking logic here
        pass
    def pop(self):
        # implement your context destacking logic here
        pass
    pass

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
        self.right = None
        self.token = op

class Num(ASTNode):
    def __init__(self, value):
        self.type = 'num'
        self.value = self.token = value
        self.left = self.right = None

def countPAR(syntaxes):
    '''
        i is the index
        j is the ( num
        k is the ) num
    '''
    i=0
    j = 1
    k=0
    while (j!=k):
        i += 1
        if syntaxes[i] == '(':
            j += 1
        if syntaxes[i] == ')':
            k += 1

    return i
    
    

def Tree(syntaxes):
    # print(syntaxes)
    if syntaxes[0] == '(':
        return Tree(syntaxes[1:])
    if syntaxes[0] == ')':
        return None
    if syntaxes[0] in ['+', '-', '*', 'pow']:
        i = countPAR(syntaxes[1:])
        # print("i=", i)
        # print(syntaxes[i+2: ])
        return BinOp(op=syntaxes[0], left=Tree(syntaxes[2:]), right=Tree(syntaxes[i+2: ]))
    if syntaxes[0] in ['sin', 'cos', 'exp']:
        global datatype
        datatype = NUMF
        return UOp(op=syntaxes[0], left=Tree(syntaxes[1:]))
    if syntaxes[0] in ['neg']:
        return UOp(op=syntaxes[0], left=Tree(syntaxes[1:]))
    if syntaxes[0] in ['numi']:
        return Num(value = int(syntaxes[1]))
    if syntaxes[0] in ['numf']:
        global datatype
        datatype = NUMF
        return Num(value = float(syntaxes[1]))

def printAST(AST):
    print(AST.token)
    if(AST.left != None):
        printAST(AST.left)
    if(AST.right != None):
        printAST(AST.right)

def evaluate(node):
    if node.token == '+':
        return  evaluate(node.left) +  evaluate(node.right)
    if node.token == '-':
        return  evaluate(node.left) -  evaluate(node.right)
    if node.token == '*':
        return  evaluate(node.left) *  evaluate(node.right)
    if node.token == 'pow':
        return  evaluate(node.left)** evaluate(node.right)
    if node.token == 'sin':
        return sin( evaluate(node.left))
    if node.token == 'cos':
        return cos( evaluate(node.left))
    if node.token == 'neg':
        return - ( evaluate(node.left))
    if node.type == 'num':
        return node.value


class AST:
    # implement your AST here
    def syntaxesToAST(syntaxes):
        return Tree(syntaxes)

    # def evaluate(node: ASTNode, eval_context = None):
    #     if node.token == '+':
    #         return AST.evaluate(node.left) + AST.evaluate(node.right)
    #     if node.token == '-':
    #         return AST.evaluate(node.left) - AST.evaluate(node.right)
    #     if node.token == '*':
    #         return AST.evaluate(node.left) * AST.evaluate(node.right)
    #     if node.token == 'pow':
    #         return AST.evaluate(node.left)**AST.evaluate(node.right)
    #     if node.token == 'sin':
    #         return sin(AST.evaluate(node.left))
    #     if node.token == 'cos':
    #         return cos(AST.evaluate(node.left))
    #     if node.token == 'neg':
    #         return - (AST.evaluate(node.left))
    #     if node.value.isdigit():
    #         return node.value
        
        

class Evaluator:
    # implement your evaluator here
    def getInputAsChars(self):
        # retrieve the input as characters from the input file here
        # ... generator is greatly recommended.
        f = open("input.txt", "r+")
        input = f.readline().replace('(', ' ( ').replace(')',' ) ').split()
        print(input)
        return input

    def evaluate(self):
        global datatype
        chars = self.getInputAsChars()
        syntaxes = Syntax.charsToSyntaxes(chars)
        print(datatype)
        ast = AST.syntaxesToAST(syntaxes)
        ec = EvaluationContext(None)
        # printAST(ast)
        # print(ast.right.token)
        return evaluate(node = ast)

    def stringifyResult(self, result):
        print(datatype)
        if datatype == NUMI:
            return '(numi ' + str(int(result)) + ')'
        if datatype == NUMF:
            return '(numf ' +  '%.5f' % result + ')'
    def writeOutput(self, s):
        f = open("output.txt", "w+")
        f.writelines(s)


if __name__ == "__main__":
    evaluator = Evaluator()
    result = evaluator.evaluate()
    s = evaluator.stringifyResult(result)
    print(s)
    evaluator.writeOutput(s)
