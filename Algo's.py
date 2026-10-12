#........................... Analysis of algorithms................



# Example: One Loop
# Problem: Does array A contain the integer t? Given A (array of length n) and t(an integer)
# Algorithm 1



for i=1 to n
    if A[i] == t
        return True
    return False





# Example: Two Loop
# Problem: Given A;B (arrays of length n) and t(an integer) [Does array A or B contain t]



# Algorithm 2
for i=1 to n
    if A[i] == t
        return True

for i=1 to n
    if A[i] == t
        return True
    return  False




# Example: Two Nested Loop



# Problem: Given A;B (arrays of length n) and t(an integer). [Does A or B contain t?]
# Algorithm 3


for i=1 to n
    for j=1 to n
       if A[i]==B[j]
           return True
    return False




# Example: Two Nested Loop(II)



# Problem: Given A have duplicate entries? Given arrays A of length n.
# # Algorithm 4


for i=1 to n
    for j=i+1 to n
       if A[i]==B[j]
           return True
    return False