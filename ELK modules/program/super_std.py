from __future__ import print_function
# This must be the first statement before other statements.
# You may only put a quoted or triple quoted string,
# Python comments, other future statements, or blank lines before the __future__ line.

try:
    import __builtin__
except ImportError:
    # Python 3
    import __builtins__ as __builtin__
 
def super_print(filename):
    '''filename is the file where output will be written'''
    def wrap(func):
        '''func is the function you are "overriding", i.e. wrapping'''
        def wrapped_func(*args,**kwargs):
            '''*args and **kwargs are the arguments supplied 
            to the overridden function'''
            #use with statement to open, write to, and close the file safely
            with open(filename,'a') as outputfile:
                outputfile.write(*args,**kwargs)
                outputfile.write("\n")
            #now original function executed with its arguments as normal
            return func(*args,**kwargs)
        return wrapped_func
    return wrap

def super_raw_input(filename):
    '''filename is the file where output will be written'''
    def wrap(func):
        '''func is the function you are "overriding", i.e. wrapping'''
        def wrapped_func(*args,**kwargs):
            '''*args and **kwargs are the arguments supplied
            to the overridden function'''
            #use with statement to open, write to, and close the file safely
            with open(filename,'a') as outputfile:
                outputfile.write(*args,**kwargs)
                input_word = func(*args,**kwargs)
                outputfile.write(input_word)
                outputfile.write("\n")
            return input_word
        return wrapped_func
    return wrap

def setting(func):
    print = super_print('output.txt')(__builtin__.print)
    raw_input = super_raw_input('output.txt')(__builtin__.raw_input)
    return func


if __name__ == "__main__":
    print = super_print('output.txt')(__builtin__.print)
    raw_input = super_raw_input('output.txt')(__builtin__.raw_input)
    print("hello joe")
    print("2")
    raw_input("number: ")

