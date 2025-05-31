






















def maxScore(cardPoints, k) :
        total=sum(cardPoints[:k])
        n=len(cardPoints)-1
        maxi=0
        j=0
        for i in range(k-1,-1,-1):
            total-=cardPoints[i]
            total+=cardPoints[n-j]
            j+=1
            maxi=max(maxi,total)
        return maxi



cardPoints=[100,40,17,9,73,75]
k =3
print(maxScore(cardPoints,k))