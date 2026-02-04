# Totally forgot how to this so now I'm 
# checking online solutions

def generate_parenthesis(n:int) -> list[str]:
    stack = []
    result = []

    def backtracking(open_n, close_n):
        if(open_n == close_n == n):
            result.append("".join(stack))
            return

        if(open_n < n):
            stack.append("(")
            backtracking(open_n + 1, close_n)
            stack.pop()
        
        if(close_n < open_n):
            stack.append(")")
            backtracking(open_n, close_n + 1)
            stack.pop()
    
    backtracking(0, 0)
    return result





if __name__ == "__main__":
    res = generate_parenthesis(3)
    print(res)