"""Student Id = 20CE063
    Student name = Preet Padariya"""
#Number of Occurance of Words

# GITHUB-LINK : https://github.com/preetpadariya/PIP_Prac6.git

t = int(input())

dict = {}
for i in range(t):
    str = input()
    if str in dict:
        dict[str] +=1
    else:
        dict[str] = 1
print(len(dict))
for i in dict.values():
    print(i ,end=' ')
