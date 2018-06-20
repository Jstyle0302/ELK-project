import os
import super_stdio as super
def check_firewall_port():
    #Receive the port number
    super.super_print("\033[5;31;40mYou could quit anytime by enter 'q' or 'exit'!\033[0;37;40m")
    port_number = super.super_raw_input("Please enter the port number you want to check: ")
    
    #Use the while loop to continuely receive the port number and check it.
    while True:
        #Only check the firewall at the specific port number when the port number is digital number
        if port_number.isdigit():
            tcp_wall = os.popen("firewall-cmd --query-port=%d/tcp" % int(port_number)).read()
            udp_wall = os.popen("firewall-cmd --query-port=%d/udp" % int(port_number)).read()
            if ("yes" in tcp_wall) and ("yes" in udp_wall):
                super.super_print("Both of the tcp and udp firewall protocal at your port number %d have already been opened." % int(port_number))
            elif "yes" in tcp_wall:
                super.super_print("The tcp firewall protocal at your port number %d has already been opened.\033[1;31;40m However, the udp firewall protocal has not yet been opened.\033[0;37;40m" % int(port_number))
            elif "yes" in udp_wall:
                super.super_print("The udp firewall protocal at your port number %d has already been opened.\033[1;31;40m However, the tcp firewall protocal has not yet been opened.\033[0;37;40m" % int(port_number))
            else:
                super.super_print("\033[1;31;40mBoth of the tcp and udp firewall protocal at your port number %d have not been opened.\033[0;37;40m" % int(port_number))
        #If user type the 'q' or 'exit', escape from the program
        elif("q" == port_number) or ("exit" == port_number):
            super.super_print("Exit this program!")
            break
        #When we cannot analysis the port number, pop out the error message.
        else:
            super.super_print("This is not an illegal port number!!")
        port_number = super.super_raw_input("Please enter the port number you want to check: ")

if __name__ == "__main__":
    check_firewall_port()

