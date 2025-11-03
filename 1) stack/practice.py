from stack_class import ArrayStack

def check(sentence):

    pair = {')':'(','}':'{',']':'['}
    left = set(pair.values())
    stack = ArrayStack(len(sentence))

    for ch in sentence:
        if ch in left:
            stack.push(ch)
        elif ch in pair:
            if stack.is_empty():
                return False
            if stack.peek() != pair[ch]:
                return False
            return stack.pop() 
        else:
            pass
        
    return stack.is_empty

def test_brackets():
    tests = [
        "{A[(i+1)]=0;}", #True
        "if ((x<0) && (y<3)", #False
        "while (n < 8)) {n++;}", #False
        "arr[(i+1])=0;", #False
    ]
    for t in tests:
        print(t, "->", check(t))

if __name__ == "__main__":
    test_brackets()   

    