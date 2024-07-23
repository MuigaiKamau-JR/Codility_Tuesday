def solution(R, V):
    # Initial balances for banks A and B
    balance_A = 0
    balance_B = 0
    
    # Track minimum balances needed
    min_balance_A = 0
    min_balance_B = 0
    
    # Iterate over each transfer
    for i in range(len(R)):
        if R[i] == 'A':
            # Transfer to bank A
            balance_B -= V[i]
            balance_A += V[i]
        else:
            # Transfer to bank B
            balance_A -= V[i]
            balance_B += V[i]
        
        # Track the minimum required balance to avoid going negative
        min_balance_A = min(min_balance_A, balance_A)
        min_balance_B = min(min_balance_B, balance_B)
    
    # Prepare results
    return [-min_balance_A, -min_balance_B]

# Example usage
if __name__ == "__main__":
    R1 = "BAABA"
    V1 = [2, 4, 1, 1, 2]
    print("Example 1:", solution(R1, V1))  # Output: [2, 4]

    R2 = "ABAB"
    V2 = [10, 5, 10, 15]
    print("Example 2:", solution(R2, V2))  # Output: [0, 15]

    R3 = "B"
    V3 = [100]
    print("Example 3:", solution(R3, V3))  # Output: [100, 0]
