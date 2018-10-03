
# coding: utf-8

# In[ ]:

g={}
g[1]=[3,4]
g[2]=[1,4]
g[3]=[]
g[4]=[3]


# In[5]:

g


# In[6]:

g[1]


# In[7]:

n = int(input('Enter the node: '))


# In[11]:

ind=0
for k in g.keys():
    if n in g[k]:
        ind+=1
        
print(ind)


# In[12]:

print(len(g[n]))


# In[19]:

stack = []
def push(s,e):
    if e in s: return
    s.insert(0,e)
  

def pop(s):
    if(len(s)==0):
        return null
    else:
        return s.pop(0)
    
def empty(s):
    return len(s)==0


# In[25]:

push(stack,1)


# In[26]:

while empty(stack)==False:
    e=pop(stack)
    print(e)
    for k in g[e]:
        push (stack,k)

