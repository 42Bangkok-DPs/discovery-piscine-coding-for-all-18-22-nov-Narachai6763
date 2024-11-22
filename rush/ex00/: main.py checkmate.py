def is_king_in_check(board):
    """
    Check if the king is in check on the given board.
    Returns True if king is in check, False otherwise.
    """
    # First validate board
    if not board or not isinstance(board, list):
        return False
    
    # Get board dimensions
    height = len(board)
    if height == 0:
        return False
    width = len(board[0])
    if width != height:  # Board must be square
        return False
    
    # Find king's position
    king_pos = None
    for i in range(height):
        if not isinstance(board[i], str) or len(board[i]) != width:
            return False
        for j in range(width):
            if board[i][j] == 'K':
                if king_pos:  # More than one king found
                    return False
                king_pos = (i, j)
    
    if not king_pos:  # No king found
        return False
    
    # Check all possible threats
    return (
        check_pawn_threat(board, king_pos) or
        check_rook_threat(board, king_pos) or
        check_bishop_threat(board, king_pos) or
        check_queen_threat(board, king_pos)
    )

def check_pawn_threat(board, king_pos):
    """Check if any pawn is threatening the king"""
    row, col = king_pos
    # Pawns attack diagonally from above
    for d_col in [-1, 1]:
        if row - 1 >= 0 and 0 <= col + d_col < len(board):
            if board[row-1][col+d_col] == 'P':
                return True
    return False

def check_direction(board, king_pos, delta_row, delta_col):
    """
    Check for threats in a specific direction.
    Returns True if a threat is found in that direction.
    """
    row, col = king_pos
    size = len(board)
    row += delta_row
    col += delta_col
    
    while 0 <= row < size and 0 <= col < size:
        piece = board[row][col]
        if piece != '.':  # Found a piece
            return piece  # Return the piece found
        row += delta_row
        col += delta_col
    return None

def check_rook_threat(board, king_pos):
    """Check if any rook or queen threatens the king horizontally or vertically"""
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    for d_row, d_col in directions:
        piece = check_direction(board, king_pos, d_row, d_col)
        if piece in ['R', 'Q']:  # Rook or Queen found
            return True
    return False

def check_bishop_threat(board, king_pos):
    """Check if any bishop or queen threatens the king diagonally"""
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Diagonals
    for d_row, d_col in directions:
        piece = check_direction(board, king_pos, d_row, d_col)
        if piece in ['B', 'Q']:  # Bishop or Queen found
            return True
    return False

def check_queen_threat(board, king_pos):
    """
    Queen's threats are already covered by rook and bishop checks
    This is included for completeness and clarity
    """
    return False  # Already checked in rook and bishop functions

def main():
    # Example usage
    test_boards = [
        [
            "........",
            "........",
            "........",
            "...Q.K..",
            "........",
            "........",
            "........",
            "........"
            
        ],
        
        
    ]
    
    for board in test_boards:
        result = is_king_in_check(board)
        print("Success" if result else "Fail")

if __name__ == "__main__":
    main()