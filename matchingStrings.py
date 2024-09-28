def matchingStrings(stringList, queries):
    # Write your code here
    results=[]
    stringMap={}
    for s in stringList:
        if s in stringMap:
            stringMap[s] += 1
        else:
            stringMap[s] = 1
    
    for q in queries:
        if q in stringMap:
            results.append(stringMap[q])
        else:
            results.append(0)               
        
    return results