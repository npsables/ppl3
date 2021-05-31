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

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast, c):

        # [self.visit(x, c) for x in ast.decl]
        return 0
