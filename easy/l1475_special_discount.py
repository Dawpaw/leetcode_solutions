'''
The idea in this one is that the stack is made in an 
incrementing order, so you know that if the top element in the stack
is smaller than the one being checked, you can subtract the value being checked
to all the elements in the stack
'''

def finalPrices(prices: list[int]) -> list[int]:
    # Increasing monotone stack
    res = [p for p in prices]
    stack = []

    for i in range(len(prices)):
        while stack and prices[stack[-1]]>= prices[i]:
            j = stack.pop()
            res[j] -= prices[i]
        # Append the element to the stack
        stack.append(i)

    return res