


# arr={ 1:[2,4], 2:[1,3,5,8], 3:[2,4,9,10], 4:[1,3], 5:[2,6,7], 6:[5], 7:[5,8],8:[2,7],9:[3],10:[3] }
arr={
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

def dfs(arr,vertex):
    dfs=[]
    stack=[]
    
    stack.append(vertex)
    while len(stack)!=0:
        top=stack.pop()
        if top not in dfs:
            dfs.append(top)
        
        for i in arr[top]:
            if i  in dfs:
                continue
            stack.append(top)
            stack.append(i)
            break
            
 



    return dfs

print(dfs(arr,'A'))
