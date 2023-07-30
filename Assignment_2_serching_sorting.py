# Q1. Implement Binary Search

def bs(x,value):
    l = 0
    h = len(x)-1
    m = 0
    while l<= h:
        m = (l+h)//2
        mid_value = x[m]

        if mid_value == value:
            return m
        if mid_value < value:
            l = m+1
        else:
            h = m-1
    return "Value not found"

x = [1,4,2,6,3,23,15,11,10,8,7] 
x.sort()
print("Sorted of x is:",x)
print("position of value is: ",bs(x,15))
#-------------------------------------------------------------------------------------------------

# Q2. Implement Quick Sort

def quicksort(x):
    if len(x) <= 1:
        return(x)
    else:
        p = x[0]
        l = [i for i in x[1:] if i < p]
        r = [i for i in x[1:] if i >= p]
        return quicksort(l) + [p] + quicksort(r)
    
arr = [4,3,2,1,2,5,6,74,4]
sorted_array = quicksort(arr)
print(sorted_array)

#--------------------------------------------------------------------------------------------------

# Q3. Implement Merge Sort--

def marge(x,l,m,r):
    n1 = m-l+1
    n2 = r-m

    L = []
    R = []
    print(n1)

    for i in range(0,n1):
        L.append(x[l+i])

    for j in range(0,n2):
        R.append(x[m+1+j])

    i = 0 # for l side
    j = 0 # for r side
    k = l # for merged one

    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            x[k] = L[i]
            i += 1
        else :
            x[k] = R[j]
            j += 1
        k+=1
    
    while i<n1:
        x[k] = L[i]
        i+=1
        k+=1

    while j<n2:
        x[k] = R[j]
        j+=1
        k+=1

def margesort(x,l,r):
    if l<r:
        m= l+(r-l)//2
        margesort(x,l,m)
        margesort(x,m+1,r)
        marge(x,l,m,r)

arr = [12,34,2,98,46,19,45,54,32,74,15,34]
margesort(arr,0,len(arr)-1)
print(arr)        
#-----------------------------------------------------------------------------------------

#Q4. implement insertion sort--

def insertionsort(x):
    l = len(x)
    if l<=1:
        return
    for i in range(1,l):
        n = x[i]
        j = i-1
        while j>=0 and n < x[j]:
            x[j+1] = x[j]
            j=j-1
        x[j+1]=n

arr = [12,34,2,98,46,19,45,54,32,74,15,34]
insertionsort(arr)
print('insertion sort : ',arr)
#----------------------------------------------------------------------------------------------
#Q5. Write a program to sort list of strings (similar to that of dictionary)


list1 = ["Hi","Welcome","To","Flight"]
for i in sorted(list1):
        print(i)



def sort(x):
    if len(x) <= 1:
        return(x)
    else:
        p = x[0]
        l = [i for i in x[1:] if i < p]
        r = [i for i in x[1:] if i >= p]
        return sort(l) + [p] + sort(r)
    
arr = ['the','apple','is','good']
sorted_array = sort(arr)
print(sorted_array)