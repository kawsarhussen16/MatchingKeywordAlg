# Basic Naive Algorithm
import time
start_time = time.time()
def BasicNaive(keyword, url): 
    M = len(keyword) 
    N = len(url) 
  
    # A loop to slide ulr[] one by one 
    for i in range(N - M + 1): 
        j = 0
          
        # For current index i, check  
        # for pattern match 
        for j in range(0, M): 
            if (url[i + j] != keyword[j]): 
                break
  
        if (j == M - 1):  
            print("Keyword match at index ", i) 
  
url = "targetthisstringtargett"
keyword = "target"
BasicNaive(keyword, url) 
end_time = time.time()
print (f"runtime: {end_time - start_time} seconds")