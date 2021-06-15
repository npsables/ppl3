from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
from Visitor import *
from StaticError import *
from functools import *


class Type(ABC):
    __metaclass__ = ABCMeta
    pass


class Prim(Type):
    __metaclass__ = ABCMeta
    pass


class NumberType(Prim):
    
    def __str__(self):
        return "NumberType"

class StringType(Prim):
    
    def __str__(self):
        return "StringType"

class BoolType(Prim):
    
    def __str__(self):
        return "BoolType"

class VoidType(Type):
    
    def __str__(self):
        return "VoidType"

class Unknown(Type):
    
    def __str__(self):
        return "Unknown"



@dataclass
class ArrayType(Type):
    dimen: List[int]
    eletype: Type

    # Print for debug
    def __str__(self):
        return "ArrayType([" + ", ".join(str(i) for i in self.dimen) + "], " + str(self.eletype) + ")"

@dataclass
class MType:
    intype: List[Type]
    restype: Type

    # Print for debug
    def __str__(self):
        return "MType([" + ", ".join(str(i) for i in self.intype) + "], " + str(self.restype) + ")"


@dataclass
class Symbol:
    name: str
    mtype: MType

    # Print for debug
    def __str__(self):
        return "Symbol(" + self.name + ", " + str(self.mtype) + ")"


