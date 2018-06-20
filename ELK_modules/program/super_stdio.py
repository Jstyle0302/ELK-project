from __future__ import print_function
# This must be the first statement before other statements.
# You may only put a quoted or triple quoted string,
# Python comments, other future statements, or blank lines before the __future__ line.
try:
    import __builtin__
except ImportError:
    # Python 3
    import __builtins__ as __builtin__

filename = "history.txt"

# Set the super_print not only print out the message but also save all of the interactive message
def super_print(*args, **kwargs):
    with open(filename,"a") as logfile:
        __builtin__.print(*args,file = logfile)
        print(*args,**kwargs)

# Set the super_raw_input not only receive the message but also save all of the interactive message
def super_raw_input(*args, **kwargs):
    with open(filename,"a") as logfile:
        logfile.write(*args,**kwargs)
        input_word = raw_input(*args,**kwargs)
        logfile.write(input_word+"\n")
    return input_word



if __name__ == "__main__":
    logfile = open(filename,"a")    
    super_print("Hello")
    str1 = date.today()
    super_print(str1)
    num = super_raw_input("Number: ")
    logfile.close()
    
