mydict={}
list1=[]
i=1
n=int(input("Enter how many terms: "))
while(i<=n):
    key_name=int(input("Enter key: "))
    list1.append(key_name)
    i+=1

for y in list1:
    print("Enter value for",y)
    mydict[y]=input()

print("The dictionary you enterd is: ",mydict)

print("The sorted list is: ")

list1.sort()
for z in list1:
    print("(" ,z, "," ,mydict[z], ")" ,end=",")
    
#sorting keys

print("\nSorted keys: ",sorted(mydict))

#sorting values

print("\nSorted values: ")
for w in sorted(mydict,key=mydict.get):
    print("(" ,w, "," ,mydict[w], ")" ,end=",")
