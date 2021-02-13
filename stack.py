def create_stack():
    st = []
    return st

def push(stack,x):
    
    return stack.append(x)

def isEmpty(stack):
    
    if len(stack)==0:
        return True
    else:
        return False
def pop(stack):
    if isEmpty(stack)==True:
        print("stack is already empty")
    else:
        length = len(stack)
        value = stack[length-1]
        stack.remove(value)
        return value

stack = create_stack()
print(stack)  
push(stack,3)
print(stack)
push(stack,6)
print(stack)
r = pop(stack)
print(r)
print(stack)

    