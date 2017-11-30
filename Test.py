from AST import *

a = Ast.random_generate()
# test
a.print()
print(a.evaluate(1.0))
print(str(a.count_nodes()))

print("//")
test_expr = BinOp('+', Num(666), Num(69))
b = Ast(test_expr)
nodes = b.count_nodes()
print(str(nodes))

son = Ast(Ast.cross_over(a, b))
print("ahi va")
son.print()
print("fue")
