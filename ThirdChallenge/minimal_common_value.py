def solution(A, B):
    # Convert list A to a set for faster lookup
    set_a = set(A)

    # Initialize the minimal value to infinity
    min_value = float('inf')

    # Iterate over list B to find the minimal common value
    for value in B:
        if value in set_a and value < min_value:
            min_value = value

    # Return the minimal value if found, else return -1
    return min_value if min_value != float('inf') else -1

# Example usage
A = [1, 3, 2, 1]
B = [4, 2, 5, 3, 2]
result = solution(A, B)
print(f"Minimal common value: {result}")  # Expected output: 2
