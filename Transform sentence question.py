def transformSentence(sentence):
    ans = ""
    ans += sentence[0]
    
    for i in range(1,len(sentence)):
        if sentence[i-1] == " ":
            ans+=sentence[i]
        else:
            if sentence[i].lower()>sentence[i-1].lower():
                ans+=sentence[i].upper()
            elif sentence[i].lower()<sentence[i-1].lower():
                ans+=sentence[i].lower()
            else:
                ans+=sentence[i]
    
    return ans
