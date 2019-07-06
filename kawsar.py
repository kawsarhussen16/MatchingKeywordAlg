# KMP Algorithm 
import time

def KMPurlMatch(keyword, url): 
    Key = len(keyword) 
    Url = len(url) 
  
    # create lps[] that will hold the longest prefix suffix  
    # values for keyword 
    lps = [0]*Key 
    j = 0 # index for keyword[] 
  
    # Preprocess the keyword (calculate lps[] array) 
    calculateLPSArray(keyword, Key, lps) 
  
    i = 0 # index for url[] 
    while i < Url: 
        if keyword[j] == url[i]: 
            i += 1
            j += 1
  
        if j == Key: 
            print("Keyword found at index " + str(i-j))
            j = lps[j-1] 
  
        # mismatch after j matches 
        elif i < Url and keyword[j] != url[i]: 
            # Do not match lps[0..lps[j-1]] characters, 
            # they will match anyway 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
  
def calculateLPSArray(keyword, Key, lps): 
    len = 0 # length of the previous longest prefix suffix 
  
    lps[0] # lps[0] is always 0 
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < Key: 
        if keyword[i]== keyword[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            if len != 0: 
                len = lps[len-1] 
  
                # do not increment i here 
            else: 
                lps[i] = 0
                i += 1
  

url = "targetthisstringtargett"
keyword = "target"
KMPurlMatch(keyword, url)
