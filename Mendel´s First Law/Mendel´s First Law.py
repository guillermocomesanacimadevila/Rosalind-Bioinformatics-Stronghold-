import os
f = open(os.path.expanduser("~/Desktop/rosalind_iprb.txt"))
f = f.read().replace("\n", "")

def prob_dominant(k,m,n):
    total = k+m+n
    prob_kk = (k/total) * ((k-1)/(total-1)) #total = 6 - (2/6) * (1/5)
    prob_km = (k/total) * (m/(total-1)) + (m/total)* (k/(total-1)) # (2/5) * (2/6) + (2/6) * (2/5)
    prob_kn = (k/total) * (n/(total-1)) + (n/total)* (k/(total-1)) # (2/6) * (2/5) + (2/6) * (2/5)
    prob_mm = (m/total) * ((m-1)/(total-1)) *0.75 # (2/5) * ((1/5)) * 3/4 or 0.75
    prob_mn = (m/total) * (n/(total-1))* 0.5 + (n/total)*(m/(total-1))*0.5 # (2/6) * (2/5) * 0.5 + (2/6) * (2/5) * 0.5
    total_prob_dom = prob_kk + prob_km + prob_kn+ prob_mm + prob_mn #Probability sum
    return total_prob_dom

print(prob_dominant(16, 20, 20))
print(prob_dominant(f[0], f[1], f[2]))