class StaticChecker(BaseVisitor):

    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol("read",      MType([],               StringType())),
            Symbol("print",     MType([StringType()],   VoidType())),
            Symbol("printSLn",  MType([StringType()],   VoidType()))
        ]

    def lookup(self,name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast, c):
        lst = [[],[0],[],[False],[]]

        no_main_func = True

        #Store List for travel AST tree
        # lst[0]: Store symbol | symbol list
        # lst[1]: Store the index when go to block stmt of function, 0 mean global block | scope index list
        # lst[2]: Store type of function for checking with return type
        # lst[3]: Check if in-loop or not

        lst[0] = [] + c # add global_envi to symbol list for checking redeclare


        # Check redeclare (function, variable, constant)
        for decl in ast.decl:
            if type(decl) is VarDecl:
                lst[0] = lst[0] + [self.visit(decl,lst)]
            elif type(decl) is ConstDecl:
                lst[0] = lst[0] + [self.visit(decl,lst)]
            else:
                if self.lookup(decl.name.name, lst[0], lambda x: x.name) is not None:
                    raise Redeclared(Function(), decl.name.name)
                else:
                    if decl.name.name == "main":
                        no_main_func = False
                    lst[0]= lst[0] + [Symbol(decl.name.name, MType([y.typ for y in decl.param], VoidType()))]

        # Check if not main function
        if no_main_func:
            raise NoEntryPoint()

        # Visit function block
        for decl in ast.decl:
            if type(decl) is FuncDecl:
                lst[1] = lst[1] + [len(lst[0])]
                lst[2] = lst[2] + [Symbol(decl.name.name, MType([y.typ for y in decl.param], VoidType()))]
                self.visit(decl, lst)
        return 0

    def visitVarDecl(self, ast, c):
        start = c[1][-1] # Get index of current scope to travel in symbol list
        end = len(c[0])
        if self.lookup(ast.variable.name, c[0][start:end], lambda x: x.name) is not None:
            raise Redeclared(Variable(), ast.variable.name)

        return Symbol(ast.variable.name, MType([], ast.typ))

    def visitConstDecl(self, ast, c):
        start = c[1][-1] # Get index of current scope to travel in symbol list
        end = len(c[0])

        if self.lookup(ast.constant.name, c[0][start:end], lambda x: x.name) is not None:
            raise Redeclared(Constant(), ast.constant.name)

        return Symbol(ast.constant.name, MType([], ast.typ))

    def visitFuncDecl(self, ast, c):
        param_list = []

        # Check parameter redeclared
        if ast.param != []:
            lst = [Symbol(ast.param[0].variable.name, ast.param[0].typ)]

            for x in ast.param[1:len(ast.param)]:
                if self.lookup(x.variable.name, lst, lambda x: x.name) is not None:
                    raise Redeclared(Parameter(), x.variable.name)
                else:
                    lst = lst + [Symbol(x.variable.name, x.typ)]
            
            c[0] = c[0] + lst
        
        # Visit function body
        inLoop = c[3][0]
        for inst in ast.body:
            # self.isContinueandBreakInLoop(ast.member,inLoop)
            # isContinueandBreakInLoop is False if it do not raise exception
            if type(inst) is VarDecl:
                c[0] = c[0] + [self.visit(inst, c)]
            elif type(inst) is Assign:
                self.visit(inst, c)
                print(c[0][4])
            elif type(inst) is Return:
                self.visit(inst, c)
            elif type(inst) is If:
                self.visit(inst, c)
            elif type(inst) is Dowhile:
                self.visit(inst, c)
                c[3][0] = False
            elif type(inst) is For:
                self.visit(inst, c)
                c[3][0] = False
            else:
                self.visit(inst,c)
            
        for y in range(c[1][-1], len(c[0])):
            c[0].pop()
        c[1].pop()

    # def isContinueandBreakInLoop(self,lst,inLoop):
    #     if inLoop == False: 
    #         if self.lookup(Break, lst, lambda x: type(x)) is not None:
    #             raise BreakNotInLoop()
    #         if self.lookup(Continue, lst, lambda x: type(x)) is not None:
    #             raise ContinueNotInLoop()
    #     return False

    def visitBinaryOp(self, ast, c):
        return None

    def visitUnaryOp(self, ast, c):
        return None

    def visitCallExpr(self, ast, c):
        return None

    def visitId(self, ast, c):
        return None


    def visitArrayAccess(self, ast, c):
        for x in ast.idx:
            typ = self.visit(x, c)
            if typ != NumberType():
                raise TypeMismatchInExpression(ast)
        print("asdasd")
        return ast.arr.name


    def visitJSONAccess(self, ast, c):
        for x in ast.idx:
            typ = self.visit(x, c)
            if typ != StringType():
                raise TypeMismatchInExpression(ast)
    
        return ast.json.name


    def visitAssign(self, ast, c):
        if type(ast.lhs) is Id:
            symbol = self.lookup(ast.lhs.name, c[0], lambda x: x.name) 
            if symbol is None:
                raise Undeclared(Variable(), ast.lhs.name)

        if type(ast.lhs) is ArrayAccess:
            id_arr = self.visit(ast.lhs, c)
            symbol = self.lookup(id_arr, c[0], lambda x: x.name) 
            if symbol is None:
                raise Undeclared(Variable(), ast.lhs.name)

        if type(ast.lhs) is JSONAccess:
            id_arr = self.visit(ast.json, c)
            symbol = self.lookup(id_arr, c[0], lambda x: x.name) 
            if symbol is None:
                raise Undeclared(Variable(), ast.lhs.name)

        rhs_type = self.visit(ast.rhs, c)
        if symbol.mtype.restype == VoidType():
            raise TypeMismatchInStatement(ast)
        elif symbol.mtype.restype!= rhs_type:
            raise TypeMismatchInStatement(ast)

        return None

    def visitIf(self, ast, c):
        return None

    def visitFor(self, ast, c):
        return None

    def visitContinue(self, ast, c):
        return None

    def visitBreak(self, ast, c):
        return None

    def visitReturn(self, ast, c):
        return None

    def visitDowhile(self, ast, c):
        return None

    def visitWhile(self, ast, c):
        return None

    def visitCallStmt(self, ast, c):
        return None

    def visitNumberLiteral(self, ast, c):
        return NumberType()

    def visitBooleanLiteral(self, ast, c):
        return None

    def visitStringLiteral(self, ast, c):
        return None

    def visitArrayLiteral(self, ast, c):
        return None

    def visitJSONLiteral(self, ast, c):
        return None