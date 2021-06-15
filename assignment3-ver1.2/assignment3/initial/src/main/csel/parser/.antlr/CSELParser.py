# Generated from /home/arturob/Documents/uni/ppl/assignment3/ppl3/assignment3-ver1.2/assignment3/initial/src/main/csel/parser/CSEL.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3>")
        buf.write("\u0200\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\3\2\6\2T\n\2\r\2\16\2U\3\2\3\2\3")
        buf.write("\3\3\3\3\3\5\3]\n\3\3\4\3\4\3\4\3\4\7\4c\n\4\f\4\16\4")
        buf.write("f\13\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5n\n\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\7\6w\n\6\f\6\16\6z\13\6\3\6\3\6\3\7\3\7")
        buf.write("\5\7\u0080\n\7\3\7\3\7\5\7\u0084\n\7\3\7\3\7\5\7\u0088")
        buf.write("\n\7\3\b\3\b\5\b\u008c\n\b\3\b\3\b\5\b\u0090\n\b\3\b\3")
        buf.write("\b\5\b\u0094\n\b\3\t\3\t\3\t\7\t\u0099\n\t\f\t\16\t\u009c")
        buf.write("\13\t\3\n\3\n\3\n\5\n\u00a1\n\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\5\13\u00ac\n\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00c7\n\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00d2\n\r\f\r\16\r\u00d5")
        buf.write("\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\7\16")
        buf.write("\u00e0\n\16\f\16\16\16\u00e3\13\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u00f1\n")
        buf.write("\17\f\17\16\17\u00f4\13\17\3\20\3\20\3\20\5\20\u00f9\n")
        buf.write("\20\3\21\3\21\3\21\5\21\u00fe\n\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\6\22\u0107\n\22\r\22\16\22\u0108\7\22")
        buf.write("\u010b\n\22\f\22\16\22\u010e\13\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u0115\n\23\3\24\3\24\3\24\3\24\7\24\u011b\n")
        buf.write("\24\f\24\16\24\u011e\13\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u012e")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\5\30\u0138")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\7\31\u0145\n\31\f\31\16\31\u0148\13\31\3\31\3\31")
        buf.write("\5\31\u014c\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3")
        buf.write("\33\5\33\u0156\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \5 \u016c\n \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\7!\u0178")
        buf.write("\n!\f!\16!\u017b\13!\5!\u017d\n!\3!\3!\3!\3!\3\"\3\"\7")
        buf.write("\"\u0185\n\"\f\"\16\"\u0188\13\"\3\"\3\"\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\5#\u0198\n#\3$\3$\3$\3$\5$\u019e")
        buf.write("\n$\3%\3%\7%\u01a2\n%\f%\16%\u01a5\13%\3%\3%\7%\u01a9")
        buf.write("\n%\f%\16%\u01ac\13%\3%\3%\3&\3&\7&\u01b2\n&\f&\16&\u01b5")
        buf.write("\13&\3&\3&\7&\u01b9\n&\f&\16&\u01bc\13&\3&\3&\7&\u01c0")
        buf.write("\n&\f&\16&\u01c3\13&\3&\3&\7&\u01c7\n&\f&\16&\u01ca\13")
        buf.write("&\3&\3&\7&\u01ce\n&\f&\16&\u01d1\13&\3&\3&\7&\u01d5\n")
        buf.write("&\f&\16&\u01d8\13&\3&\7&\u01db\n&\f&\16&\u01de\13&\3\'")
        buf.write("\3\'\3\'\7\'\u01e3\n\'\f\'\16\'\u01e6\13\'\3\'\3\'\7\'")
        buf.write("\u01ea\n\'\f\'\16\'\u01ed\13\'\3\'\7\'\u01f0\n\'\f\'\16")
        buf.write("\'\u01f3\13\'\3\'\3\'\3(\3(\3(\3(\3(\5(\u01fc\n(\3)\3")
        buf.write(")\3)\2\6\30\32\34\"*\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNP\2\4\3\2\5\6\4")
        buf.write("\2\63\66::\2\u0226\2S\3\2\2\2\4\\\3\2\2\2\6^\3\2\2\2\b")
        buf.write("i\3\2\2\2\nr\3\2\2\2\f}\3\2\2\2\16\u0089\3\2\2\2\20\u0095")
        buf.write("\3\2\2\2\22\u00a0\3\2\2\2\24\u00ab\3\2\2\2\26\u00c6\3")
        buf.write("\2\2\2\30\u00c8\3\2\2\2\32\u00d6\3\2\2\2\34\u00e4\3\2")
        buf.write("\2\2\36\u00f8\3\2\2\2 \u00fd\3\2\2\2\"\u00ff\3\2\2\2$")
        buf.write("\u0114\3\2\2\2&\u0116\3\2\2\2(\u0121\3\2\2\2*\u012d\3")
        buf.write("\2\2\2,\u012f\3\2\2\2.\u0137\3\2\2\2\60\u0139\3\2\2\2")
        buf.write("\62\u014d\3\2\2\2\64\u0155\3\2\2\2\66\u0157\3\2\2\28\u015d")
        buf.write("\3\2\2\2:\u0163\3\2\2\2<\u0166\3\2\2\2>\u0169\3\2\2\2")
        buf.write("@\u016f\3\2\2\2B\u0182\3\2\2\2D\u0197\3\2\2\2F\u0199\3")
        buf.write("\2\2\2H\u019f\3\2\2\2J\u01af\3\2\2\2L\u01df\3\2\2\2N\u01fb")
        buf.write("\3\2\2\2P\u01fd\3\2\2\2RT\5\4\3\2SR\3\2\2\2TU\3\2\2\2")
        buf.write("US\3\2\2\2UV\3\2\2\2VW\3\2\2\2WX\7\2\2\3X\3\3\2\2\2Y]")
        buf.write("\5\n\6\2Z]\5\b\5\2[]\5\6\4\2\\Y\3\2\2\2\\Z\3\2\2\2\\[")
        buf.write("\3\2\2\2]\5\3\2\2\2^_\7\67\2\2_d\5\16\b\2`a\7!\2\2ac\5")
        buf.write("\16\b\2b`\3\2\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2eg\3\2")
        buf.write("\2\2fd\3\2\2\2gh\7 \2\2h\7\3\2\2\2ij\79\2\2jk\7\5\2\2")
        buf.write("km\7\34\2\2ln\5\20\t\2ml\3\2\2\2mn\3\2\2\2no\3\2\2\2o")
        buf.write("p\7\35\2\2pq\5B\"\2q\t\3\2\2\2rs\7/\2\2sx\5\f\7\2tu\7")
        buf.write("!\2\2uw\5\f\7\2vt\3\2\2\2wz\3\2\2\2xv\3\2\2\2xy\3\2\2")
        buf.write("\2y{\3\2\2\2zx\3\2\2\2{|\7 \2\2|\13\3\2\2\2}\177\7\5\2")
        buf.write("\2~\u0080\5&\24\2\177~\3\2\2\2\177\u0080\3\2\2\2\u0080")
        buf.write("\u0083\3\2\2\2\u0081\u0082\7%\2\2\u0082\u0084\5P)\2\u0083")
        buf.write("\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0087\3\2\2\2")
        buf.write("\u0085\u0086\7\22\2\2\u0086\u0088\5\24\13\2\u0087\u0085")
        buf.write("\3\2\2\2\u0087\u0088\3\2\2\2\u0088\r\3\2\2\2\u0089\u008b")
        buf.write("\7\6\2\2\u008a\u008c\5&\24\2\u008b\u008a\3\2\2\2\u008b")
        buf.write("\u008c\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008e\7%\2\2")
        buf.write("\u008e\u0090\5P)\2\u008f\u008d\3\2\2\2\u008f\u0090\3\2")
        buf.write("\2\2\u0090\u0093\3\2\2\2\u0091\u0092\7\22\2\2\u0092\u0094")
        buf.write("\5\24\13\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\17\3\2\2\2\u0095\u009a\5\22\n\2\u0096\u0097\7!\2\2\u0097")
        buf.write("\u0099\5\22\n\2\u0098\u0096\3\2\2\2\u0099\u009c\3\2\2")
        buf.write("\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\21\3")
        buf.write("\2\2\2\u009c\u009a\3\2\2\2\u009d\u00a1\7\5\2\2\u009e\u00a1")
        buf.write("\7\6\2\2\u009f\u00a1\5F$\2\u00a0\u009d\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a0\u009f\3\2\2\2\u00a1\23\3\2\2\2\u00a2\u00a3")
        buf.write("\5\26\f\2\u00a3\u00a4\7\32\2\2\u00a4\u00a5\5\26\f\2\u00a5")
        buf.write("\u00ac\3\2\2\2\u00a6\u00a7\5\26\f\2\u00a7\u00a8\7\33\2")
        buf.write("\2\u00a8\u00a9\5\26\f\2\u00a9\u00ac\3\2\2\2\u00aa\u00ac")
        buf.write("\5\26\f\2\u00ab\u00a2\3\2\2\2\u00ab\u00a6\3\2\2\2\u00ab")
        buf.write("\u00aa\3\2\2\2\u00ac\25\3\2\2\2\u00ad\u00ae\5\30\r\2\u00ae")
        buf.write("\u00af\7\27\2\2\u00af\u00b0\5\30\r\2\u00b0\u00c7\3\2\2")
        buf.write("\2\u00b1\u00b2\5\30\r\2\u00b2\u00b3\7\17\2\2\u00b3\u00b4")
        buf.write("\5\30\r\2\u00b4\u00c7\3\2\2\2\u00b5\u00b6\5\30\r\2\u00b6")
        buf.write("\u00b7\7\20\2\2\u00b7\u00b8\5\30\r\2\u00b8\u00c7\3\2\2")
        buf.write("\2\u00b9\u00ba\5\30\r\2\u00ba\u00bb\7\30\2\2\u00bb\u00bc")
        buf.write("\5\30\r\2\u00bc\u00c7\3\2\2\2\u00bd\u00be\5\30\r\2\u00be")
        buf.write("\u00bf\7\21\2\2\u00bf\u00c0\5\30\r\2\u00c0\u00c7\3\2\2")
        buf.write("\2\u00c1\u00c2\5\30\r\2\u00c2\u00c3\7\31\2\2\u00c3\u00c4")
        buf.write("\5\30\r\2\u00c4\u00c7\3\2\2\2\u00c5\u00c7\5\30\r\2\u00c6")
        buf.write("\u00ad\3\2\2\2\u00c6\u00b1\3\2\2\2\u00c6\u00b5\3\2\2\2")
        buf.write("\u00c6\u00b9\3\2\2\2\u00c6\u00bd\3\2\2\2\u00c6\u00c1\3")
        buf.write("\2\2\2\u00c6\u00c5\3\2\2\2\u00c7\27\3\2\2\2\u00c8\u00c9")
        buf.write("\b\r\1\2\u00c9\u00ca\5\32\16\2\u00ca\u00d3\3\2\2\2\u00cb")
        buf.write("\u00cc\f\5\2\2\u00cc\u00cd\7\16\2\2\u00cd\u00d2\5\32\16")
        buf.write("\2\u00ce\u00cf\f\4\2\2\u00cf\u00d0\7\26\2\2\u00d0\u00d2")
        buf.write("\5\32\16\2\u00d1\u00cb\3\2\2\2\u00d1\u00ce\3\2\2\2\u00d2")
        buf.write("\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2")
        buf.write("\u00d4\31\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d7\b\16")
        buf.write("\1\2\u00d7\u00d8\5\34\17\2\u00d8\u00e1\3\2\2\2\u00d9\u00da")
        buf.write("\f\5\2\2\u00da\u00db\7\13\2\2\u00db\u00e0\5\34\17\2\u00dc")
        buf.write("\u00dd\f\4\2\2\u00dd\u00de\7\23\2\2\u00de\u00e0\5\34\17")
        buf.write("\2\u00df\u00d9\3\2\2\2\u00df\u00dc\3\2\2\2\u00e0\u00e3")
        buf.write("\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2")
        buf.write("\33\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e4\u00e5\b\17\1\2\u00e5")
        buf.write("\u00e6\5\36\20\2\u00e6\u00f2\3\2\2\2\u00e7\u00e8\f\6\2")
        buf.write("\2\u00e8\u00e9\7\f\2\2\u00e9\u00f1\5\36\20\2\u00ea\u00eb")
        buf.write("\f\5\2\2\u00eb\u00ec\7\24\2\2\u00ec\u00f1\5\36\20\2\u00ed")
        buf.write("\u00ee\f\4\2\2\u00ee\u00ef\7\25\2\2\u00ef\u00f1\5\36\20")
        buf.write("\2\u00f0\u00e7\3\2\2\2\u00f0\u00ea\3\2\2\2\u00f0\u00ed")
        buf.write("\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2")
        buf.write("\u00f3\3\2\2\2\u00f3\35\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5")
        buf.write("\u00f6\7\r\2\2\u00f6\u00f9\5\36\20\2\u00f7\u00f9\5 \21")
        buf.write("\2\u00f8\u00f5\3\2\2\2\u00f8\u00f7\3\2\2\2\u00f9\37\3")
        buf.write("\2\2\2\u00fa\u00fb\7\23\2\2\u00fb\u00fe\5 \21\2\u00fc")
        buf.write("\u00fe\5\"\22\2\u00fd\u00fa\3\2\2\2\u00fd\u00fc\3\2\2")
        buf.write("\2\u00fe!\3\2\2\2\u00ff\u0100\b\22\1\2\u0100\u0101\5$")
        buf.write("\23\2\u0101\u010c\3\2\2\2\u0102\u0103\f\5\2\2\u0103\u010b")
        buf.write("\5&\24\2\u0104\u0106\f\4\2\2\u0105\u0107\5(\25\2\u0106")
        buf.write("\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0106\3\2\2\2")
        buf.write("\u0108\u0109\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u0102\3")
        buf.write("\2\2\2\u010a\u0104\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a")
        buf.write("\3\2\2\2\u010c\u010d\3\2\2\2\u010d#\3\2\2\2\u010e\u010c")
        buf.write("\3\2\2\2\u010f\u0110\7\34\2\2\u0110\u0111\5\24\13\2\u0111")
        buf.write("\u0112\7\35\2\2\u0112\u0115\3\2\2\2\u0113\u0115\5*\26")
        buf.write("\2\u0114\u010f\3\2\2\2\u0114\u0113\3\2\2\2\u0115%\3\2")
        buf.write("\2\2\u0116\u0117\7\"\2\2\u0117\u011c\5\24\13\2\u0118\u0119")
        buf.write("\7!\2\2\u0119\u011b\5\24\13\2\u011a\u0118\3\2\2\2\u011b")
        buf.write("\u011e\3\2\2\2\u011c\u011a\3\2\2\2\u011c\u011d\3\2\2\2")
        buf.write("\u011d\u011f\3\2\2\2\u011e\u011c\3\2\2\2\u011f\u0120\7")
        buf.write("#\2\2\u0120\'\3\2\2\2\u0121\u0122\7\36\2\2\u0122\u0123")
        buf.write("\5\24\13\2\u0123\u0124\7\37\2\2\u0124)\3\2\2\2\u0125\u012e")
        buf.write("\7\7\2\2\u0126\u012e\5@!\2\u0127\u012e\7\5\2\2\u0128\u012e")
        buf.write("\7\6\2\2\u0129\u012e\7\b\2\2\u012a\u012e\7\n\2\2\u012b")
        buf.write("\u012e\5L\'\2\u012c\u012e\5H%\2\u012d\u0125\3\2\2\2\u012d")
        buf.write("\u0126\3\2\2\2\u012d\u0127\3\2\2\2\u012d\u0128\3\2\2\2")
        buf.write("\u012d\u0129\3\2\2\2\u012d\u012a\3\2\2\2\u012d\u012b\3")
        buf.write("\2\2\2\u012d\u012c\3\2\2\2\u012e+\3\2\2\2\u012f\u0130")
        buf.write("\5.\30\2\u0130\u0131\7\22\2\2\u0131\u0132\5\24\13\2\u0132")
        buf.write("\u0133\7 \2\2\u0133-\3\2\2\2\u0134\u0138\7\5\2\2\u0135")
        buf.write("\u0138\7\6\2\2\u0136\u0138\5\"\22\2\u0137\u0134\3\2\2")
        buf.write("\2\u0137\u0135\3\2\2\2\u0137\u0136\3\2\2\2\u0138/\3\2")
        buf.write("\2\2\u0139\u013a\7(\2\2\u013a\u013b\7\34\2\2\u013b\u013c")
        buf.write("\5\24\13\2\u013c\u013d\7\35\2\2\u013d\u0146\5B\"\2\u013e")
        buf.write("\u013f\7*\2\2\u013f\u0140\7\34\2\2\u0140\u0141\5\24\13")
        buf.write("\2\u0141\u0142\7\35\2\2\u0142\u0143\5B\"\2\u0143\u0145")
        buf.write("\3\2\2\2\u0144\u013e\3\2\2\2\u0145\u0148\3\2\2\2\u0146")
        buf.write("\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u014b\3\2\2\2")
        buf.write("\u0148\u0146\3\2\2\2\u0149\u014a\7)\2\2\u014a\u014c\5")
        buf.write("B\"\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\61")
        buf.write("\3\2\2\2\u014d\u014e\7+\2\2\u014e\u014f\7\34\2\2\u014f")
        buf.write("\u0150\5\24\13\2\u0150\u0151\7\35\2\2\u0151\u0152\5B\"")
        buf.write("\2\u0152\63\3\2\2\2\u0153\u0156\5\66\34\2\u0154\u0156")
        buf.write("\58\35\2\u0155\u0153\3\2\2\2\u0155\u0154\3\2\2\2\u0156")
        buf.write("\65\3\2\2\2\u0157\u0158\7,\2\2\u0158\u0159\7\5\2\2\u0159")
        buf.write("\u015a\7.\2\2\u015a\u015b\5\24\13\2\u015b\u015c\5B\"\2")
        buf.write("\u015c\67\3\2\2\2\u015d\u015e\7,\2\2\u015e\u015f\7\5\2")
        buf.write("\2\u015f\u0160\7-\2\2\u0160\u0161\5\24\13\2\u0161\u0162")
        buf.write("\5B\"\2\u01629\3\2\2\2\u0163\u0164\7&\2\2\u0164\u0165")
        buf.write("\7 \2\2\u0165;\3\2\2\2\u0166\u0167\7\'\2\2\u0167\u0168")
        buf.write("\7 \2\2\u0168=\3\2\2\2\u0169\u016b\78\2\2\u016a\u016c")
        buf.write("\5\24\13\2\u016b\u016a\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016d\3\2\2\2\u016d\u016e\7 \2\2\u016e?\3\2\2\2\u016f")
        buf.write("\u0170\7\62\2\2\u0170\u0171\7\34\2\2\u0171\u0172\7\5\2")
        buf.write("\2\u0172\u0173\7!\2\2\u0173\u017c\7\"\2\2\u0174\u0179")
        buf.write("\5\24\13\2\u0175\u0176\7!\2\2\u0176\u0178\5\24\13\2\u0177")
        buf.write("\u0175\3\2\2\2\u0178\u017b\3\2\2\2\u0179\u0177\3\2\2\2")
        buf.write("\u0179\u017a\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3")
        buf.write("\2\2\2\u017c\u0174\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017e\u017f\7#\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u0181\7\35\2\2\u0181A\3\2\2\2\u0182\u0186\7\36\2\2\u0183")
        buf.write("\u0185\5D#\2\u0184\u0183\3\2\2\2\u0185\u0188\3\2\2\2\u0186")
        buf.write("\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0189\3\2\2\2")
        buf.write("\u0188\u0186\3\2\2\2\u0189\u018a\7\37\2\2\u018aC\3\2\2")
        buf.write("\2\u018b\u0198\5\6\4\2\u018c\u0198\5\n\6\2\u018d\u0198")
        buf.write("\5,\27\2\u018e\u0198\5\60\31\2\u018f\u0198\5\64\33\2\u0190")
        buf.write("\u0198\5\62\32\2\u0191\u0198\5:\36\2\u0192\u0198\5<\37")
        buf.write("\2\u0193\u0198\5> \2\u0194\u0195\5@!\2\u0195\u0196\7 ")
        buf.write("\2\2\u0196\u0198\3\2\2\2\u0197\u018b\3\2\2\2\u0197\u018c")
        buf.write("\3\2\2\2\u0197\u018d\3\2\2\2\u0197\u018e\3\2\2\2\u0197")
        buf.write("\u018f\3\2\2\2\u0197\u0190\3\2\2\2\u0197\u0191\3\2\2\2")
        buf.write("\u0197\u0192\3\2\2\2\u0197\u0193\3\2\2\2\u0197\u0194\3")
        buf.write("\2\2\2\u0198E\3\2\2\2\u0199\u019d\t\2\2\2\u019a\u019e")
        buf.write("\5&\24\2\u019b\u019c\7\"\2\2\u019c\u019e\7#\2\2\u019d")
        buf.write("\u019a\3\2\2\2\u019d\u019b\3\2\2\2\u019eG\3\2\2\2\u019f")
        buf.write("\u01a3\7\36\2\2\u01a0\u01a2\7\3\2\2\u01a1\u01a0\3\2\2")
        buf.write("\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4")
        buf.write("\3\2\2\2\u01a4\u01a6\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6")
        buf.write("\u01aa\5J&\2\u01a7\u01a9\7\3\2\2\u01a8\u01a7\3\2\2\2\u01a9")
        buf.write("\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2")
        buf.write("\u01ab\u01ad\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae\7")
        buf.write("\37\2\2\u01aeI\3\2\2\2\u01af\u01b3\7\5\2\2\u01b0\u01b2")
        buf.write("\7\3\2\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2")
        buf.write("\u01b5\u01b3\3\2\2\2\u01b6\u01ba\7%\2\2\u01b7\u01b9\7")
        buf.write("\3\2\2\u01b8\u01b7\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb\u01bd\3\2\2\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bd\u01dc\5N(\2\u01be\u01c0\7\3\2\2\u01bf")
        buf.write("\u01be\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf\3\2\2\2")
        buf.write("\u01c1\u01c2\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3\u01c1\3")
        buf.write("\2\2\2\u01c4\u01c8\7!\2\2\u01c5\u01c7\7\3\2\2\u01c6\u01c5")
        buf.write("\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8")
        buf.write("\u01c9\3\2\2\2\u01c9\u01cb\3\2\2\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01cb\u01cf\7\5\2\2\u01cc\u01ce\7\3\2\2\u01cd\u01cc\3")
        buf.write("\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0")
        buf.write("\3\2\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d2")
        buf.write("\u01d6\7%\2\2\u01d3\u01d5\7\3\2\2\u01d4\u01d3\3\2\2\2")
        buf.write("\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3")
        buf.write("\2\2\2\u01d7\u01d9\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01db")
        buf.write("\5N(\2\u01da\u01c1\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01ddK\3\2\2\2\u01de\u01dc")
        buf.write("\3\2\2\2\u01df\u01e0\7\"\2\2\u01e0\u01f1\5N(\2\u01e1\u01e3")
        buf.write("\7\3\2\2\u01e2\u01e1\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4")
        buf.write("\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e7\3\2\2\2")
        buf.write("\u01e6\u01e4\3\2\2\2\u01e7\u01eb\7!\2\2\u01e8\u01ea\7")
        buf.write("\3\2\2\u01e9\u01e8\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb\u01e9")
        buf.write("\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ee\3\2\2\2\u01ed")
        buf.write("\u01eb\3\2\2\2\u01ee\u01f0\5N(\2\u01ef\u01e4\3\2\2\2\u01f0")
        buf.write("\u01f3\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2")
        buf.write("\u01f2\u01f4\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4\u01f5\7")
        buf.write("#\2\2\u01f5M\3\2\2\2\u01f6\u01fc\7\7\2\2\u01f7\u01fc\7")
        buf.write("\b\2\2\u01f8\u01fc\5L\'\2\u01f9\u01fc\5H%\2\u01fa\u01fc")
        buf.write("\7\n\2\2\u01fb\u01f6\3\2\2\2\u01fb\u01f7\3\2\2\2\u01fb")
        buf.write("\u01f8\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fa\3\2\2\2")
        buf.write("\u01fcO\3\2\2\2\u01fd\u01fe\t\3\2\2\u01feQ\3\2\2\2\66")
        buf.write("U\\dmx\177\u0083\u0087\u008b\u008f\u0093\u009a\u00a0\u00ab")
        buf.write("\u00c6\u00d1\u00d3\u00df\u00e1\u00f0\u00f2\u00f8\u00fd")
        buf.write("\u0108\u010a\u010c\u0114\u011c\u012d\u0137\u0146\u014b")
        buf.write("\u0155\u016b\u0179\u017c\u0186\u0197\u019d\u01a3\u01aa")
        buf.write("\u01b3\u01ba\u01c1\u01c8\u01cf\u01d6\u01dc\u01e4\u01eb")
        buf.write("\u01f1\u01fb")
        return buf.getvalue()


