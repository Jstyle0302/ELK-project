import os
import super_stdio as super

def check_service(service):
    #Check whether the service is active or not.
    command = "systemctl is-active %s" % service
    service_active = os.popen(command).readline()[:-1]

    #If the service is 'active', just super.super_print out the 'active' message and do nothing
    if service_active == "active":
        super.super_print("Service %s is active now!" % (service))
    #If the service is not 'active', try to help the user turn on the service
    else:
        super.super_print("Service %s is not active." % (service))
        start = start_service(service)
        if start == "active":
            super.super_print("We have already help you to start the service %s" % (service))
        else:
            super.super_print("Sorry, there are some error and we fail to help you start the service %s" % (service))

def start_service(service):
    #Try to turn on the service
    try:
        command = "systemctl enable %s.service" % service
        os.popen(command).readline()
        command = "systemctl start %s.service" % service
        os.popen(command).readline()
    except:
        super.super_print("\033[5;31;40mError message: ")
       # super.super_print(OSError)
        super.super_print("\033[0;37;40m")
        return 0

    #Re-check whether the service is active or not and return the result
    command = "systemctl is-active %s" % service
    service_active = os.popen(command).readline()[:-1]
    return service_active

#Absolutely process this command
os.popen("systemctl daemon-reload")

if __name__ == "__main__":
    super.super_print("\033[5;31;40mYou could quit anytime by enter 'q' or 'exit'!\033[0;37;40m")
    while True:
        service = super.super_raw_input("Please enter your service name: ")
        if (service == "q") or (service == "exit"):
            super.super_print("Exit this program")
            break
        else:
            check_service(service)
