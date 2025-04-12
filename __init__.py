import os

print ("Initializing vtube folder: " + os.getcwd())
if (os.path.exists("vtube/services.py")):
    from . import services
else:
    print("Services file does not exist")
    
