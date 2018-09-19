
# coding: utf-8

# In[10]:

for i in range(1,101):
    print(i)


# In[22]:

year = int(input("Enter year in a number :"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("the year is a leap year")
        else:
            print("the year is not a leap year")

    else:
            print("this year is a leap year")
else:
        print("the year is not a leap year")


# In[23]:

name = "Noman islam"
s = name[0:10:3]
print(s)


# In[24]:

name = "Noman islam"
s = name[::-1]
print(s)


# In[25]:

name = "Noman islam 1 2 3"
countDigit = 0;
countAlpha = 0;
for i in name:
    if(i.isalpha()):
        print(i)
        countAlpha += 1;
    elif(i.isdigit()):
        print(i)
        countDigit += 1;

print("total alpha ",countAlpha)
print("total digits", countDigit)


# In[ ]:



