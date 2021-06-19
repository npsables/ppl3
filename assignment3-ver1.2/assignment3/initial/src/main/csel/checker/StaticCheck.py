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

        #TODO: VOID_TYPE!!!!
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
        tmp = ast.typ
        if self.lookup(ast.variable.name, c[0][start:end], lambda x: x.name) is not None:
            raise Redeclared(Variable(), ast.variable.name)

        typ_init = self.visit(ast.varInit, c) if ast.varInit is not None else None
        if typ_init is None:
            return Symbol(ast.variable.name, MType([], ast.typ))
        else: 
            if type(ast.typ) is NoneType:
                tmp = typ_init
            elif type(ast.typ) is not type(typ_init):
                raise TypeMismatchInStatement(ast)

        return Symbol(ast.variable.name, MType([], tmp))

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
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        
        if ast.op in ["+", "-", "*", "/", "%", "==", "!=", ">", ">=", "<", "<="]:
            if type(left) is not NumberType or type(right) is not NumberType:
                raise TypeMismatchInExpression(ast)
            elif ast.op in ["+", "-", "*", "/", "%"]:
                return NumberType()
            elif ast.op in [ "==", "!=", ">", ">=", "<", "<="]:
                return BooleanType()
        
        elif ast.op in ["&&", "||"]:
            if type(left) is not BooleanType or type(right) is not BooleanType:
                raise TypeMismatchInExpression(ast)        
            return BooleanType()
        
        elif ast.op in ["+.", "==."]:
            if type(left) is not StringType or type(right) is not StringType:
                raise TypeMismatchInExpression(ast) 
            return StringType()


    def visitUnaryOp(self, ast, c):
        body = self.visit(ast.body, c)
        if ast.op == '-':
            if type(body) is not NumberType:
                raise TypeMismatchInExpression(ast)
            else:
                return NumberType()
        
        elif ast.op == '!':
            if type(body) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            else:
                return BooleanType()
    

    def visitCallExpr(self, ast, c):
        return None

    def visitId(self, ast, c):
        symbol = self.lookup(ast.name, c[0], lambda x: x.name) 
        if symbol is None:
            raise Undeclared(Identifier(), ast.name)
        return symbol.mtype.restype
        

    def visitArrayAccess(self, ast, c):
        arr = self.visit(ast.arr, c)
        for x in ast.idx:
            typ = self.visit(x, c)
            if type(typ) is not NumberType:
                raise TypeMismatchInExpression(ast)
                
        return arr


    def visitJSONAccess(self, ast, c):
        for x in ast.idx:
            typ = self.visit(x, c)
            if type(typ) is not StringType:
                raise TypeMismatchInExpression(ast)
        return ast.json.name


    def visitAssign(self, ast, c):
        mtype = self.visit(ast.lhs,c) 
        
        if type(mtype) is NoneType:
            raise TypeCannotBeInferred(ast)

        rhs_type = self.visit(ast.rhs, c)
        # print(type(symbol.mtype.restype), type(rhs_type))
        if type(mtype) is VoidType:
            raise TypeMismatchInStatement(ast)
        
        elif type(mtype) is not type(rhs_type):
            raise TypeMismatchInStatement(ast)

        return None

    def visitIf(self, ast, c):
        """
            [  (exp, [ {}, {} ])   ]
        """
        for x in ast.ifthenStmt:
            exp_typ = self.visit(x[0],c)
            if type(exp_typ) is not BooleanType():
                raise TypeMismatchInStatement(ast)
            for inst in x[1]:
                self.visit(inst, c)
        
        for x in elseStmt:
            self.visit(x, c)

        return None

    def visitForIn(self, ast, c):
        # id_typ = self.visit(ast.idx1)
        return None

    def visitContinue(self, ast, c):
        return Continue()

    def visitBreak(self, ast, c):
        return Break()

    def visitReturn(self, ast, c):

        return None

    def visitDowhile(self, ast, c):
        return None

    def visitWhile(self, ast, c):
        exp_type =  self.visit(ast.exp, c)
        if type(exp_type) is not BooleanType():
            raise TypeMismatchInStatement(ast)
        
        return None

    def visitCallStmt(self, ast, c):
        return None

    def visitNumberLiteral(self, ast, c):
        return NumberType()

    def visitBooleanLiteral(self, ast, c):
        return BooleanType()

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitArrayLiteral(self, ast, c):
        # first = self.visit(ast.value[0], c)
        # for x in ast.value[1:]:
        #     typ = self.visit(x, c)
        #     if typ != first:
        #         raise InvalidArrayLiteral(x)
        # return typ
        return None

    def visitJSONLiteral(self, ast, c):

        return None