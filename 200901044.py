#!/usr/bin/env python
# coding: utf-8

# In[ ]:



    


# In[ ]:





# In[32]:


#program begin
class py_solution:
    #defining functions
   def is_valid_parenthese(self, str1):
    
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}

        for parenthese in str1:
            #using loop and if/else
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0
    #returning stack

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
#using output for printing parenthesis
print(py_solution().is_valid_parenthese("()"))
#print("prog.finished")
#print("prog.end")
#Print("fin")


# In[ ]:




