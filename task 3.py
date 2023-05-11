#TASK 3
def average_score():
    scores=[50,10,80]
    scores.sort()
    lowest=min(scores)
    highest=max(scores)
    a=0
    for i in range (len (scores)):
        a=a+scores[i]
    b=len(scores)
    c=a/b
    print ("lowest:",lowest)
    print ("highest:",highest)
    print ("average:","% .2f"%(c))
average_score()

    
    
