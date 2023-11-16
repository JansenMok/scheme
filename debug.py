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

# expr = Pair(Pair('+', Pair('x', Pair(2, nil))), nil)
# print(do_quote_form(expr, env))

# PROBLEM 8 DEBUGGING
from scheme_classes import *
global_frame = create_global_frame()
formals = Pair('fuck', nil)
vals = Pair(69, nil)
new_frame = global_frame.make_child_frame(formals, vals)
# # print(new_frame.parent)
# print(new_frame.lookup('fuck'))
print(new_frame.bindings)
# print(global_frame.lookup('fuck'))

# global_frame = create_global_frame()
# frame = global_frame.make_child_frame(nil, nil)
# print(frame.parent is global_frame)

# PROBLEM 9 DEBUGGING
import math
import numbers
import operator
import sys

# from pair import Pair, nil, repl_str
from scheme_reader import *
from scheme_eval_apply import *
from scheme_classes import *
from scheme_utils import *
import builtins
from pair import *
import sys
from scheme_utils import *
from ucb import main, trace
import scheme_forms
from scheme_builtins import *
import numbers
import sys
import os
from scheme_forms import *
from scheme_builtins import *

do_define_form(read_line(""))