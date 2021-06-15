from CSELVisitor import CSELVisitor
from CSELParser import CSELParser
from functools import reduce
from AST import *
import json

class ASTGeneration(CSELVisitor):
    map_literal_lhs = lambda self,y: list(map(lambda x: \
        StringLiteral(x.replace('"','')) if isinstance(x, str) \
        else BooleanLiteral(x) if isinstance(x,bool) \
        else ArrayLiteral(self.map_literal_lhs(x)) if isinstance(x,list) \
        else NumberLiteral(float(x)), y))

    flatten =  lambda self,l: reduce(lambda x, y: x + self.flatten(y) if isinstance(y,list) else x + [y], l, [])

    def visitProgram(self, ctx: CSELParser.ProgramContext):
        declList = [self.visit(x) for x in ctx.manydecls()]

        # print("DeclList: ", declList,"\n")
        # print("Program2: ", Program(self.flatten(declList)),"\n")

        return Program(self.flatten(declList))


    def visitManydecls(self, ctx: CSELParser.ManydeclsContext):
        if ctx.vardecl_stmt():
            return self.visit(ctx.vardecl_stmt())
        if ctx.constant_decl():
            return self.visit(ctx.constant_decl())
        if ctx.funcdecl(): 
            return self.visit(ctx.funcdecl())


    def visitConstant_decl(self, ctx: CSELParser.Constant_declContext):
        constant_list = list(map(lambda x: self.visit(x), ctx.var_constant()))
        return constant_list    


    def visitVar_constant(self, ctx:CSELParser.Var_constantContext):
        primtype = self.visit(ctx.primtypes()) if ctx.primtypes() != None else NoneType()
        dimen = self.visit(ctx.index_operators()) if ctx.index_operators() else None
        init_val = self.visit(ctx.exp_0()) if ctx.ASSIGN() else None

        return ConstDecl(Id(ctx.CONST_ID().getText()), dimen, primtype, init_val)


    def visitVardecl_stmt(self, ctx: CSELParser.Vardecl_stmtContext):
        var_temp_list = [self.visit(x) for x in ctx.var_temp()]

        # print("var_temp_list: ", var_temp_list)

        return var_temp_list


    def visitVar_temp(self, ctx: CSELParser.Var_tempContext):
        primtype = self.visit(ctx.primtypes()) if ctx.primtypes() != None else NoneType()
        dimen = self.visit(ctx.index_operators()) if ctx.index_operators() else None
        init_val = self.visit(ctx.exp_0()) if ctx.ASSIGN() else None   

        return VarDecl(Id(ctx.NORM_ID().getText()), dimen, primtype, init_val)


    def visitFuncdecl(self, ctx: CSELParser.FuncdeclContext):
        list_of_para = []
        if ctx.paralist():
            list_of_para = self.visit(ctx.paralist())
        list_body = self.visit(ctx.block_stmt())

        # print("FuncDecl: ", FuncDecl(Id(ctx.NORM_ID().getText()), list_of_para, (list_body,[])))

        return FuncDecl(Id(ctx.NORM_ID().getText()), list_of_para, list_body)


    def visitBlock_stmt(self, ctx: CSELParser.Block_stmtContext):
        block_stmt = []

        if ctx.stmt():
            block_stmt = block_stmt + [self.visit(x) for x in ctx.stmt()]
            
        # print("block_stmt: ", block_stmt)

        return self.flatten(block_stmt)


    def visitStmt(self, ctx: CSELParser.StmtContext):
        if ctx.vardecl_stmt():
            return self.visit(ctx.vardecl_stmt())
        if ctx.constant_decl():
            return self.visit(ctx.constant_decl())        
        if ctx.assign_stmt():
            return self.visit(ctx.assign_stmt())
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        if ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        if ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        if ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        if ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        if ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        if ctx.funcalls():
            return self.visit(ctx.funcalls())


    def visitAssign_stmt(self, ctx: CSELParser.Assign_stmtContext):
        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.exp_0())
        return Assign(lhs, exp)


    def visitLhs(self, ctx: CSELParser.LhsContext):
        if ctx.NORM_ID():
            return Id(ctx.NORM_ID().getText())
        elif ctx.CONST_ID():
            return Id(ctx.CONST_ID().getText())
        elif ctx.exp_7():
            return self.visit(ctx.exp_7())



    def visitIf_stmt(self, ctx: CSELParser.If_stmtContext):
        exp_0_list = [self.visit(x) for x in ctx.exp_0()]
        block_stmt_list = [self.visit(x) for x in ctx.block_stmt()]

        else_block_stmt = []
        if ctx.ELSE():
            else_block_stmt = block_stmt_list[-1]
            block_stmt_list = block_stmt_list[:-1]
        tuple_list =  list(zip(exp_0_list, block_stmt_list))

        return If(tuple_list, else_block_stmt)


    def visitFor_stmt(self, ctx: CSELParser.For_stmtContext):
        if ctx.forin_stmt():
            return self.visit(ctx.forin_stmt())
        else:
            return self.visit(ctx.forof_stmt())


    def visitForin_stmt(self, ctx: CSELParser.Forin_stmtContext):
        idx = Id(ctx.NORM_ID().getText())
        exp = self.visit(ctx.exp_0())
        blk_stmt = self.visit(ctx.block_stmt())

        return ForIn(idx, exp, blk_stmt)


    def visitForof_stmt(self, ctx: CSELParser.Forof_stmtContext):
        idx = Id(ctx.NORM_ID().getText())
        exp = self.visit(ctx.exp_0())
        blk_stmt = self.visit(ctx.block_stmt())

        return ForOf(idx, exp, blk_stmt)


    def visitBreak_stmt(self, ctx:CSELParser.Break_stmtContext):
        return Break()


    def visitReturn_stmt(self, ctx:CSELParser.Return_stmtContext):
    
        return Return(self.visit(ctx.exp_0()) if ctx.exp_0() else None)


    def visitContinue_stmt(self, ctx: CSELParser.Continue_stmtContext):
        return Continue()


    def visitWhile_stmt(self, ctx:CSELParser.While_stmtContext):
        exp = self.visit(ctx.exp_0())
        stmt= self.visit(ctx.block_stmt())
        return While(exp, stmt)


    def visitFuncalls(self, ctx:CSELParser.FuncallsContext):
        list_exp = [self.visit(x) for x in ctx.exp_0()]
        return CallStmt(Id(ctx.NORM_ID().getText()), list_exp)


    def visitParalist(self, ctx: CSELParser.ParalistContext):
        list_para =  [self.visit(x) for x in ctx.paradecl()]
        return list_para


    def visitParadecl(self, ctx: CSELParser.ParadeclContext):
        if ctx.NORM_ID():
            return VarDecl(Id(ctx.NORM_ID().getText()), None, NoneType(), None)
        elif ctx.CONST_ID():
            return VarDecl(Id(ctx.CONST_ID().getText()), None, NoneType(), None)
        else:
            return self.visit(ctx.indexdecl())


    def visitIndexdecl(self, ctx: CSELParser.IndexdeclContext):
        dimen = self.visit(ctx.index_operators()) if ctx.index_operators() \
            else [] if ctx.LS() else None

        if ctx.NORM_ID():   
            return VarDecl(Id(ctx.NORM_ID().getText()), dimen, NoneType(), None)

        if ctx.CONST_ID():
            return VarDecl(Id(ctx.CONST_ID().getText()), dimen, NoneType(), None)


    def visitExp_0(self, ctx: CSELParser.Exp_0Context):
        if ctx.STR_ADD():
            exp_1_list = [self.visit(x) for x in ctx.exp_1()]
            return BinaryOp(ctx.STR_ADD().getText(), exp_1_list[0], exp_1_list[1])
        elif ctx.STR_COMPARE():
            exp_1_list = [self.visit(x) for x in ctx.exp_1()]
            return BinaryOp(ctx.STR_COMPARE().getText(), exp_1_list[0], exp_1_list[1])
        else:
            exp_1_list = [self.visit(x) for x in ctx.exp_1()]
            return exp_1_list[0]


    def visitExp_1(self, ctx: CSELParser.Exp_1Context):
        if ctx.EQ():
            exp_2_list = [self.visit(x) for x in ctx.exp_2()]
            return BinaryOp(ctx.EQ().getText(), exp_2_list[0], exp_2_list[1])
        elif ctx.NEQ():
            exp_2_list = [self.visit(x) for x in ctx.exp_2()]
            return BinaryOp(ctx.NEQ().getText(), exp_2_list[0], exp_2_list[1])
        elif ctx.LT():
            exp_2_list = [self.visit(x) for x in ctx.exp_2()]
            return BinaryOp(ctx.LT().getText(), exp_2_list[0], exp_2_list[1])
        elif ctx.GT():
            exp_2_list = [self.visit(x) for x in ctx.exp_2()]
            return BinaryOp(ctx.GT().getText(), exp_2_list[0], exp_2_list[1])
        elif ctx.LTEQ():
            exp_2_list = [self.visit(x) for x in ctx.exp_2()]
            return BinaryOp(ctx.LTEQ().getText(), exp_2_list[0], exp_2_list[1])
        elif ctx.GTEQ():
            exp_2_list = [self.visit(x) for x in ctx.exp_2()]
            return BinaryOp(ctx.GTEQ().getText(), exp_2_list[0], exp_2_list[1])
        else:
            exp_2_list = [self.visit(x) for x in ctx.exp_2()]
            return exp_2_list[0]


    def visitExp_2(self, ctx: CSELParser.Exp_2Context):
        if ctx.OR():
            exp2 = self.visit(ctx.exp_2())
            exp3 = self.visit(ctx.exp_3())
            return BinaryOp(ctx.OR().getText(), exp2, exp3)
        elif ctx.AND():
            exp2 = self.visit(ctx.exp_2())
            exp3 = self.visit(ctx.exp_3())
            return BinaryOp(ctx.AND().getText(), exp2, exp3)
        else:
            return self.visit(ctx.exp_3())


    def visitExp_3(self, ctx: CSELParser.Exp_3Context):
        if ctx.ADD():
            exp3 = self.visit(ctx.exp_3())
            exp4 = self.visit(ctx.exp_4())
            return BinaryOp(ctx.ADD().getText(), exp3, exp4)
        elif ctx.SUB():
            exp3 = self.visit(ctx.exp_3())
            exp4 = self.visit(ctx.exp_4())
            return BinaryOp(ctx.SUB().getText(), exp3, exp4)
        else:
            return self.visit(ctx.exp_4()) 


    def visitExp_4(self, ctx: CSELParser.Exp_4Context):
        if ctx.MUL():
            exp4 = self.visit(ctx.exp_4())
            exp5 = self.visit(ctx.exp_5())
            return BinaryOp(ctx.MUL().getText(), exp4, exp5)
        elif ctx.DIV():
            exp4 = self.visit(ctx.exp_4())
            exp5 = self.visit(ctx.exp_5())
            return BinaryOp(ctx.DIV().getText(), exp4, exp5)
        elif ctx.MOD():
            exp4 = self.visit(ctx.exp_4())
            exp5 = self.visit(ctx.exp_5())
            return BinaryOp(ctx.MOD().getText(), exp4, exp5)
        else:
            return self.visit(ctx.exp_5())


    def visitExp_5(self, ctx: CSELParser.Exp_5Context):
        if ctx.NOT():
            exp5 = self.visit(ctx.exp_5())
            return UnaryOp(ctx.NOT().getText(), exp5)
        else:
            return self.visit(ctx.exp_6())


    def visitExp_6(self, ctx: CSELParser.Exp_6Context):
        if ctx.SUB():
            exp6 = self.visit(ctx.exp_6())
            return UnaryOp(ctx.SUB().getText(), exp6)
        else:
            return self.visit(ctx.exp_7()) 


    def visitExp_7(self, ctx: CSELParser.Exp_7Context):
        if ctx.index_operators():
            exp = self.visit(ctx.exp_7())
            idxs = self.visit(ctx.index_operators())

            return ArrayAccess(exp, idxs)

        elif ctx.key_operators():
            exp = self.visit(ctx.exp_7())
            keys = [self.visit(x) for x in ctx.key_operators()]
            return JSONAccess(exp, keys)

        else:   
            exp8 = self.visit(ctx.exp_8())
            return exp8


    def visitExp_8(self, ctx: CSELParser.Exp_8Context):
        if ctx.exp_0():
            return self.visit(ctx.exp_0()) 
        else:
            return self.visit(ctx.operands())


    def visitIndex_operators(self, ctx: CSELParser.Index_operatorsContext):
        para_val_list = [self.visit(x) for x in ctx.exp_0()]

        return para_val_list


    def visitKey_operators(self, ctx: CSELParser.Key_operatorsContext):
        return self.visit(ctx.exp_0())


    def visitOperands(self, ctx: CSELParser.OperandsContext):
        if ctx.NORM_ID():
            return Id(str(ctx.NORM_ID().getText()))
        elif ctx.funcalls():
            funcall = self.visit(ctx.funcalls())
            return CallExpr(funcall.method, funcall.param)
        elif ctx.NUMBER_LIT():
            return NumberLiteral(float(ctx.NUMBER_LIT().getText()))
        elif ctx.BOOLEAN_LIT():
            if str(ctx.BOOLEAN_LIT()) == 'True':
                return BooleanLiteral(True)
            else:
                return BooleanLiteral(False)
        elif ctx.array_lit():
            return self.visit(ctx.array_lit())
        elif ctx.json_lit():
            return self.visit(ctx.json_lit())
        elif ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT()))


    def visitArray_lit(self, ctx: CSELParser.Array_litContext):
        list_normlit = [self.visit(x) for x in ctx.normal_lit()]

        return ArrayLiteral(list_normlit)


    def visitJson_lit(self, ctx: CSELParser.Json_litContext):
        listkeyvalue = self.visit(ctx.listkeyvalue())
        return  JSONLiteral(listkeyvalue)


    def visitListkeyvalue(self, ctx:CSELParser.ListkeyvalueContext):
        norm_ids= [x.getText() for x in ctx.NORM_ID()]
        list_normlit = [self.visit(x) for x in ctx.normal_lit()]
        return list(zip(norm_ids, list_normlit))


    def visitPrimtypes(self, ctx: CSELParser.PrimtypesContext):
        if ctx.STRING():
            return StringType()
        elif ctx.NUMBER():
           return NumberType()
        elif ctx.JSON():
            return JSONType()
        elif ctx.ARRAY():
            return ArrayType()
        elif ctx.BOOLEAN():
            return BooleanType()


    def visitNormal_lit(self, ctx:CSELParser.Normal_litContext):
        if ctx.NUMBER_LIT():
            return NumberLiteral(float(ctx.NUMBER_LIT().getText()))
        elif ctx.BOOLEAN_LIT():
            if str(ctx.BOOLEAN_LIT()) == 'True':
                return BooleanLiteral(True)
            else:
                return BooleanLiteral(False)
        elif ctx.array_lit():
            return self.visit(ctx.array_lit())
        elif ctx.json_lit():
            return self.visit(ctx.json_lit())
        elif ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT()))