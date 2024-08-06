class stack:
 
 def __init__(self) :
  self.items = []
 
 def push(self, item):
  self.items.append(item)

 def is_empty(self):
   return len(self.items) == 0;

 def top(self):
  if(self.is_empty()):
    print("Stack is empty")
  else:
   return self.items[-1]

 def pop(self):
   if(self.is_empty()):
    print("Stack is empty")
   else:
    return self.items.pop()

 def __str__(self):
  return str(self.items)


stack = stack()


stack.pop()
stack.top()
stack.push(10)
stack.push(20)
print(stack.top())
stack.pop()
stack.top()

print(stack)

