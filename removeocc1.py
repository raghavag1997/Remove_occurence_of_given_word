#to remove occurence of word given by user
def removeoccurence(list1,occ,word):
    count=0
    for i in range(len(list1)):
        if word==list1[i] and count!=occ:
            count=count+1
        elif count==occ:
            break
    del list1[i]
    print(list1)
list1=[]
print("Enter no of elemets of list")
x=int(input())
print("Enter the elements")
for i in range(x):
    ele=input()
    list1.append(ele)
print("Enter the word which you want to delete")
word=input()
print("Enter the occ which you want to delete")
occ=int(input())
removeoccurence(list1,occ,word)