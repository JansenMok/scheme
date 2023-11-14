# PROBLEM 2 DEBUGGING
from scheme import *
env = create_global_frame()
# twos = Pair(2, Pair(2, nil))
# plus = BuiltinProcedure(scheme_add) # + procedure
# scheme_apply(plus, twos, env) # Type SchemeError if you think this errors

# from scheme_builtins import *
# print(scheme_add(1))
# print(scheme_add(2))
# print(scheme_add(scheme_add(3)))
# print(scheme_add(1, 3))
# s= [2, 2, 2]
# print(scheme_add(2, 2))
# print(plus.py_func(*s))

# PROBLEM 3 DEBUGGING
# from scheme_eval_apply import *
# # expr = Pair(1, Pair(2, Pair(3, nil)))
# expr = Pair('+', Pair(Pair('+', Pair(1, Pair(2, nil))), Pair(69, nil)))
# print(f'original: {expr}')
# scheme_eval(expr, env)

# PROBLEM 6 DEBUGGING
from scheme_reader import *
# from scheme_forms import *
# do_quote_form(Pair(Pair('+', Pair('x', Pair(2, nil))), nil), env)

# (cons (cons + (cons x (cons 2 nil))) nil)

# print(do_quote_form(read_line("((+ x 2))"), env))
# print(read_line("((+ x 2))"))

expr = Pair(Pair('+', Pair('x', Pair(2, nil))), nil)
print(do_quote_form(expr, env))