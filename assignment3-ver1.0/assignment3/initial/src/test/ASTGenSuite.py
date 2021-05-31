import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Let x;"""
        expect = str(Program([VarDecl(Id("x"),[],NoneType(),None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    
   