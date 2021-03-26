# taking input from command line and printing
import webbrowser, sys 

if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])
print(address)