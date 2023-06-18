#author: Anshul Jagtap


# importing stack to use it in this class
from stack import Stack


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    # accepting the value for leftchild 
    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        left = ''
        right = ''
        if self.leftChild:
            left = str(self.leftChild)
        if self.rightChild:
            right = str(self.rightChild)
        return f'{self.key}({left})({right})'

# ExpTree subclass of BinaryTree 
class ExpTree(BinaryTree):
    def __init__(self, token):
        BinaryTree.__init__(self, token)

    @staticmethod
    def make_tree(postfix):
        stack = Stack()
        operators = set(['+', '-', '*', '/', '^'])
        for char in postfix:
            if char not in operators:
                t = ExpTree(char)
                stack.push(t)
            else:
                t = ExpTree(char)
                t1 = stack.pop()
                t2 = stack.pop()
                t.rightChild = t1
                t.leftChild = t2
                stack.push(t)
        t = stack.pop()
        return t

    def __str__(self):
        if self.leftChild and self.rightChild:
            return '(' + str(self.leftChild) + str(self.key) + str(self.rightChild) + ')'
        else:
            return str(self.key)

    # preorder function 
    @staticmethod
    def preorder(tree):
        s = ''
        if tree:
            s += str(tree.key)  
            s += ExpTree.preorder(tree.leftChild)
            s += ExpTree.preorder(tree.rightChild)
        return s

    @staticmethod
    def postorder(tree):
        s = ''
        if tree:  
            s += ExpTree.postorder(tree.leftChild)
            s += ExpTree.postorder(tree.rightChild)
            s += str(tree.key)
            
        return s

    @staticmethod
    def inorder(tree):

        s = ''
        if tree:
            if tree.leftChild or tree.rightChild:
                s += '('
            s += ExpTree.inorder(tree.leftChild)
            s += str(tree.key)
            s += ExpTree.inorder(tree.rightChild)
            
            if tree.leftChild or tree.rightChild:
                s += ')'
        return s

    @staticmethod
    def evaluate(tree):
        if tree.leftChild and tree.rightChild:
            fn = ExpTree.operate(tree.key)
            return fn(ExpTree.evaluate(tree.leftChild), ExpTree.evaluate(tree.rightChild))
        else:
            return float(tree.key)

    # using operator for evaluating the calculations 
    @staticmethod
    def operate(op):
        if op == '+':
            return lambda x, y: x + y
        elif op == '-':
            return lambda x, y: x - y
        elif op == '*':
            return lambda x, y: x * y
        elif op == '/':
            return lambda x, y: x / y
        elif op == '^':
            return lambda x, y: x ** y



# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'
    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'
    
    # test an ExpTree
    
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0
    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
    