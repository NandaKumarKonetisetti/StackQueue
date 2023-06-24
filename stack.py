class Stack:
    def __init__(self):
        self.stack =[]
        
    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        if(self.is_empty()):
            return None
        return self.stack.pop()
    def is_empty(self):
        return len(self.stack)==0
    def print_elements(self):
        return(str(self.stack))


st = Stack()
print("Enter the elements of a stack")
li = list(map(int,input().split()))
for val in li:
    st.push(val)
st.pop()
st.push(77)
print(f"{st.print_elements()}")
print(f"is stack empty :{st.is_empty()}")

        
        
