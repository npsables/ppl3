# Generated from main/csel/parser/CSEL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2>")
        buf.write("\u0202\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\6\2\u0083\n\2")
        buf.write("\r\2\16\2\u0084\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u008d\n\3")
        buf.write("\f\3\16\3\u0090\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\7\4\u0099")
        buf.write("\n\4\f\4\16\4\u009c\13\4\3\5\3\5\3\5\7\5\u00a1\n\5\f\5")
        buf.write("\16\5\u00a4\13\5\3\6\5\6\u00a7\n\6\3\6\7\6\u00aa\n\6\f")
        buf.write("\6\16\6\u00ad\13\6\3\6\3\6\7\6\u00b1\n\6\f\6\16\6\u00b4")
        buf.write("\13\6\5\6\u00b6\n\6\3\6\3\6\5\6\u00ba\n\6\3\6\6\6\u00bd")
        buf.write("\n\6\r\6\16\6\u00be\5\6\u00c1\n\6\3\6\5\6\u00c4\n\6\3")
        buf.write("\6\6\6\u00c7\n\6\r\6\16\6\u00c8\3\6\3\6\5\6\u00cd\n\6")
        buf.write("\3\6\6\6\u00d0\n\6\r\6\16\6\u00d1\3\6\3\6\5\6\u00d6\n")
        buf.write("\6\3\6\6\6\u00d9\n\6\r\6\16\6\u00da\3\6\5\6\u00de\n\6")
        buf.write("\3\6\6\6\u00e1\n\6\r\6\16\6\u00e2\5\6\u00e5\n\6\3\7\3")
        buf.write("\7\5\7\u00e9\n\7\3\b\3\b\3\t\3\t\3\t\5\t\u00f0\n\t\3\n")
        buf.write("\3\n\3\n\3\13\3\13\7\13\u00f7\n\13\f\13\16\13\u00fa\13")
        buf.write("\13\3\13\3\13\7\13\u00fe\n\13\f\13\16\13\u0101\13\13\3")
        buf.write("\13\3\13\7\13\u0105\n\13\f\13\16\13\u0108\13\13\3\13\3")
        buf.write("\13\7\13\u010c\n\13\f\13\16\13\u010f\13\13\3\13\3\13\7")
        buf.write("\13\u0113\n\13\f\13\16\13\u0116\13\13\3\13\3\13\7\13\u011a")
        buf.write("\n\13\f\13\16\13\u011d\13\13\5\13\u011f\n\13\3\f\3\f\3")
        buf.write("\f\7\f\u0124\n\f\f\f\16\f\u0127\13\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3")
        buf.write("\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3*\3*\3*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3")
        buf.write("-\3-\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\39\39\3")
        buf.write("9\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3=\3=\3=\7=\u01e8\n=\f")
        buf.write("=\16=\u01eb\13=\3>\3>\3>\7>\u01f0\n>\f>\16>\u01f3\13>")
        buf.write("\3>\3>\3>\3?\3?\3?\3?\7?\u01fc\n?\f?\16?\u01ff\13?\3@")
        buf.write("\3@\4\u008e\u01fd\2A\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\2\23\2\25\2\27\n\31\13\33\f\35\r\37\16!\17#\20%\21\'")
        buf.write("\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33;\34=\35")
        buf.write("?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62")
        buf.write("i\63k\64m\65o\66q\67s8u9w:y;{<}=\177>\3\2\t\5\2\13\f\17")
        buf.write("\17\"\"\3\2c|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\7\2\n\f\16")
        buf.write("\17$$))^^\n\2$$))^^ddhhppttvv\2\u0224\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\3\u0082\3\2\2\2\5\u0088")
        buf.write("\3\2\2\2\7\u0096\3\2\2\2\t\u009d\3\2\2\2\13\u00e4\3\2")
        buf.write("\2\2\r\u00e8\3\2\2\2\17\u00ea\3\2\2\2\21\u00ef\3\2\2\2")
        buf.write("\23\u00f1\3\2\2\2\25\u011e\3\2\2\2\27\u0120\3\2\2\2\31")
        buf.write("\u012b\3\2\2\2\33\u012d\3\2\2\2\35\u012f\3\2\2\2\37\u0131")
        buf.write("\3\2\2\2!\u0134\3\2\2\2#\u0137\3\2\2\2%\u0139\3\2\2\2")
        buf.write("\'\u013c\3\2\2\2)\u013e\3\2\2\2+\u0140\3\2\2\2-\u0142")
        buf.write("\3\2\2\2/\u0144\3\2\2\2\61\u0147\3\2\2\2\63\u014a\3\2")
        buf.write("\2\2\65\u014c\3\2\2\2\67\u014f\3\2\2\29\u0152\3\2\2\2")
        buf.write(";\u0156\3\2\2\2=\u0158\3\2\2\2?\u015a\3\2\2\2A\u015c\3")
        buf.write("\2\2\2C\u015e\3\2\2\2E\u0160\3\2\2\2G\u0162\3\2\2\2I\u0164")
        buf.write("\3\2\2\2K\u0166\3\2\2\2M\u0168\3\2\2\2O\u016a\3\2\2\2")
        buf.write("Q\u0170\3\2\2\2S\u0179\3\2\2\2U\u017c\3\2\2\2W\u0181\3")
        buf.write("\2\2\2Y\u0186\3\2\2\2[\u018c\3\2\2\2]\u0190\3\2\2\2_\u0193")
        buf.write("\3\2\2\2a\u0196\3\2\2\2c\u019a\3\2\2\2e\u019f\3\2\2\2")
        buf.write("g\u01a5\3\2\2\2i\u01aa\3\2\2\2k\u01b1\3\2\2\2m\u01b9\3")
        buf.write("\2\2\2o\u01c0\3\2\2\2q\u01c5\3\2\2\2s\u01ce\3\2\2\2u\u01d5")
        buf.write("\3\2\2\2w\u01de\3\2\2\2y\u01e4\3\2\2\2{\u01ec\3\2\2\2")
        buf.write("}\u01f7\3\2\2\2\177\u0200\3\2\2\2\u0081\u0083\t\2\2\2")
        buf.write("\u0082\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0082\3")
        buf.write("\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087")
        buf.write("\b\2\2\2\u0087\4\3\2\2\2\u0088\u0089\7%\2\2\u0089\u008a")
        buf.write("\7%\2\2\u008a\u008e\3\2\2\2\u008b\u008d\13\2\2\2\u008c")
        buf.write("\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008e\u008c\3\2\2\2\u008f\u0091\3\2\2\2\u0090\u008e\3")
        buf.write("\2\2\2\u0091\u0092\7%\2\2\u0092\u0093\7%\2\2\u0093\u0094")
        buf.write("\3\2\2\2\u0094\u0095\b\3\2\2\u0095\6\3\2\2\2\u0096\u009a")
        buf.write("\t\3\2\2\u0097\u0099\t\4\2\2\u0098\u0097\3\2\2\2\u0099")
        buf.write("\u009c\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2")
        buf.write("\u009b\b\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009e\5\17")
        buf.write("\b\2\u009e\u00a2\t\3\2\2\u009f\u00a1\t\4\2\2\u00a0\u009f")
        buf.write("\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2")
        buf.write("\u00a3\3\2\2\2\u00a3\n\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5")
        buf.write("\u00a7\7/\2\2\u00a6\u00a5\3\2\2\2\u00a6\u00a7\3\2\2\2")
        buf.write("\u00a7\u00ab\3\2\2\2\u00a8\u00aa\t\5\2\2\u00a9\u00a8\3")
        buf.write("\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac")
        buf.write("\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae")
        buf.write("\u00b5\7\60\2\2\u00af\u00b1\t\5\2\2\u00b0\u00af\3\2\2")
        buf.write("\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3")
        buf.write("\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5")
        buf.write("\u00b2\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00c0\3\2\2\2")
        buf.write("\u00b7\u00b9\t\6\2\2\u00b8\u00ba\7/\2\2\u00b9\u00b8\3")
        buf.write("\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bc\3\2\2\2\u00bb\u00bd")
        buf.write("\t\5\2\2\u00bc\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c1\3\2\2\2")
        buf.write("\u00c0\u00b7\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00e5\3")
        buf.write("\2\2\2\u00c2\u00c4\7/\2\2\u00c3\u00c2\3\2\2\2\u00c3\u00c4")
        buf.write("\3\2\2\2\u00c4\u00c6\3\2\2\2\u00c5\u00c7\t\5\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c6\3\2\2\2")
        buf.write("\u00c8\u00c9\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00e5\7")
        buf.write("\60\2\2\u00cb\u00cd\7/\2\2\u00cc\u00cb\3\2\2\2\u00cc\u00cd")
        buf.write("\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00d0\t\5\2\2\u00cf")
        buf.write("\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d1\u00d2\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d5\t")
        buf.write("\6\2\2\u00d4\u00d6\7/\2\2\u00d5\u00d4\3\2\2\2\u00d5\u00d6")
        buf.write("\3\2\2\2\u00d6\u00d8\3\2\2\2\u00d7\u00d9\t\5\2\2\u00d8")
        buf.write("\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00d8\3\2\2\2")
        buf.write("\u00da\u00db\3\2\2\2\u00db\u00e5\3\2\2\2\u00dc\u00de\7")
        buf.write("/\2\2\u00dd\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e0")
        buf.write("\3\2\2\2\u00df\u00e1\t\5\2\2\u00e0\u00df\3\2\2\2\u00e1")
        buf.write("\u00e2\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2")
        buf.write("\u00e3\u00e5\3\2\2\2\u00e4\u00a6\3\2\2\2\u00e4\u00c3\3")
        buf.write("\2\2\2\u00e4\u00cc\3\2\2\2\u00e4\u00dd\3\2\2\2\u00e5\f")
        buf.write("\3\2\2\2\u00e6\u00e9\5c\62\2\u00e7\u00e9\5e\63\2\u00e8")
        buf.write("\u00e6\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9\16\3\2\2\2\u00ea")
        buf.write("\u00eb\7&\2\2\u00eb\20\3\2\2\2\u00ec\u00f0\n\7\2\2\u00ed")
        buf.write("\u00ee\7)\2\2\u00ee\u00f0\7$\2\2\u00ef\u00ec\3\2\2\2\u00ef")
        buf.write("\u00ed\3\2\2\2\u00f0\22\3\2\2\2\u00f1\u00f2\7^\2\2\u00f2")
        buf.write("\u00f3\t\b\2\2\u00f3\24\3\2\2\2\u00f4\u0106\5\13\6\2\u00f5")
        buf.write("\u00f7\5\3\2\2\u00f6\u00f5\3\2\2\2\u00f7\u00fa\3\2\2\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fb\3")
        buf.write("\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00ff\5E#\2\u00fc\u00fe")
        buf.write("\5\3\2\2\u00fd\u00fc\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff")
        buf.write("\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0102\3\2\2\2")
        buf.write("\u0101\u00ff\3\2\2\2\u0102\u0103\5\13\6\2\u0103\u0105")
        buf.write("\3\2\2\2\u0104\u00f8\3\2\2\2\u0105\u0108\3\2\2\2\u0106")
        buf.write("\u0104\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u011f\3\2\2\2")
        buf.write("\u0108\u0106\3\2\2\2\u0109\u011b\5\27\f\2\u010a\u010c")
        buf.write("\5\3\2\2\u010b\u010a\3\2\2\2\u010c\u010f\3\2\2\2\u010d")
        buf.write("\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0110\3\2\2\2")
        buf.write("\u010f\u010d\3\2\2\2\u0110\u0114\5E#\2\u0111\u0113\5\3")
        buf.write("\2\2\u0112\u0111\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0112")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117\3\2\2\2\u0116")
        buf.write("\u0114\3\2\2\2\u0117\u0118\5\27\f\2\u0118\u011a\3\2\2")
        buf.write("\2\u0119\u010d\3\2\2\2\u011a\u011d\3\2\2\2\u011b\u0119")
        buf.write("\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011f\3\2\2\2\u011d")
        buf.write("\u011b\3\2\2\2\u011e\u00f4\3\2\2\2\u011e\u0109\3\2\2\2")
        buf.write("\u011f\26\3\2\2\2\u0120\u0125\7$\2\2\u0121\u0124\5\21")
        buf.write("\t\2\u0122\u0124\5\23\n\2\u0123\u0121\3\2\2\2\u0123\u0122")
        buf.write("\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126\u0128\3\2\2\2\u0127\u0125\3\2\2\2")
        buf.write("\u0128\u0129\7$\2\2\u0129\u012a\b\f\3\2\u012a\30\3\2\2")
        buf.write("\2\u012b\u012c\7-\2\2\u012c\32\3\2\2\2\u012d\u012e\7,")
        buf.write("\2\2\u012e\34\3\2\2\2\u012f\u0130\7#\2\2\u0130\36\3\2")
        buf.write("\2\2\u0131\u0132\7~\2\2\u0132\u0133\7~\2\2\u0133 \3\2")
        buf.write("\2\2\u0134\u0135\7#\2\2\u0135\u0136\7?\2\2\u0136\"\3\2")
        buf.write("\2\2\u0137\u0138\7>\2\2\u0138$\3\2\2\2\u0139\u013a\7>")
        buf.write("\2\2\u013a\u013b\7?\2\2\u013b&\3\2\2\2\u013c\u013d\7?")
        buf.write("\2\2\u013d(\3\2\2\2\u013e\u013f\7/\2\2\u013f*\3\2\2\2")
        buf.write("\u0140\u0141\7\61\2\2\u0141,\3\2\2\2\u0142\u0143\7\'\2")
        buf.write("\2\u0143.\3\2\2\2\u0144\u0145\7(\2\2\u0145\u0146\7(\2")
        buf.write("\2\u0146\60\3\2\2\2\u0147\u0148\7?\2\2\u0148\u0149\7?")
        buf.write("\2\2\u0149\62\3\2\2\2\u014a\u014b\7@\2\2\u014b\64\3\2")
        buf.write("\2\2\u014c\u014d\7@\2\2\u014d\u014e\7?\2\2\u014e\66\3")
        buf.write("\2\2\2\u014f\u0150\7-\2\2\u0150\u0151\7\60\2\2\u01518")
        buf.write("\3\2\2\2\u0152\u0153\7?\2\2\u0153\u0154\7?\2\2\u0154\u0155")
        buf.write("\7\60\2\2\u0155:\3\2\2\2\u0156\u0157\7*\2\2\u0157<\3\2")
        buf.write("\2\2\u0158\u0159\7+\2\2\u0159>\3\2\2\2\u015a\u015b\7}")
        buf.write("\2\2\u015b@\3\2\2\2\u015c\u015d\7\177\2\2\u015dB\3\2\2")
        buf.write("\2\u015e\u015f\7=\2\2\u015fD\3\2\2\2\u0160\u0161\7.\2")
        buf.write("\2\u0161F\3\2\2\2\u0162\u0163\7]\2\2\u0163H\3\2\2\2\u0164")
        buf.write("\u0165\7_\2\2\u0165J\3\2\2\2\u0166\u0167\7\60\2\2\u0167")
        buf.write("L\3\2\2\2\u0168\u0169\7<\2\2\u0169N\3\2\2\2\u016a\u016b")
        buf.write("\7D\2\2\u016b\u016c\7t\2\2\u016c\u016d\7g\2\2\u016d\u016e")
        buf.write("\7c\2\2\u016e\u016f\7m\2\2\u016fP\3\2\2\2\u0170\u0171")
        buf.write("\7E\2\2\u0171\u0172\7q\2\2\u0172\u0173\7p\2\2\u0173\u0174")
        buf.write("\7v\2\2\u0174\u0175\7k\2\2\u0175\u0176\7p\2\2\u0176\u0177")
        buf.write("\7w\2\2\u0177\u0178\7g\2\2\u0178R\3\2\2\2\u0179\u017a")
        buf.write("\7K\2\2\u017a\u017b\7h\2\2\u017bT\3\2\2\2\u017c\u017d")
        buf.write("\7G\2\2\u017d\u017e\7n\2\2\u017e\u017f\7u\2\2\u017f\u0180")
        buf.write("\7g\2\2\u0180V\3\2\2\2\u0181\u0182\7G\2\2\u0182\u0183")
        buf.write("\7n\2\2\u0183\u0184\7k\2\2\u0184\u0185\7h\2\2\u0185X\3")
        buf.write("\2\2\2\u0186\u0187\7Y\2\2\u0187\u0188\7j\2\2\u0188\u0189")
        buf.write("\7k\2\2\u0189\u018a\7n\2\2\u018a\u018b\7g\2\2\u018bZ\3")
        buf.write("\2\2\2\u018c\u018d\7H\2\2\u018d\u018e\7q\2\2\u018e\u018f")
        buf.write("\7t\2\2\u018f\\\3\2\2\2\u0190\u0191\7Q\2\2\u0191\u0192")
        buf.write("\7h\2\2\u0192^\3\2\2\2\u0193\u0194\7K\2\2\u0194\u0195")
        buf.write("\7p\2\2\u0195`\3\2\2\2\u0196\u0197\7N\2\2\u0197\u0198")
        buf.write("\7g\2\2\u0198\u0199\7v\2\2\u0199b\3\2\2\2\u019a\u019b")
        buf.write("\7V\2\2\u019b\u019c\7t\2\2\u019c\u019d\7w\2\2\u019d\u019e")
        buf.write("\7g\2\2\u019ed\3\2\2\2\u019f\u01a0\7H\2\2\u01a0\u01a1")
        buf.write("\7c\2\2\u01a1\u01a2\7n\2\2\u01a2\u01a3\7u\2\2\u01a3\u01a4")
        buf.write("\7g\2\2\u01a4f\3\2\2\2\u01a5\u01a6\7E\2\2\u01a6\u01a7")
        buf.write("\7c\2\2\u01a7\u01a8\7n\2\2\u01a8\u01a9\7n\2\2\u01a9h\3")
        buf.write("\2\2\2\u01aa\u01ab\7P\2\2\u01ab\u01ac\7w\2\2\u01ac\u01ad")
        buf.write("\7o\2\2\u01ad\u01ae\7d\2\2\u01ae\u01af\7g\2\2\u01af\u01b0")
        buf.write("\7t\2\2\u01b0j\3\2\2\2\u01b1\u01b2\7D\2\2\u01b2\u01b3")
        buf.write("\7q\2\2\u01b3\u01b4\7q\2\2\u01b4\u01b5\7n\2\2\u01b5\u01b6")
        buf.write("\7g\2\2\u01b6\u01b7\7c\2\2\u01b7\u01b8\7p\2\2\u01b8l\3")
        buf.write("\2\2\2\u01b9\u01ba\7U\2\2\u01ba\u01bb\7v\2\2\u01bb\u01bc")
        buf.write("\7t\2\2\u01bc\u01bd\7k\2\2\u01bd\u01be\7p\2\2\u01be\u01bf")
        buf.write("\7i\2\2\u01bfn\3\2\2\2\u01c0\u01c1\7L\2\2\u01c1\u01c2")
        buf.write("\7U\2\2\u01c2\u01c3\7Q\2\2\u01c3\u01c4\7P\2\2\u01c4p\3")
        buf.write("\2\2\2\u01c5\u01c6\7E\2\2\u01c6\u01c7\7q\2\2\u01c7\u01c8")
        buf.write("\7p\2\2\u01c8\u01c9\7u\2\2\u01c9\u01ca\7v\2\2\u01ca\u01cb")
        buf.write("\7c\2\2\u01cb\u01cc\7p\2\2\u01cc\u01cd\7v\2\2\u01cdr\3")
        buf.write("\2\2\2\u01ce\u01cf\7T\2\2\u01cf\u01d0\7g\2\2\u01d0\u01d1")
        buf.write("\7v\2\2\u01d1\u01d2\7w\2\2\u01d2\u01d3\7t\2\2\u01d3\u01d4")
        buf.write("\7p\2\2\u01d4t\3\2\2\2\u01d5\u01d6\7H\2\2\u01d6\u01d7")
        buf.write("\7w\2\2\u01d7\u01d8\7p\2\2\u01d8\u01d9\7e\2\2\u01d9\u01da")
        buf.write("\7v\2\2\u01da\u01db\7k\2\2\u01db\u01dc\7q\2\2\u01dc\u01dd")
        buf.write("\7p\2\2\u01ddv\3\2\2\2\u01de\u01df\7C\2\2\u01df\u01e0")
        buf.write("\7t\2\2\u01e0\u01e1\7t\2\2\u01e1\u01e2\7c\2\2\u01e2\u01e3")
        buf.write("\7{\2\2\u01e3x\3\2\2\2\u01e4\u01e9\7$\2\2\u01e5\u01e8")
        buf.write("\5\21\t\2\u01e6\u01e8\5\23\n\2\u01e7\u01e5\3\2\2\2\u01e7")
        buf.write("\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7\3\2\2\2")
        buf.write("\u01e9\u01ea\3\2\2\2\u01eaz\3\2\2\2\u01eb\u01e9\3\2\2")
        buf.write("\2\u01ec\u01f1\7$\2\2\u01ed\u01f0\5\21\t\2\u01ee\u01f0")
        buf.write("\5\23\n\2\u01ef\u01ed\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0")
        buf.write("\u01f3\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2")
        buf.write("\u01f2\u01f4\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4\u01f5\7")
        buf.write("^\2\2\u01f5\u01f6\n\b\2\2\u01f6|\3\2\2\2\u01f7\u01f8\7")
        buf.write("%\2\2\u01f8\u01f9\7%\2\2\u01f9\u01fd\3\2\2\2\u01fa\u01fc")
        buf.write("\13\2\2\2\u01fb\u01fa\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd")
        buf.write("\u01fe\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe~\3\2\2\2\u01ff")
        buf.write("\u01fd\3\2\2\2\u0200\u0201\13\2\2\2\u0201\u0080\3\2\2")
        buf.write("\2\'\2\u0084\u008e\u009a\u00a2\u00a6\u00ab\u00b2\u00b5")
        buf.write("\u00b9\u00be\u00c0\u00c3\u00c8\u00cc\u00d1\u00d5\u00da")
        buf.write("\u00dd\u00e2\u00e4\u00e8\u00ef\u00f8\u00ff\u0106\u010d")
        buf.write("\u0114\u011b\u011e\u0123\u0125\u01e7\u01e9\u01ef\u01f1")
        buf.write("\u01fd\4\b\2\2\3\f\2")
        return buf.getvalue()


class CSELLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    COMMENT_LINES = 2
    NORM_ID = 3
    CONST_ID = 4
    NUMBER_LIT = 5
    BOOLEAN_LIT = 6
    DOLLAR = 7
    STRINGLIT = 8
    ADD = 9
    MUL = 10
    NOT = 11
    OR = 12
    NEQ = 13
    LT = 14
    LTEQ = 15
    ASSIGN = 16
    SUB = 17
    DIV = 18
    MOD = 19
    AND = 20
    EQ = 21
    GT = 22
    GTEQ = 23
    STR_ADD = 24
    STR_COMPARE = 25
    LB = 26
    RB = 27
    LP = 28
    RP = 29
    SM = 30
    CM = 31
    LS = 32
    RS = 33
    DOT = 34
    COLON = 35
    BREAK = 36
    CONTINUE = 37
    IF = 38
    ELSE = 39
    ELIF = 40
    WHILE = 41
    FOR = 42
    OF = 43
    IN = 44
    LET = 45
    TRUE = 46
    FALSE = 47
    CALL = 48
    NUMBER = 49
    BOOLEAN = 50
    STRING = 51
    JSON = 52
    CONSTANT = 53
    RETURN = 54
    FUNCTION = 55
    ARRAY = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58
    UNTERMINATED_COMMENT = 59
    ERROR_CHAR = 60

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'$'", "'+'", "'*'", "'!'", "'||'", "'!='", "'<'", "'<='", "'='", 
            "'-'", "'/'", "'%'", "'&&'", "'=='", "'>'", "'>='", "'+.'", 
            "'==.'", "'('", "')'", "'{'", "'}'", "';'", "','", "'['", "']'", 
            "'.'", "':'", "'Break'", "'Continue'", "'If'", "'Else'", "'Elif'", 
            "'While'", "'For'", "'Of'", "'In'", "'Let'", "'True'", "'False'", 
            "'Call'", "'Number'", "'Boolean'", "'String'", "'JSON'", "'Constant'", 
            "'Return'", "'Function'", "'Array'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "COMMENT_LINES", "NORM_ID", "CONST_ID", "NUMBER_LIT", 
            "BOOLEAN_LIT", "DOLLAR", "STRINGLIT", "ADD", "MUL", "NOT", "OR", 
            "NEQ", "LT", "LTEQ", "ASSIGN", "SUB", "DIV", "MOD", "AND", "EQ", 
            "GT", "GTEQ", "STR_ADD", "STR_COMPARE", "LB", "RB", "LP", "RP", 
            "SM", "CM", "LS", "RS", "DOT", "COLON", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "WHILE", "FOR", "OF", "IN", "LET", "TRUE", 
            "FALSE", "CALL", "NUMBER", "BOOLEAN", "STRING", "JSON", "CONSTANT", 
            "RETURN", "FUNCTION", "ARRAY", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "WS", "COMMENT_LINES", "NORM_ID", "CONST_ID", "NUMBER_LIT", 
                  "BOOLEAN_LIT", "DOLLAR", "STRINGCHARS", "ESCAPECASE", 
                  "LISTKEY", "STRINGLIT", "ADD", "MUL", "NOT", "OR", "NEQ", 
                  "LT", "LTEQ", "ASSIGN", "SUB", "DIV", "MOD", "AND", "EQ", 
                  "GT", "GTEQ", "STR_ADD", "STR_COMPARE", "LB", "RB", "LP", 
                  "RP", "SM", "CM", "LS", "RS", "DOT", "COLON", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "WHILE", "FOR", "OF", 
                  "IN", "LET", "TRUE", "FALSE", "CALL", "NUMBER", "BOOLEAN", 
                  "STRING", "JSON", "CONSTANT", "RETURN", "FUNCTION", "ARRAY", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
                  "ERROR_CHAR" ]

    grammarFileName = "CSEL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:
            raise UncloseString(result.text[1:])
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text[1:])
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result.text;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[10] = self.STRINGLIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     


