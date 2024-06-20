if __name__ == '__main__':
    x = int(input())  # Dimension along x-axis
    y = int(input())  # Dimension along y-axis
    z = int(input())  # Dimension along z-axis
    n = int(input())  # Sum constraint

    # Generate all possible coordinates using list comprehensions
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
    
    # Filter coordinates based on the sum constraint
    filtered_coordinates = [coord for coord in coordinates if sum(coord) != n]

    print(filtered_coordinates)
