# str= input("Enter word :")
# countVowel = 0
# listVowel = []
# list=['a','e','i','o','u']
# for i in str:
#     if (i in list):
#         countVowel += 1
#         listVowel.append(i)
#
#
# print(listVowel)


str= input("Enter word : ")

vowels=['a','e','i','o','u']
d={'a':0,'e':0,'i':0,'o':0,'u':0}
for i in str:
    if i in vowels:
        d[i]+=1
print(d)
