import math

INTEGER, FLOAT, TERM, LPAR, RPAR = (
	'INTEGER', 'FLOAT', 'TERM', '(', ')'
)

NUMI, NUMF, = (
    'numi', 'numf',
)

lambda_flag = 0
apply_flag = 0

global datatype
datatype = NUMI

class Syntax:
    def charsToSyntaxes(symbols):
        print(symbols)
        return symbols

class EvaluationContext:
    # implement your evaluation context here
    def __init__(self, prev):
        # implement your evaluation context initialization here
        self.prev = prev
        self.list = list()

    def store(self, name, value):
        # implement your variable store logic here
        for i in self.list:
                if i[0] == name:
                        i[1] = value
                        return 
        
        self.list.append([name,value])

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

class BinOp():
    def __init__(self, left, op, right):
        self.type = 'BinOp'
        self.left = left
        self.right = right
        self.token = op

class UOp():
    def __init__(self, left, op):
        self.type = 'UOp'
        self.left = left
        self.right = None
        self.token = op

class Num():
    def __init__(self, value, type = 'num'):
        self.type = type
        self.value = self.token = value
        self.left = self.right = None

def countPAR(syntaxes):
    '''
        i is the index
        j is the ( num
        k is the ) num
    '''
    i = 0
    j = 1
    k= 0
    while (j!=k):
        i += 1
        if syntaxes[i] == '(':
            j += 1
        if syntaxes[i] == ')':
            k += 1

    return i
    
def judge(syntaxes):
    if syntaxes[0] != '(':
        return Num(value=syntaxes[0], type='var')
    else:
        return Tree(syntaxes)

def Tree(syntaxes):
    # print(syntaxes)
    if syntaxes[0] == '(':
        return Tree(syntaxes[1:])

    if syntaxes[0] == ')':
        return None

    if syntaxes[0] == 'apply':
        if syntaxes[1] == ')':
            return Num(value = syntaxes[0], type='var')
        
        tmp = (syntaxes[1:])
        tmp.insert(0,'identifier')
        global apply_flag
        apply_flag = 1
        return BinOp(op = syntaxes[0], left = Tree(tmp), right = Tree(syntaxes[ syntaxes[1:].index('lambda')  :]))
    
    if syntaxes[0] == 'identifier':
        if syntaxes[1] == ')':
            return Num(value = syntaxes[0], type='var')
        return BinOp(op = syntaxes[0], left = Num(value = syntaxes[1], type='var'), right = judge(syntaxes[2:]))    

    if syntaxes[0] == 'lambda':
        if syntaxes[1] == ')':
            return Num(value = syntaxes[0], type='var')
        
        return BinOp(op = syntaxes[0], left=Num(value = syntaxes[1], type='var'), right= judge(syntaxes[2:]))

    if syntaxes[0] in ['+', '-', '*', 'pow']:
        if syntaxes[1] == '(':
            i = countPAR(syntaxes[1:])
            return BinOp(op=syntaxes[0], left=Tree(syntaxes[2:]), right=Tree(syntaxes[i+2: ]))
        if syntaxes[1] == ')':
            return Num(value = syntaxes[0], type='var')
        return BinOp(op=syntaxes[0], left=Num(value = syntaxes[1], type='var'), right=Tree(syntaxes[2: ]))

    if syntaxes[0] in ['sin', 'cos', 'exp']:
        if syntaxes[1] == ')':
            return Num(value = syntaxes[0], type='var')
        global datatype
        datatype = NUMF
        return UOp(op=syntaxes[0], left=Tree(syntaxes[1:]))

    if syntaxes[0] in ['neg']:
        if syntaxes[1] == ')':
            return Num(value = syntaxes[0], type='var')
        return UOp(op=syntaxes[0], left=Tree(syntaxes[1:]))

    if syntaxes[0] in ['numi']:
        if syntaxes[1] == ')':
            return Num(value = syntaxes[0], type='var')
        return Num(value = int(syntaxes[1]))

    if syntaxes[0] in ['numf']:
        if syntaxes[1] == ')':
            return Num(value = syntaxes[0], type='var')
        datatype = NUMF
        return Num(value=float(syntaxes[1]))

    return Num(value = syntaxes[0], type='var')

def printAST(AST):
    print(AST.token , AST.type)
    if(AST.left != None):
        print('left: ', end='')
        printAST(AST.left)
    if(AST.right != None):
        print('right: ', end='')
        printAST(AST.right)

def replace(origin_value, target_value, target_type, node):
    if node.type == 'var' and  node.value==origin_value :
        node.type = target_type
        node.token = node.value = target_value
    if(node.left != None):
        replace(origin_value, target_value, target_type, node.left)
    if(node.right != None):
        replace(origin_value, target_value, target_type, node.right)
    

class AST:
    # implement your AST here
    def syntaxesToAST(syntaxes):
        return Tree(syntaxes)

    def evaluate(node, eval_context=None):
        if node.type == 'var':
            global lambda_flag
            lambda_flag = 1
            return node.value


        if node.token == 'apply':
            replace(node.left.left.value, node.left.right.value, node.left.right.type, node.right.right)
            print('replaced')
            printAST(node)
            # printAST(node.right)
            return AST.evaluate(node.right)
            

        if node.token == 'lambda':
            # return '(lambda '+ AST.evaluate(node.left) + ' ' +  AST.evaluate(node.right) + ')'
            if apply_flag == 1 and type(AST.evaluate(node.right)) != str:
                return stringify(AST.evaluate(node.right))
            if apply_flag == 1 and type(AST.evaluate(node.right)) == str:
                return AST.evaluate(node.right)
                
            if type(AST.evaluate(node.left)) == str and type(AST.evaluate(node.right)) != str:
                return '(lambda ' + AST.evaluate(node.left) + ' ' + stringify(AST.evaluate(node.right)) + ')'

            if type(AST.evaluate(node.left)) != str and type(AST.evaluate(node.right)) == str:
                return '(lambda ' + stringify(AST.evaluate(node.left)) + ' ' + AST.evaluate(node.right) + ')'

            if type(AST.evaluate(node.left)) != str and type(AST.evaluate(node.right)) != str:
                print('yo')
                return (AST.evaluate(node.left)) +  AST.evaluate(node.right) 

            return '(lambda '+ AST.evaluate(node.left) + ' ' +  AST.evaluate(node.right) + ')'


        if node.token == '+':

            if type(AST.evaluate(node.left)) == str and type(AST.evaluate(node.right)) == str:
                return '(+ ' + AST.evaluate(node.left) + ' ' + (AST.evaluate(node.right)) + ')'

            if type(AST.evaluate(node.left)) == str and type(AST.evaluate(node.right)) != str:
                return '(+ ' + AST.evaluate(node.left) + ' ' + stringify(AST.evaluate(node.right)) + ')'

            if type(AST.evaluate(node.left)) != str and type(AST.evaluate(node.right)) == str:
                return '(+ ' + stringify(AST.evaluate(node.left)) + ' ' + AST.evaluate(node.right) + ')'

            return AST.evaluate(node.left) + AST.evaluate(node.right)
            

        if node.token == '-':
            if type(AST.evaluate(node.left)) == str and type(AST.evaluate(node.right)) == str:
                return '(- ' + AST.evaluate(node.left) + ' ' + (AST.evaluate(node.right)) + ')'

            if type(AST.evaluate(node.left)) == str and type(AST.evaluate(node.right)) != str:
                return '(- ' + AST.evaluate(node.left) + ' ' + stringify(AST.evaluate(node.right)) + ')'

            if type(AST.evaluate(node.left)) != str and type(AST.evaluate(node.right)) == str:
                return '(- ' + stringify(AST.evaluate(node.left)) + ' ' + AST.evaluate(node.right) + ')'

            return   AST.evaluate(node.left) -   AST.evaluate(node.right)


        if node.token == '*':

            if type(AST.evaluate(node.left)) == str and type(AST.evaluate(node.right)) == str:
                return '(* ' + AST.evaluate(node.left) + ' ' + (AST.evaluate(node.right)) + ')'

            if type(AST.evaluate(node.left)) == str and type(AST.evaluate(node.right)) != str:
                return '(* ' + AST.evaluate(node.left) + ' ' + stringify(AST.evaluate(node.right)) + ')'

            if type(AST.evaluate(node.left)) != str and type(AST.evaluate(node.right)) == str:
                return '(* ' + stringify(AST.evaluate(node.left)) + ' ' + AST.evaluate(node.right) + ')'

            return   AST.evaluate(node.left) *   AST.evaluate(node.right)


        if node.token == 'pow':
            if type(AST.evaluate(node.left)) == str and type(AST.evaluate(node.right)) == str:
                return '(pow ' + AST.evaluate(node.left) + ' ' + (AST.evaluate(node.right)) + ')'

            if type(AST.evaluate(node.left)) == str and type(AST.evaluate(node.right)) != str:
                return '(pow ' + AST.evaluate(node.left) + ' ' + stringify(AST.evaluate(node.right)) + ')'

            if type(AST.evaluate(node.left)) != str and type(AST.evaluate(node.right)) == str:
                return '(pow ' + stringify(AST.evaluate(node.left)) + ' ' + AST.evaluate(node.right) + ')'
            print(AST.evaluate(node.left) **  AST.evaluate(node.right))
            return   AST.evaluate(node.left) **  AST.evaluate(node.right)


        if node.token == 'sin':

            if type(AST.evaluate(node.left)) == str:
                return '(sin '+ AST.evaluate(node.left)+')'

            return math.sin(  AST.evaluate(node.left))


        if node.token == 'exp':

            if type(AST.evaluate(node.left)) == str:
                return '(exp '+ AST.evaluate(node.left)+')'
            return math.exp(  AST.evaluate(node.left))

        if node.token == 'cos':

            if type(AST.evaluate(node.left)) == str:
                return '(cos '+ AST.evaluate(node.left)+')'
            return math.cos(  AST.evaluate(node.left))


        if node.token == 'neg':

            if type(AST.evaluate(node.left)) == str:
                return '(neg '+ AST.evaluate(node.left)+')'

            return - (AST.evaluate(node.left))

            
        if node.type == 'num':
            return node.value




def stringify(result):
    print('result: ',result)
    global datatype

    if datatype == NUMI:
        return '(numi ' + str(int(result)) + ')'
    if datatype == NUMF:
        return '(numf ' +  '%.5f' % result + ')'


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
        ast = AST.syntaxesToAST(syntaxes)
        printAST(ast)
        ec = EvaluationContext(None)
        node = ast
        # printAST(ast)
        # print(ast.right.token)
        return AST.evaluate(ast, ec)

    def stringifyResult(self, result):
        print('result: ', result)
        print(lambda_flag)
        global datatype
        if lambda_flag or apply_flag:
            return result
        if datatype == NUMI:
            return '(numi ' + str(int(result)) + ')'
        if datatype == NUMF:
            return '(numf ' + '%.5f' % result + ')'
    def writeOutput(self, s):
        f = open("output.txt", "w+")
        f.writelines(s)


if __name__ == "__main__":
    evaluator = Evaluator()
    result = evaluator.evaluate()
    print(result)
    s = evaluator.stringifyResult(result)

    evaluator.writeOutput(s)
