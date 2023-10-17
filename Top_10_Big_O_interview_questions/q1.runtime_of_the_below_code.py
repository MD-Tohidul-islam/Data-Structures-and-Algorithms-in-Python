#  what is the runtime of the below code?
def foo(array):
    sum = 0  # Big_O = O(1)
    product = 1  # Big_O = O(1)
    for i in array:  # Big_O = O(n)
        sum+=i  # Big_O = O(1)
    for i in array:  # Big_O = O(n)
        product*=i  # Big_O = O(1)
    print(f'sum={sum} and product={product}') ## Big_O = O(1)

# total Big_O = O(1)+O(1)+O(n)+O(1)+O(n)+O(1)+O(1)=O(n)