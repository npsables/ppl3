
import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):

    # def test_var_redeclared(self):
    #     input = """
    #     Let x; Let x;
    #     """
    #     expect = str(Redeclared(Variable(), "x"))
    #     self.assertTrue(TestChecker.test(input, expect, 1))

    # def test_func_redeclared(self):
    #     input = """
    #     Let x; Function a(){Let a;}
    #     """
    #     expect = str(Redeclared(Function(), "x"))
    #     self.assertTrue(TestChecker.test(input, expect, 2))

    # def test_var_and_const(self):
    #     input = """
    #     Let x; Constant $x;
    #     """
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.test(input, expect, 3))

    # def test_const_redeclared(self):
    #     input = """Constant $x2; Constant $x2;
    #     """
    #     expect = str(Redeclared(Constant(), "$x2"))
    #     self.assertTrue(TestChecker.test(input, expect, 4))

    # def test_2_func_redeclared(self):
    #     input = """
    #     Function foo(){} 
    #     Function foo(){}
    #     """
    #     expect = str(Redeclared(Function(), "foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 5))

    # def test_no_entry_point(self):
    #     input = """
    #     Function foo(){} 
    #     """
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.test(input, expect, 6))

    # def test_para_redeclare_1(self):
    #     input = """
    #     Function foo(b){} 
    #     Function main(){} 
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 7))

    # def test_para_redeclare_1(self):
    #     input = """
    #     Function foo(b, b){} 
    #     Function main(){} 
    #     """
    #     expect = str(Redeclared(Parameter(), "b"))
    #     self.assertTrue(TestChecker.test(input, expect, 8))

    # def test_undeclared_function(self):
    #     """Simple program: main"""
    #     input = """Function main() {
    #         Call(foo, []);
    #     }
    #     """
    #     expect = "" #str(Undeclared(Function(), "foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 9))

    # def test_diff_numofparam_stmt(self):
    #     """Complex program"""
    #     input = """Function main() {
    #         Call(printStrLn, [])
    #     }"""
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
    #     self.assertTrue(TestChecker.test(input, expect, 10))

    # def test_diff_numofparam_expr(self):
    #     """More complex program"""
    #     input = """Function main() {
    #         Call(printStrLn, [Call(read, [4])])
    #     }
    #     """
    #     expect = str(TypeMismatchInExpression(
    #         CallExpr(Id("read"), [IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input, expect, 11))

    # def test_undeclared_function_use_ast(self):
    #     """Simple program: main """
    #     input = Program([FuncDecl(Id("main"), [], ([], [
    #         CallExpr(Id("foo"), [])]))])
    #     expect = str(Undeclared(Function(), "foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 12))

    # def test_diff_numofparam_expr_use_ast(self):
    #     """More complex program"""
    #     input = Program([
    #         FuncDecl(Id("main"), [], ([], [
    #             CallStmt(Id("printStrLn"), [
    #                 CallExpr(Id("read"), [IntLiteral(4)])
    #             ])]))])
    #     expect = str(TypeMismatchInExpression(
    #         CallExpr(Id("read"), [IntLiteral(4)])))
    #     self.assertTrue(TestChecker.test(input, expect, 13))

    # def test_diff_numofparam_stmt_use_ast(self):
    #     """Complex program"""
    #     input = Program([
    #         FuncDecl(Id("main"), [], ([], [
    #             CallStmt(Id("printStrLn"), [])]))])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id("printStrLn"), [])))
    #     self.assertTrue(TestChecker.test(input, expect, 14))

    # def test_func_redeclared_15(self):
    #     input = """
    #     Let a; Function main(){Let a; Let b;}
    #     """
    #     expect = str(Redeclared(Variable(), "a"))
    #     self.assertTrue(TestChecker.test(input, expect, 15))
    
    # def test_func_redeclared_16(self):
    #     input = """
    #     Function main(){Let a; a = 1;}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 16))
    
    # def test_func_redeclared_17(self):
    #     input = """
    #     Function main(){Let a[5]: Number = [1, 2, 3, 4, 5];}
    #     """
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 17))

    def test_func_redeclared_17(self):
        input = """
        Function main(){Let a[5]: Number = [1, 2, 3, 4, 5];}
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 17))