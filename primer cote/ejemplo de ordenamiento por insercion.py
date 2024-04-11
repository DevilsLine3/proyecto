def insercion(A):
    for i in range(1,len(A)):
        key=A[i]
        j=i-1
        while j>=0 and key < A[j]:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key
    print(A)
#Programa Principal
A=[6,5,3,1,8,7,2,4]
print("Ejemplo con números a ordernar")
print(A)
insercion(A)

def insercion(b):
    for i in range(1,len(b)):
        key=b[i]
        j=i-1
        while j>=0 and key < b[j]:
            b[j+1]=b[j]
            j-=1
        b[j+1]=key
    print(b)
print("\n")
print("Ejemplo con nombres a ordernar")
b=["juan","maria","pepito","laura","juliana","bernarda","carlos","david"]
print(b)
insercion(b)