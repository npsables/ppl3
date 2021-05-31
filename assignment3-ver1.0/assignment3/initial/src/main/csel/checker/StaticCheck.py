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
        return "ArrayType([" + ",".join(str(i) for i in self.dimen) + "]," + str(self.eletype) + ")"

@dataclass
class MType:
    intype: List[Type]
    restype: Type

    # Print for debug
    def __str__(self):
        return "MType([" + ",".join(str(i) for i in self.intype) + "]," + str(self.restype) + ")"


@dataclass
class Symbol:
    name: str
    mtype: MType

    # Print for debug
    def __str__(self):
        return "Symbol(" + self.name + "," + str(self.mtype) + ")"


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
        lst = [[],[0],[VoidType()],[False],[]]

        #Store List for travel AST tree
        # lst[0]: Store symbol | symbol list
        # lst[1]: Store the index when go to block stmt of function, 0 mean global block | scope index list
        # lst[2]: Store type of function for checking with return type
        # lst[3]: Check if in-loop or not
        # lst[4]: Check if function main exit

        lst[0] = [] + c # add global_envi to symbol list for checking redeclare

        for decl in ast.decl:
            if type(decl) is VarDecl:
                lst[0] = lst[0] + [self.visit(decl,lst)]
            else:
                if self.lookup(decl.name.name, lst[0], lambda x: x.name) is not None:
                    raise Redeclared(Function(),decl.name.name)
                else:
                    if x.name.name != "main":
                        lst[4] = lst[4] + [decl.name.name] 
                    lst[0]= lst[0] + [Symbol(decl.name.name,MType([y.varType for y in decl.param], VoidType()))]

        # [self.visit(x, c) for x in ast.decl]
        return 0

    def visitVarDecl(self, ast, c):
        start = c[1][len(c[1]) - 1] # Get index of current scope to travel in symbol list
        end = len(c[0])
        if self.lookup(ast.variable.name, c[0][start:end], lambda x: x.name) is not None:
            
            raise Redeclared(Variable(), ast.variable.name)
        return Symbol(ast.variable.name, ast.typ)