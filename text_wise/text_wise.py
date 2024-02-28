def reverse_string(string):
    helper(0, len(string) - 1, string)
    return string

def helper(l, r, string):
    if l >= r: return
    string[l], string[r] = string[r], string[l]
    return helper(l + 1, r - 1, string)
        
print(reverse_string(['A','B','C','D']))