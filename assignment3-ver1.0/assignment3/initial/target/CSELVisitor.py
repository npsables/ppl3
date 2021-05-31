# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSELParser import CSELParser
else:
    from CSELParser import CSELParser

# This class defines a complete generic visitor for a parse tree produced by CSELParser.

class CSELVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSELParser#program.
    def visitProgram(self, ctx:CSELParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#manydecls.
    def visitManydecls(self, ctx:CSELParser.ManydeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#constant_decl.
    def visitConstant_decl(self, ctx:CSELParser.Constant_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#funcdecl.
    def visitFuncdecl(self, ctx:CSELParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#vardecl_stmt.
    def visitVardecl_stmt(self, ctx:CSELParser.Vardecl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_temp.
    def visitVar_temp(self, ctx:CSELParser.Var_tempContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#var_constant.
    def visitVar_constant(self, ctx:CSELParser.Var_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#paralist.
    def visitParalist(self, ctx:CSELParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#paradecl.
    def visitParadecl(self, ctx:CSELParser.ParadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp_0.
    def visitExp_0(self, ctx:CSELParser.Exp_0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp_1.
    def visitExp_1(self, ctx:CSELParser.Exp_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp_2.
    def visitExp_2(self, ctx:CSELParser.Exp_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp_3.
    def visitExp_3(self, ctx:CSELParser.Exp_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp_4.
    def visitExp_4(self, ctx:CSELParser.Exp_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp_5.
    def visitExp_5(self, ctx:CSELParser.Exp_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp_6.
    def visitExp_6(self, ctx:CSELParser.Exp_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp_7.
    def visitExp_7(self, ctx:CSELParser.Exp_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#exp_8.
    def visitExp_8(self, ctx:CSELParser.Exp_8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#index_operators.
    def visitIndex_operators(self, ctx:CSELParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#key_operators.
    def visitKey_operators(self, ctx:CSELParser.Key_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#operands.
    def visitOperands(self, ctx:CSELParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#assign_stmt.
    def visitAssign_stmt(self, ctx:CSELParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#lhs.
    def visitLhs(self, ctx:CSELParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#if_stmt.
    def visitIf_stmt(self, ctx:CSELParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#while_stmt.
    def visitWhile_stmt(self, ctx:CSELParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#for_stmt.
    def visitFor_stmt(self, ctx:CSELParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#forin_stmt.
    def visitForin_stmt(self, ctx:CSELParser.Forin_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#forof_stmt.
    def visitForof_stmt(self, ctx:CSELParser.Forof_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#break_stmt.
    def visitBreak_stmt(self, ctx:CSELParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#continue_stmt.
    def visitContinue_stmt(self, ctx:CSELParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#return_stmt.
    def visitReturn_stmt(self, ctx:CSELParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#funcalls.
    def visitFuncalls(self, ctx:CSELParser.FuncallsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#block_stmt.
    def visitBlock_stmt(self, ctx:CSELParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#stmt.
    def visitStmt(self, ctx:CSELParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#indexdecl.
    def visitIndexdecl(self, ctx:CSELParser.IndexdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#json_lit.
    def visitJson_lit(self, ctx:CSELParser.Json_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#listkeyvalue.
    def visitListkeyvalue(self, ctx:CSELParser.ListkeyvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#array_lit.
    def visitArray_lit(self, ctx:CSELParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#normal_lit.
    def visitNormal_lit(self, ctx:CSELParser.Normal_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSELParser#primtypes.
    def visitPrimtypes(self, ctx:CSELParser.PrimtypesContext):
        return self.visitChildren(ctx)



del CSELParser