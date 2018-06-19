from __future__ import print_function
# This must be the first statement before other statements.
# You may only put a quoted or triple quoted string,
# Python comments, other future statements, or blank lines before the __future__ line.

try:
    import __builtin__
except ImportError:
    # Python 3
    import __builtins__ as __builtin__
import super_std as sstd
print = sstd.super_print('output.txt')(__builtin__.print)
raw_input = sstd.super_raw_input('output.txt')(__builtin__.raw_input)






import os

def check_service(service):
    #Check whether the service is active or not.
    command = "systemctl is-active %s" % service
    service_active = os.popen(command).readline()[:-1]

    #If the service is 'active', just print out the 'active' message and do nothing
    if service_active == "active":
        print("Service %s is active now!" % (service))
    #If the service is not 'active', try to help the user turn on the service
    else:
        print("Service %s is not active." % (service))
        start = start_service(service)
        if start == "active":
            print("We have already help you to start the service %s" % (service))
        else:
            print("Sorry, there are some error and we fail to help you start the service %s" % (service))

def start_service(service):
    #Try to turn on the service
    try:
        command = "systemctl enable %s.service" % service
        os.popen(command).readline()
        command = "systemctl start %s.service" % service
        os.popen(command).readline()
    except:
        print("\033[5;31;40mError message: ")
       # print(OSError)
        print("\033[0;37;40m")
        return 0

    #Re-check whether the service is active or not and return the result
    command = "systemctl is-active %s" % service
    service_active = os.popen(command).readline()[:-1]
    return service_active

#Absolutely process this command
os.popen("systemctl daemon-reload")

if __name__ == "__main__":
    print("\033[5;31;40mYou could quit anytime by enter 'q' or 'exit'!\033[0;37;40m")
    while True:
        service = raw_input("Please enter your service name: ")
        if (service == "q") or (service == "exit"):
            print("Exit this program")
            break
        else:
            check_service(service)
