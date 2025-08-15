def canplace(stalls,m,k):
    cow_count = 1
    last_position = stalls[0]
    for i in stalls[1:]:
        if i - last_position >= m:
            cow_count += 1
            last_position = i
            if cow_count == k:
                return True
    return False
 
