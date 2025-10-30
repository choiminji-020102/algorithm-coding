import sys

input = sys.stdin.readline

N = int(input().strip())

stack = []
for i in range(N):
    command = input().strip()
    
    if 'push' in command:
        stack.append(command.split()[-1])
    elif command == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
            
        
        
    
        
    

