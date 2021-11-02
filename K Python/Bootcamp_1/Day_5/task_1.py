class HumanNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        
        
try:
    human_name = input("What is your child name: ")
    if any(char.isdigit() for char in human_name):
        raise HumanNameError
        
    if human_name[0].islower():
        raise HumanNameError
except HumanNameError:
    print("Your child \"Name\" shouldn't contain numbers...!!!\n\"Name\" should be start with capital letter...!!!")
    
