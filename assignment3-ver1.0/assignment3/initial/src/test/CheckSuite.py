import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):

    def test_0(self):
        """Simple program: main"""
        input = """Let x;
        """
        expect = "" #str(Undeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 0))

    # def test_undeclared_function(self):
    #     """Simple program: main"""
    #     input = """Function main() {
    #         Call(foo, []);
    #     }
    #     """
    #     expect = "" #str(Undeclared(Function(), "foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 1))

    # def test_diff_numofparam_stmt(self):
    #     """Complex program"""
    #     input = """Function main() {
    #         Call(printStrLn, [])
    #     }"""
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
    #     self.assertTrue(TestChecker.test(input, expect, 2))

    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function main() {
    #         Call(printStrLn, [Call(read, [4])])
    #     }
    #     """
    #     expect = str(TypeMismatchInExpression(
    #         CallExpr(Id("read"), [IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input, expect, 3))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"), [], ([], [
    #         CallExpr(Id("foo"), [])]))])
    #     expect = str(Undeclared(Function(), "foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 4))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #         FuncDecl(Id("main"), [], ([], [
    #             CallStmt(Id("printStrLn"), [
    #                 CallExpr(Id("read"), [IntLiteral(4)])
    #             ])]))])
    #     expect = str(TypeMismatchInExpression(
    #         CallExpr(Id("read"), [IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input, expect, 5))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #         FuncDecl(Id("main"), [], ([], [
    #             CallStmt(Id("printStrLn"), [])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
    #     self.assertTrue(TestChecker.test(input, expect, 6))