class CSELParser ( Parser ):

    grammarFileName = "CSEL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'$'", "<INVALID>", 
                     "'+'", "'*'", "'!'", "'||'", "'!='", "'<'", "'<='", 
                     "'='", "'-'", "'/'", "'%'", "'&&'", "'=='", "'>'", 
                     "'>='", "'+.'", "'==.'", "'('", "')'", "'{'", "'}'", 
                     "';'", "','", "'['", "']'", "'.'", "':'", "'Break'", 
                     "'Continue'", "'If'", "'Else'", "'Elif'", "'While'", 
                     "'For'", "'Of'", "'In'", "'Let'", "'True'", "'False'", 
                     "'Call'", "'Number'", "'Boolean'", "'String'", "'JSON'", 
                     "'Constant'", "'Return'", "'Function'", "'Array'" ]

    symbolicNames = [ "<INVALID>", "WS", "COMMENT_LINES", "NORM_ID", "CONST_ID", 
                      "NUMBER_LIT", "BOOLEAN_LIT", "DOLLAR", "STRINGLIT", 
                      "ADD", "MUL", "NOT", "OR", "NEQ", "LT", "LTEQ", "ASSIGN", 
                      "SUB", "DIV", "MOD", "AND", "EQ", "GT", "GTEQ", "STR_ADD", 
                      "STR_COMPARE", "LB", "RB", "LP", "RP", "SM", "CM", 
                      "LS", "RS", "DOT", "COLON", "BREAK", "CONTINUE", "IF", 
                      "ELSE", "ELIF", "WHILE", "FOR", "OF", "IN", "LET", 
                      "TRUE", "FALSE", "CALL", "NUMBER", "BOOLEAN", "STRING", 
                      "JSON", "CONSTANT", "RETURN", "FUNCTION", "ARRAY", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_manydecls = 1
    RULE_constant_decl = 2
    RULE_funcdecl = 3
    RULE_vardecl_stmt = 4
    RULE_var_temp = 5
    RULE_var_constant = 6
    RULE_paralist = 7
    RULE_paradecl = 8
    RULE_exp_0 = 9
    RULE_exp_1 = 10
    RULE_exp_2 = 11
    RULE_exp_3 = 12
    RULE_exp_4 = 13
    RULE_exp_5 = 14
    RULE_exp_6 = 15
    RULE_exp_7 = 16
    RULE_exp_8 = 17
    RULE_index_operators = 18
    RULE_key_operators = 19
    RULE_operands = 20
    RULE_assign_stmt = 21
    RULE_lhs = 22
    RULE_if_stmt = 23
    RULE_while_stmt = 24
    RULE_for_stmt = 25
    RULE_forin_stmt = 26
    RULE_forof_stmt = 27
    RULE_break_stmt = 28
    RULE_continue_stmt = 29
    RULE_return_stmt = 30
    RULE_funcalls = 31
    RULE_block_stmt = 32
    RULE_stmt = 33
    RULE_indexdecl = 34
    RULE_json_lit = 35
    RULE_listkeyvalue = 36
    RULE_array_lit = 37
    RULE_normal_lit = 38
    RULE_primtypes = 39

    ruleNames =  [ "program", "manydecls", "constant_decl", "funcdecl", 
                   "vardecl_stmt", "var_temp", "var_constant", "paralist", 
                   "paradecl", "exp_0", "exp_1", "exp_2", "exp_3", "exp_4", 
                   "exp_5", "exp_6", "exp_7", "exp_8", "index_operators", 
                   "key_operators", "operands", "assign_stmt", "lhs", "if_stmt", 
                   "while_stmt", "for_stmt", "forin_stmt", "forof_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "funcalls", 
                   "block_stmt", "stmt", "indexdecl", "json_lit", "listkeyvalue", 
                   "array_lit", "normal_lit", "primtypes" ]

    EOF = Token.EOF
    WS=1
    COMMENT_LINES=2
    NORM_ID=3
    CONST_ID=4
    NUMBER_LIT=5
    BOOLEAN_LIT=6
    DOLLAR=7
    STRINGLIT=8
    ADD=9
    MUL=10
    NOT=11
    OR=12
    NEQ=13
    LT=14
    LTEQ=15
    ASSIGN=16
    SUB=17
    DIV=18
    MOD=19
    AND=20
    EQ=21
    GT=22
    GTEQ=23
    STR_ADD=24
    STR_COMPARE=25
    LB=26
    RB=27
    LP=28
    RP=29
    SM=30
    CM=31
    LS=32
    RS=33
    DOT=34
    COLON=35
    BREAK=36
    CONTINUE=37
    IF=38
    ELSE=39
    ELIF=40
    WHILE=41
    FOR=42
    OF=43
    IN=44
    LET=45
    TRUE=46
    FALSE=47
    CALL=48
    NUMBER=49
    BOOLEAN=50
    STRING=51
    JSON=52
    CONSTANT=53
    RETURN=54
    FUNCTION=55
    ARRAY=56
    UNCLOSE_STRING=57
    ILLEGAL_ESCAPE=58
    UNTERMINATED_COMMENT=59
    ERROR_CHAR=60

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSELParser.EOF, 0)

        def manydecls(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.ManydeclsContext)
            else:
                return self.getTypedRuleContext(CSELParser.ManydeclsContext,i)


        def getRuleIndex(self):
            return CSELParser.RULE_program




    def program(self):

        localctx = CSELParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.manydecls()
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.LET) | (1 << CSELParser.CONSTANT) | (1 << CSELParser.FUNCTION))) != 0)):
                    break

            self.state = 85
            self.match(CSELParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ManydeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl_stmt(self):
            return self.getTypedRuleContext(CSELParser.Vardecl_stmtContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(CSELParser.FuncdeclContext,0)


        def constant_decl(self):
            return self.getTypedRuleContext(CSELParser.Constant_declContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_manydecls




    def manydecls(self):

        localctx = CSELParser.ManydeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_manydecls)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.LET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.vardecl_stmt()
                pass
            elif token in [CSELParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.funcdecl()
                pass
            elif token in [CSELParser.CONSTANT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.constant_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTANT(self):
            return self.getToken(CSELParser.CONSTANT, 0)

        def var_constant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Var_constantContext)
            else:
                return self.getTypedRuleContext(CSELParser.Var_constantContext,i)


        def SM(self):
            return self.getToken(CSELParser.SM, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.CM)
            else:
                return self.getToken(CSELParser.CM, i)

        def getRuleIndex(self):
            return CSELParser.RULE_constant_decl




    def constant_decl(self):

        localctx = CSELParser.Constant_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_constant_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(CSELParser.CONSTANT)
            self.state = 93
            self.var_constant()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.CM:
                self.state = 94
                self.match(CSELParser.CM)
                self.state = 95
                self.var_constant()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(CSELParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(CSELParser.FUNCTION, 0)

        def NORM_ID(self):
            return self.getToken(CSELParser.NORM_ID, 0)

        def LB(self):
            return self.getToken(CSELParser.LB, 0)

        def RB(self):
            return self.getToken(CSELParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(CSELParser.Block_stmtContext,0)


        def paralist(self):
            return self.getTypedRuleContext(CSELParser.ParalistContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_funcdecl




    def funcdecl(self):

        localctx = CSELParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(CSELParser.FUNCTION)
            self.state = 104
            self.match(CSELParser.NORM_ID)
            self.state = 105
            self.match(CSELParser.LB)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.NORM_ID or _la==CSELParser.CONST_ID:
                self.state = 106
                self.paralist()


            self.state = 109
            self.match(CSELParser.RB)
            self.state = 110
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(CSELParser.LET, 0)

        def var_temp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Var_tempContext)
            else:
                return self.getTypedRuleContext(CSELParser.Var_tempContext,i)


        def SM(self):
            return self.getToken(CSELParser.SM, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.CM)
            else:
                return self.getToken(CSELParser.CM, i)

        def getRuleIndex(self):
            return CSELParser.RULE_vardecl_stmt




    def vardecl_stmt(self):

        localctx = CSELParser.Vardecl_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(CSELParser.LET)
            self.state = 113
            self.var_temp()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.CM:
                self.state = 114
                self.match(CSELParser.CM)
                self.state = 115
                self.var_temp()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
            self.match(CSELParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_tempContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORM_ID(self):
            return self.getToken(CSELParser.NORM_ID, 0)

        def index_operators(self):
            return self.getTypedRuleContext(CSELParser.Index_operatorsContext,0)


        def COLON(self):
            return self.getToken(CSELParser.COLON, 0)

        def primtypes(self):
            return self.getTypedRuleContext(CSELParser.PrimtypesContext,0)


        def ASSIGN(self):
            return self.getToken(CSELParser.ASSIGN, 0)

        def exp_0(self):
            return self.getTypedRuleContext(CSELParser.Exp_0Context,0)


        def getRuleIndex(self):
            return CSELParser.RULE_var_temp




    def var_temp(self):

        localctx = CSELParser.Var_tempContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_temp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(CSELParser.NORM_ID)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.LS:
                self.state = 124
                self.index_operators()


            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.COLON:
                self.state = 127
                self.match(CSELParser.COLON)
                self.state = 128
                self.primtypes()


            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.ASSIGN:
                self.state = 131
                self.match(CSELParser.ASSIGN)
                self.state = 132
                self.exp_0()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_constantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST_ID(self):
            return self.getToken(CSELParser.CONST_ID, 0)

        def index_operators(self):
            return self.getTypedRuleContext(CSELParser.Index_operatorsContext,0)


        def COLON(self):
            return self.getToken(CSELParser.COLON, 0)

        def primtypes(self):
            return self.getTypedRuleContext(CSELParser.PrimtypesContext,0)


        def ASSIGN(self):
            return self.getToken(CSELParser.ASSIGN, 0)

        def exp_0(self):
            return self.getTypedRuleContext(CSELParser.Exp_0Context,0)


        def getRuleIndex(self):
            return CSELParser.RULE_var_constant




    def var_constant(self):

        localctx = CSELParser.Var_constantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(CSELParser.CONST_ID)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.LS:
                self.state = 136
                self.index_operators()


            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.COLON:
                self.state = 139
                self.match(CSELParser.COLON)
                self.state = 140
                self.primtypes()


            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.ASSIGN:
                self.state = 143
                self.match(CSELParser.ASSIGN)
                self.state = 144
                self.exp_0()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paradecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.ParadeclContext)
            else:
                return self.getTypedRuleContext(CSELParser.ParadeclContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.CM)
            else:
                return self.getToken(CSELParser.CM, i)

        def getRuleIndex(self):
            return CSELParser.RULE_paralist




    def paralist(self):

        localctx = CSELParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paralist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.paradecl()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.CM:
                self.state = 148
                self.match(CSELParser.CM)
                self.state = 149
                self.paradecl()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParadeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORM_ID(self):
            return self.getToken(CSELParser.NORM_ID, 0)

        def CONST_ID(self):
            return self.getToken(CSELParser.CONST_ID, 0)

        def indexdecl(self):
            return self.getTypedRuleContext(CSELParser.IndexdeclContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_paradecl




    def paradecl(self):

        localctx = CSELParser.ParadeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paradecl)
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(CSELParser.NORM_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(CSELParser.CONST_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.indexdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_0Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Exp_1Context)
            else:
                return self.getTypedRuleContext(CSELParser.Exp_1Context,i)


        def STR_ADD(self):
            return self.getToken(CSELParser.STR_ADD, 0)

        def STR_COMPARE(self):
            return self.getToken(CSELParser.STR_COMPARE, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_exp_0




    def exp_0(self):

        localctx = CSELParser.Exp_0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exp_0)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.exp_1()
                self.state = 161
                self.match(CSELParser.STR_ADD)
                self.state = 162
                self.exp_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.exp_1()
                self.state = 165
                self.match(CSELParser.STR_COMPARE)
                self.state = 166
                self.exp_1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.exp_1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Exp_2Context)
            else:
                return self.getTypedRuleContext(CSELParser.Exp_2Context,i)


        def EQ(self):
            return self.getToken(CSELParser.EQ, 0)

        def NEQ(self):
            return self.getToken(CSELParser.NEQ, 0)

        def LT(self):
            return self.getToken(CSELParser.LT, 0)

        def GT(self):
            return self.getToken(CSELParser.GT, 0)

        def LTEQ(self):
            return self.getToken(CSELParser.LTEQ, 0)

        def GTEQ(self):
            return self.getToken(CSELParser.GTEQ, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_exp_1




    def exp_1(self):

        localctx = CSELParser.Exp_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exp_1)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.exp_2(0)
                self.state = 172
                self.match(CSELParser.EQ)
                self.state = 173
                self.exp_2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.exp_2(0)
                self.state = 176
                self.match(CSELParser.NEQ)
                self.state = 177
                self.exp_2(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.exp_2(0)
                self.state = 180
                self.match(CSELParser.LT)
                self.state = 181
                self.exp_2(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
                self.exp_2(0)
                self.state = 184
                self.match(CSELParser.GT)
                self.state = 185
                self.exp_2(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 187
                self.exp_2(0)
                self.state = 188
                self.match(CSELParser.LTEQ)
                self.state = 189
                self.exp_2(0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 191
                self.exp_2(0)
                self.state = 192
                self.match(CSELParser.GTEQ)
                self.state = 193
                self.exp_2(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 195
                self.exp_2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_3(self):
            return self.getTypedRuleContext(CSELParser.Exp_3Context,0)


        def exp_2(self):
            return self.getTypedRuleContext(CSELParser.Exp_2Context,0)


        def OR(self):
            return self.getToken(CSELParser.OR, 0)

        def AND(self):
            return self.getToken(CSELParser.AND, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_exp_2



    def exp_2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSELParser.Exp_2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_exp_2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.exp_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 207
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = CSELParser.Exp_2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_2)
                        self.state = 201
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 202
                        self.match(CSELParser.OR)
                        self.state = 203
                        self.exp_3(0)
                        pass

                    elif la_ == 2:
                        localctx = CSELParser.Exp_2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_2)
                        self.state = 204
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 205
                        self.match(CSELParser.AND)
                        self.state = 206
                        self.exp_3(0)
                        pass

             
                self.state = 211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp_3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_4(self):
            return self.getTypedRuleContext(CSELParser.Exp_4Context,0)


        def exp_3(self):
            return self.getTypedRuleContext(CSELParser.Exp_3Context,0)


        def ADD(self):
            return self.getToken(CSELParser.ADD, 0)

        def SUB(self):
            return self.getToken(CSELParser.SUB, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_exp_3



    def exp_3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSELParser.Exp_3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_exp_3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.exp_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 221
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = CSELParser.Exp_3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_3)
                        self.state = 215
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 216
                        self.match(CSELParser.ADD)
                        self.state = 217
                        self.exp_4(0)
                        pass

                    elif la_ == 2:
                        localctx = CSELParser.Exp_3Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_3)
                        self.state = 218
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 219
                        self.match(CSELParser.SUB)
                        self.state = 220
                        self.exp_4(0)
                        pass

             
                self.state = 225
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp_4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_5(self):
            return self.getTypedRuleContext(CSELParser.Exp_5Context,0)


        def exp_4(self):
            return self.getTypedRuleContext(CSELParser.Exp_4Context,0)


        def MUL(self):
            return self.getToken(CSELParser.MUL, 0)

        def DIV(self):
            return self.getToken(CSELParser.DIV, 0)

        def MOD(self):
            return self.getToken(CSELParser.MOD, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_exp_4



    def exp_4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSELParser.Exp_4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_exp_4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.exp_5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 240
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 238
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = CSELParser.Exp_4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_4)
                        self.state = 229
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 230
                        self.match(CSELParser.MUL)
                        self.state = 231
                        self.exp_5()
                        pass

                    elif la_ == 2:
                        localctx = CSELParser.Exp_4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_4)
                        self.state = 232
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 233
                        self.match(CSELParser.DIV)
                        self.state = 234
                        self.exp_5()
                        pass

                    elif la_ == 3:
                        localctx = CSELParser.Exp_4Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_4)
                        self.state = 235
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 236
                        self.match(CSELParser.MOD)
                        self.state = 237
                        self.exp_5()
                        pass

             
                self.state = 242
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp_5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(CSELParser.NOT, 0)

        def exp_5(self):
            return self.getTypedRuleContext(CSELParser.Exp_5Context,0)


        def exp_6(self):
            return self.getTypedRuleContext(CSELParser.Exp_6Context,0)


        def getRuleIndex(self):
            return CSELParser.RULE_exp_5




    def exp_5(self):

        localctx = CSELParser.Exp_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exp_5)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(CSELParser.NOT)
                self.state = 244
                self.exp_5()
                pass
            elif token in [CSELParser.NORM_ID, CSELParser.CONST_ID, CSELParser.NUMBER_LIT, CSELParser.BOOLEAN_LIT, CSELParser.STRINGLIT, CSELParser.SUB, CSELParser.LB, CSELParser.LP, CSELParser.LS, CSELParser.CALL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.exp_6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(CSELParser.SUB, 0)

        def exp_6(self):
            return self.getTypedRuleContext(CSELParser.Exp_6Context,0)


        def exp_7(self):
            return self.getTypedRuleContext(CSELParser.Exp_7Context,0)


        def getRuleIndex(self):
            return CSELParser.RULE_exp_6




    def exp_6(self):

        localctx = CSELParser.Exp_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp_6)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(CSELParser.SUB)
                self.state = 249
                self.exp_6()
                pass
            elif token in [CSELParser.NORM_ID, CSELParser.CONST_ID, CSELParser.NUMBER_LIT, CSELParser.BOOLEAN_LIT, CSELParser.STRINGLIT, CSELParser.LB, CSELParser.LP, CSELParser.LS, CSELParser.CALL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.exp_7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_8(self):
            return self.getTypedRuleContext(CSELParser.Exp_8Context,0)


        def exp_7(self):
            return self.getTypedRuleContext(CSELParser.Exp_7Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(CSELParser.Index_operatorsContext,0)


        def key_operators(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Key_operatorsContext)
            else:
                return self.getTypedRuleContext(CSELParser.Key_operatorsContext,i)


        def getRuleIndex(self):
            return CSELParser.RULE_exp_7



    def exp_7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSELParser.Exp_7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_exp_7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.exp_8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 264
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = CSELParser.Exp_7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_7)
                        self.state = 256
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 257
                        self.index_operators()
                        pass

                    elif la_ == 2:
                        localctx = CSELParser.Exp_7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_7)
                        self.state = 258
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 260 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 259
                                self.key_operators()

                            else:
                                raise NoViableAltException(self)
                            self.state = 262 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                        pass

             
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp_8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(CSELParser.LB, 0)

        def exp_0(self):
            return self.getTypedRuleContext(CSELParser.Exp_0Context,0)


        def RB(self):
            return self.getToken(CSELParser.RB, 0)

        def operands(self):
            return self.getTypedRuleContext(CSELParser.OperandsContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_exp_8




    def exp_8(self):

        localctx = CSELParser.Exp_8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp_8)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(CSELParser.LB)
                self.state = 270
                self.exp_0()
                self.state = 271
                self.match(CSELParser.RB)
                pass
            elif token in [CSELParser.NORM_ID, CSELParser.CONST_ID, CSELParser.NUMBER_LIT, CSELParser.BOOLEAN_LIT, CSELParser.STRINGLIT, CSELParser.LP, CSELParser.LS, CSELParser.CALL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.operands()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(CSELParser.LS, 0)

        def exp_0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Exp_0Context)
            else:
                return self.getTypedRuleContext(CSELParser.Exp_0Context,i)


        def RS(self):
            return self.getToken(CSELParser.RS, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.CM)
            else:
                return self.getToken(CSELParser.CM, i)

        def getRuleIndex(self):
            return CSELParser.RULE_index_operators




    def index_operators(self):

        localctx = CSELParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_index_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(CSELParser.LS)
            self.state = 277
            self.exp_0()
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.CM:
                self.state = 278
                self.match(CSELParser.CM)
                self.state = 279
                self.exp_0()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 285
            self.match(CSELParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Key_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CSELParser.LP, 0)

        def exp_0(self):
            return self.getTypedRuleContext(CSELParser.Exp_0Context,0)


        def RP(self):
            return self.getToken(CSELParser.RP, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_key_operators




    def key_operators(self):

        localctx = CSELParser.Key_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_key_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(CSELParser.LP)
            self.state = 288
            self.exp_0()
            self.state = 289
            self.match(CSELParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(CSELParser.NUMBER_LIT, 0)

        def funcalls(self):
            return self.getTypedRuleContext(CSELParser.FuncallsContext,0)


        def NORM_ID(self):
            return self.getToken(CSELParser.NORM_ID, 0)

        def CONST_ID(self):
            return self.getToken(CSELParser.CONST_ID, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(CSELParser.BOOLEAN_LIT, 0)

        def STRINGLIT(self):
            return self.getToken(CSELParser.STRINGLIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(CSELParser.Array_litContext,0)


        def json_lit(self):
            return self.getTypedRuleContext(CSELParser.Json_litContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_operands




    def operands(self):

        localctx = CSELParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_operands)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(CSELParser.NUMBER_LIT)
                pass
            elif token in [CSELParser.CALL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                self.funcalls()
                pass
            elif token in [CSELParser.NORM_ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 293
                self.match(CSELParser.NORM_ID)
                pass
            elif token in [CSELParser.CONST_ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 294
                self.match(CSELParser.CONST_ID)
                pass
            elif token in [CSELParser.BOOLEAN_LIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 295
                self.match(CSELParser.BOOLEAN_LIT)
                pass
            elif token in [CSELParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 6)
                self.state = 296
                self.match(CSELParser.STRINGLIT)
                pass
            elif token in [CSELParser.LS]:
                self.enterOuterAlt(localctx, 7)
                self.state = 297
                self.array_lit()
                pass
            elif token in [CSELParser.LP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 298
                self.json_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(CSELParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(CSELParser.ASSIGN, 0)

        def exp_0(self):
            return self.getTypedRuleContext(CSELParser.Exp_0Context,0)


        def SM(self):
            return self.getToken(CSELParser.SM, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_assign_stmt




    def assign_stmt(self):

        localctx = CSELParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.lhs()
            self.state = 302
            self.match(CSELParser.ASSIGN)
            self.state = 303
            self.exp_0()
            self.state = 304
            self.match(CSELParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORM_ID(self):
            return self.getToken(CSELParser.NORM_ID, 0)

        def CONST_ID(self):
            return self.getToken(CSELParser.CONST_ID, 0)

        def exp_7(self):
            return self.getTypedRuleContext(CSELParser.Exp_7Context,0)


        def getRuleIndex(self):
            return CSELParser.RULE_lhs




    def lhs(self):

        localctx = CSELParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_lhs)
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.match(CSELParser.NORM_ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
                self.match(CSELParser.CONST_ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 308
                self.exp_7(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSELParser.IF, 0)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.LB)
            else:
                return self.getToken(CSELParser.LB, i)

        def exp_0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Exp_0Context)
            else:
                return self.getTypedRuleContext(CSELParser.Exp_0Context,i)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.RB)
            else:
                return self.getToken(CSELParser.RB, i)

        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(CSELParser.Block_stmtContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.ELIF)
            else:
                return self.getToken(CSELParser.ELIF, i)

        def ELSE(self):
            return self.getToken(CSELParser.ELSE, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_if_stmt




    def if_stmt(self):

        localctx = CSELParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(CSELParser.IF)
            self.state = 312
            self.match(CSELParser.LB)
            self.state = 313
            self.exp_0()
            self.state = 314
            self.match(CSELParser.RB)
            self.state = 315
            self.block_stmt()
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.ELIF:
                self.state = 316
                self.match(CSELParser.ELIF)
                self.state = 317
                self.match(CSELParser.LB)
                self.state = 318
                self.exp_0()
                self.state = 319
                self.match(CSELParser.RB)
                self.state = 320
                self.block_stmt()
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSELParser.ELSE:
                self.state = 327
                self.match(CSELParser.ELSE)
                self.state = 328
                self.block_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CSELParser.WHILE, 0)

        def LB(self):
            return self.getToken(CSELParser.LB, 0)

        def exp_0(self):
            return self.getTypedRuleContext(CSELParser.Exp_0Context,0)


        def RB(self):
            return self.getToken(CSELParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(CSELParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_while_stmt




    def while_stmt(self):

        localctx = CSELParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(CSELParser.WHILE)
            self.state = 332
            self.match(CSELParser.LB)
            self.state = 333
            self.exp_0()
            self.state = 334
            self.match(CSELParser.RB)
            self.state = 335
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forin_stmt(self):
            return self.getTypedRuleContext(CSELParser.Forin_stmtContext,0)


        def forof_stmt(self):
            return self.getTypedRuleContext(CSELParser.Forof_stmtContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_for_stmt




    def for_stmt(self):

        localctx = CSELParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_stmt)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.forin_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.forof_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forin_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSELParser.FOR, 0)

        def NORM_ID(self):
            return self.getToken(CSELParser.NORM_ID, 0)

        def IN(self):
            return self.getToken(CSELParser.IN, 0)

        def exp_0(self):
            return self.getTypedRuleContext(CSELParser.Exp_0Context,0)


        def block_stmt(self):
            return self.getTypedRuleContext(CSELParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_forin_stmt




    def forin_stmt(self):

        localctx = CSELParser.Forin_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_forin_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(CSELParser.FOR)
            self.state = 342
            self.match(CSELParser.NORM_ID)
            self.state = 343
            self.match(CSELParser.IN)
            self.state = 344
            self.exp_0()
            self.state = 345
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forof_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSELParser.FOR, 0)

        def NORM_ID(self):
            return self.getToken(CSELParser.NORM_ID, 0)

        def OF(self):
            return self.getToken(CSELParser.OF, 0)

        def exp_0(self):
            return self.getTypedRuleContext(CSELParser.Exp_0Context,0)


        def block_stmt(self):
            return self.getTypedRuleContext(CSELParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSELParser.RULE_forof_stmt




    def forof_stmt(self):

        localctx = CSELParser.Forof_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_forof_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(CSELParser.FOR)
            self.state = 348
            self.match(CSELParser.NORM_ID)
            self.state = 349
            self.match(CSELParser.OF)
            self.state = 350
            self.exp_0()
            self.state = 351
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSELParser.BREAK, 0)

        def SM(self):
            return self.getToken(CSELParser.SM, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_break_stmt




    def break_stmt(self):

        localctx = CSELParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(CSELParser.BREAK)
            self.state = 354
            self.match(CSELParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSELParser.CONTINUE, 0)

        def SM(self):
            return self.getToken(CSELParser.SM, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_continue_stmt




    def continue_stmt(self):

        localctx = CSELParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(CSELParser.CONTINUE)
            self.state = 357
            self.match(CSELParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSELParser.RETURN, 0)

        def SM(self):
            return self.getToken(CSELParser.SM, 0)

        def exp_0(self):
            return self.getTypedRuleContext(CSELParser.Exp_0Context,0)


        def getRuleIndex(self):
            return CSELParser.RULE_return_stmt




    def return_stmt(self):

        localctx = CSELParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(CSELParser.RETURN)
            self.state = 361
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.NORM_ID) | (1 << CSELParser.CONST_ID) | (1 << CSELParser.NUMBER_LIT) | (1 << CSELParser.BOOLEAN_LIT) | (1 << CSELParser.STRINGLIT) | (1 << CSELParser.NOT) | (1 << CSELParser.SUB) | (1 << CSELParser.LB) | (1 << CSELParser.LP) | (1 << CSELParser.LS) | (1 << CSELParser.CALL))) != 0):
                self.state = 360
                self.exp_0()


            self.state = 363
            self.match(CSELParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALL(self):
            return self.getToken(CSELParser.CALL, 0)

        def LB(self):
            return self.getToken(CSELParser.LB, 0)

        def NORM_ID(self):
            return self.getToken(CSELParser.NORM_ID, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.CM)
            else:
                return self.getToken(CSELParser.CM, i)

        def RB(self):
            return self.getToken(CSELParser.RB, 0)

        def LS(self):
            return self.getToken(CSELParser.LS, 0)

        def RS(self):
            return self.getToken(CSELParser.RS, 0)

        def exp_0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Exp_0Context)
            else:
                return self.getTypedRuleContext(CSELParser.Exp_0Context,i)


        def getRuleIndex(self):
            return CSELParser.RULE_funcalls




    def funcalls(self):

        localctx = CSELParser.FuncallsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_funcalls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(CSELParser.CALL)
            self.state = 366
            self.match(CSELParser.LB)
            self.state = 367
            self.match(CSELParser.NORM_ID)
            self.state = 368
            self.match(CSELParser.CM)

            self.state = 369
            self.match(CSELParser.LS)
            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.NORM_ID) | (1 << CSELParser.CONST_ID) | (1 << CSELParser.NUMBER_LIT) | (1 << CSELParser.BOOLEAN_LIT) | (1 << CSELParser.STRINGLIT) | (1 << CSELParser.NOT) | (1 << CSELParser.SUB) | (1 << CSELParser.LB) | (1 << CSELParser.LP) | (1 << CSELParser.LS) | (1 << CSELParser.CALL))) != 0):
                self.state = 370
                self.exp_0()
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSELParser.CM:
                    self.state = 371
                    self.match(CSELParser.CM)
                    self.state = 372
                    self.exp_0()
                    self.state = 377
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 380
            self.match(CSELParser.RS)
            self.state = 382
            self.match(CSELParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CSELParser.LP, 0)

        def RP(self):
            return self.getToken(CSELParser.RP, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.StmtContext)
            else:
                return self.getTypedRuleContext(CSELParser.StmtContext,i)


        def getRuleIndex(self):
            return CSELParser.RULE_block_stmt




    def block_stmt(self):

        localctx = CSELParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(CSELParser.LP)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.NORM_ID) | (1 << CSELParser.CONST_ID) | (1 << CSELParser.NUMBER_LIT) | (1 << CSELParser.BOOLEAN_LIT) | (1 << CSELParser.STRINGLIT) | (1 << CSELParser.LB) | (1 << CSELParser.LP) | (1 << CSELParser.LS) | (1 << CSELParser.BREAK) | (1 << CSELParser.CONTINUE) | (1 << CSELParser.IF) | (1 << CSELParser.WHILE) | (1 << CSELParser.FOR) | (1 << CSELParser.LET) | (1 << CSELParser.CALL) | (1 << CSELParser.CONSTANT) | (1 << CSELParser.RETURN))) != 0):
                self.state = 385
                self.stmt()
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 391
            self.match(CSELParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant_decl(self):
            return self.getTypedRuleContext(CSELParser.Constant_declContext,0)


        def vardecl_stmt(self):
            return self.getTypedRuleContext(CSELParser.Vardecl_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(CSELParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(CSELParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(CSELParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(CSELParser.While_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(CSELParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(CSELParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(CSELParser.Return_stmtContext,0)


        def funcalls(self):
            return self.getTypedRuleContext(CSELParser.FuncallsContext,0)


        def SM(self):
            return self.getToken(CSELParser.SM, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_stmt




    def stmt(self):

        localctx = CSELParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_stmt)
        try:
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.constant_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.vardecl_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 395
                self.assign_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 396
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 397
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 398
                self.while_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 399
                self.break_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 400
                self.continue_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 401
                self.return_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 402
                self.funcalls()
                self.state = 403
                self.match(CSELParser.SM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORM_ID(self):
            return self.getToken(CSELParser.NORM_ID, 0)

        def CONST_ID(self):
            return self.getToken(CSELParser.CONST_ID, 0)

        def index_operators(self):
            return self.getTypedRuleContext(CSELParser.Index_operatorsContext,0)


        def LS(self):
            return self.getToken(CSELParser.LS, 0)

        def RS(self):
            return self.getToken(CSELParser.RS, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_indexdecl




    def indexdecl(self):

        localctx = CSELParser.IndexdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_indexdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            _la = self._input.LA(1)
            if not(_la==CSELParser.NORM_ID or _la==CSELParser.CONST_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 408
                self.index_operators()
                pass

            elif la_ == 2:
                self.state = 409
                self.match(CSELParser.LS)
                self.state = 410
                self.match(CSELParser.RS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Json_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CSELParser.LP, 0)

        def listkeyvalue(self):
            return self.getTypedRuleContext(CSELParser.ListkeyvalueContext,0)


        def RP(self):
            return self.getToken(CSELParser.RP, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.WS)
            else:
                return self.getToken(CSELParser.WS, i)

        def getRuleIndex(self):
            return CSELParser.RULE_json_lit




    def json_lit(self):

        localctx = CSELParser.Json_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_json_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(CSELParser.LP)
            self.state = 417
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.WS:
                self.state = 414
                self.match(CSELParser.WS)
                self.state = 419
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 420
            self.listkeyvalue()
            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.WS:
                self.state = 421
                self.match(CSELParser.WS)
                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 427
            self.match(CSELParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListkeyvalueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NORM_ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.NORM_ID)
            else:
                return self.getToken(CSELParser.NORM_ID, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.COLON)
            else:
                return self.getToken(CSELParser.COLON, i)

        def normal_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Normal_litContext)
            else:
                return self.getTypedRuleContext(CSELParser.Normal_litContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.WS)
            else:
                return self.getToken(CSELParser.WS, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.CM)
            else:
                return self.getToken(CSELParser.CM, i)

        def getRuleIndex(self):
            return CSELParser.RULE_listkeyvalue




    def listkeyvalue(self):

        localctx = CSELParser.ListkeyvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_listkeyvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(CSELParser.NORM_ID)
            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.WS:
                self.state = 430
                self.match(CSELParser.WS)
                self.state = 435
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 436
            self.match(CSELParser.COLON)
            self.state = 440
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.WS:
                self.state = 437
                self.match(CSELParser.WS)
                self.state = 442
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 443
            self.normal_lit()
            self.state = 474
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 447
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CSELParser.WS:
                        self.state = 444
                        self.match(CSELParser.WS)
                        self.state = 449
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 450
                    self.match(CSELParser.CM)
                    self.state = 454
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CSELParser.WS:
                        self.state = 451
                        self.match(CSELParser.WS)
                        self.state = 456
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 457
                    self.match(CSELParser.NORM_ID)
                    self.state = 461
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CSELParser.WS:
                        self.state = 458
                        self.match(CSELParser.WS)
                        self.state = 463
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 464
                    self.match(CSELParser.COLON)
                    self.state = 468
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==CSELParser.WS:
                        self.state = 465
                        self.match(CSELParser.WS)
                        self.state = 470
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 471
                    self.normal_lit() 
                self.state = 476
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(CSELParser.LS, 0)

        def normal_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSELParser.Normal_litContext)
            else:
                return self.getTypedRuleContext(CSELParser.Normal_litContext,i)


        def RS(self):
            return self.getToken(CSELParser.RS, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.CM)
            else:
                return self.getToken(CSELParser.CM, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(CSELParser.WS)
            else:
                return self.getToken(CSELParser.WS, i)

        def getRuleIndex(self):
            return CSELParser.RULE_array_lit




    def array_lit(self):

        localctx = CSELParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(CSELParser.LS)
            self.state = 478
            self.normal_lit()
            self.state = 495
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSELParser.WS or _la==CSELParser.CM:
                self.state = 482
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSELParser.WS:
                    self.state = 479
                    self.match(CSELParser.WS)
                    self.state = 484
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 485
                self.match(CSELParser.CM)
                self.state = 489
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSELParser.WS:
                    self.state = 486
                    self.match(CSELParser.WS)
                    self.state = 491
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 492
                self.normal_lit()
                self.state = 497
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 498
            self.match(CSELParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LIT(self):
            return self.getToken(CSELParser.NUMBER_LIT, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(CSELParser.BOOLEAN_LIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(CSELParser.Array_litContext,0)


        def json_lit(self):
            return self.getTypedRuleContext(CSELParser.Json_litContext,0)


        def STRINGLIT(self):
            return self.getToken(CSELParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_normal_lit




    def normal_lit(self):

        localctx = CSELParser.Normal_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_normal_lit)
        try:
            self.state = 505
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSELParser.NUMBER_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.match(CSELParser.NUMBER_LIT)
                pass
            elif token in [CSELParser.BOOLEAN_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.match(CSELParser.BOOLEAN_LIT)
                pass
            elif token in [CSELParser.LS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 502
                self.array_lit()
                pass
            elif token in [CSELParser.LP]:
                self.enterOuterAlt(localctx, 4)
                self.state = 503
                self.json_lit()
                pass
            elif token in [CSELParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 504
                self.match(CSELParser.STRINGLIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimtypesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CSELParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(CSELParser.NUMBER, 0)

        def JSON(self):
            return self.getToken(CSELParser.JSON, 0)

        def ARRAY(self):
            return self.getToken(CSELParser.ARRAY, 0)

        def BOOLEAN(self):
            return self.getToken(CSELParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return CSELParser.RULE_primtypes




    def primtypes(self):

        localctx = CSELParser.PrimtypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_primtypes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSELParser.NUMBER) | (1 << CSELParser.BOOLEAN) | (1 << CSELParser.STRING) | (1 << CSELParser.JSON) | (1 << CSELParser.ARRAY))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.exp_2_sempred
        self._predicates[12] = self.exp_3_sempred
        self._predicates[13] = self.exp_4_sempred
        self._predicates[16] = self.exp_7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_2_sempred(self, localctx:Exp_2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp_3_sempred(self, localctx:Exp_3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp_4_sempred(self, localctx:Exp_4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def exp_7_sempred(self, localctx:Exp_7Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




