# 1

#code_list=[1234567890,1235451256,1238737689,1230984509,1230087362,1236547315,1239513856]
#phone_list=[380631234456,380739876512,380674563135,380507912345,380976542965,380665412381,380680674715]

'''code_list = "Enter code number to add to your code list or tape 'end' to end program: "

code_message = ""
lst_1=[]

while code_message != 'end':

    code_message = input(code_list)
    lst_1.append(code_message)

 #   print(lst_1)

phone_list = "Enter phone number to add to your phone list or tape 'end' to end the program: "

phone_message = ""
lst=[]

while phone_message != 'end':

    phone_message = input(phone_list)
    lst.append(phone_message)

 #   print(lst)

def partition (array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1
def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)

size=len(lst_1[:-1])
size_1=len(lst[:-1])
quicksort(lst_1,0,size-1)
quicksort(lst,0,size_1-1)
print("Original code list: ", lst_1[:-1])
print("Original phone list: ",lst[:-1])
print(list(enumerate(lst_1[:-1])))
for index,value in enumerate(lst_1[:-1]):
    print("user {} has code number: {}".format(index,value))
print(list(enumerate(lst[:-1])))
for index,value in enumerate(lst[:-1]):
    print("user {} has phone_number {}".format(index,value))'''



# 2

total = 10
name = input("Enter students name: ")
i = 0
lst=[]
while i < 10:
    n = float(input('"Enter students mark to add to his\her list: '))
    total = total - n
    i = i + 1
    lst.append(n)
    if n > 12:
        print("Sorry,mark rate is only from 1 to 12!")
        break

print("Your list: ", lst)
mark_dic={name:lst}
#mark_dic=dict.fromkeys(lst, f"{name}'s mark")
print(f"{name}'s rate: ",mark_dic)
medium_rate=sum(lst)/10
if medium_rate >= 10.7:
    print("Congrats! You can receive your scholarship!!!")
else:
    print("Sorry! You need to repass your exams")
print(f"{name}'s medium rate is",medium_rate)
#repass_dic=mark_dic[0].insert(int(input("Enter index position")),float(input("Enter new mark: ")))
#print(repass_dic)
# заплутався на етапі редагування списку оцінок, якщо їх розглядати у вигляді словника, як прописано у завданні

k=input("Enter 1 to sort from low to high mark or 2 to sort from high to low: ")
if (k == '1'):
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1


    def quicksort(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            quicksort(array, low, pi - 1)
            quicksort(array, pi + 1, high)
    size=len(lst)

    quicksort(lst, 0, size - 1)
    print("Sorted list: ", lst)
if (k == '2'):
    def quick_sort(s):
        if len(s) <= 1:
            return s
        elem = s[0]
        left = list(filter(lambda x: x < elem, s))
        center = [i for i in s if i == elem]
        right = list(filter(lambda x: x > elem, s))
        return quick_sort(right) + center + quick_sort(left)
    print(quick_sort(lst))

