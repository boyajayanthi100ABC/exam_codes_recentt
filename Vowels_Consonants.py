s=input()
l=list(s)
vowel=["a","e","i","o","u"]

count_v=0
count_c=0

for i in range(0,len(l)-1):
    if (l[i] in vowel and l[i+1] in vowel):
        count_v=count_v+1
        
    if((l[i] not in vowel) and (l[i+1] not in vowel)):
        count_c=count_c+1
        
print("Consonants-"+str(count_c))   
print("Vowels-"+str(count_v))