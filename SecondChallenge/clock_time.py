from itertools import permutations

def solution(A, B, C, D):
    # Generate all possible permutations of the four digits
    perm = permutations([A, B, C, D])
    valid_times = set()
    
    for p in perm:
        h1, h2, m1, m2 = p
        
        hours = h1 * 10 + h2
        minutes = m1 * 10 + m2
        
        # Check if the time is valid
        if 0 <= hours < 24 and 0 <= minutes < 60:
            valid_times.add((hours, minutes))  # avoids duplicates
    
    return len(valid_times) # Return the number of unique valid times

# Examples
if __name__ == "__main__":
    print("Example 1:", solution(1, 8, 3, 2))  # Output: 6
    print("Example 2:", solution(2, 3, 3, 2))  # Output: 3
    print("Example 3:", solution(6, 2, 4, 7))  # Output: 0

