def apply_gravity_unique(box):
    """
    Applies gravity (stones fall to the bottom) using a unique zip-based approach.
    1. Transpose the box (to work column-by-column as rows).
    2. Process each new row (old column): sort it so '*' is at the end.
    3. Transpose back.
    """
    # 1. Transpose the box: columns become temporary rows (list of tuples)
    # The '*' and '.' in each tuple now represent a column from top to bottom.
    transposed = list(zip(*box))
    
    # 2. Process each temporary row (old column):
    # Sort the column so '.' comes before '*' (effectively pushing '*' to the bottom).
    # Since '.' < '*', simple sorting works!
    gravity_applied = [sorted(col) for col in transposed]
    
    # 3. Transpose back to the correct M x N box format.
    final_box = [list(row) for row in zip(*gravity_applied)]
    
    return final_box

def rotate_right_unique(box):
    """
    Rotates 90 degrees right: Transpose then reverse each row.
    """
    # Use map to reverse each row (list(row)[::-1]) then use zip for transpose.
    # The logic is: rotate = transpose + reverse rows
    return [list(row)[::-1] for row in zip(*box)]

def rotate_left_unique(box):
    """
    Rotates 90 degrees left: Reverse rows then transpose.
    """
    # The logic is: rotate = reverse rows + transpose
    return [list(col) for col in zip(*box[::-1])]


def solve_stone_box_rotation_unique():
    """
    Main function to process input and execute unique rotation/gravity logic.
    """
    try:
        # Read M and N
        M, N = map(int, input().split())
        
        # Read the initial box configuration (convert to list of lists of strings)
        box = []
        for _ in range(M):
            box.append(input().split())
            
        # Apply gravity to the initial configuration first
        current_box = apply_gravity_unique(box)
        
        # Read K (number of instructions)
        K = int(input())
        
        # Read instructions
        instructions = [input().strip().lower() for _ in range(K)]
            
        # Process rotations
        for instruction in instructions:
            if instruction == 'right':
                current_box = rotate_right_unique(current_box)
            elif instruction == 'left':
                current_box = rotate_left_unique(current_box)
            
            # Apply gravity after every rotation
            current_box = apply_gravity_unique(current_box)
            
        # Output the final configuration
        for row in current_box:
            # Print the row with elements space-separated
            print(' '.join(row))

    except Exception:
        # Simple error handling
        pass

# Execute the unique solution
solve_stone_box_rotation_unique()