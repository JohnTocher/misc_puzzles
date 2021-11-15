""" Rotating annular platfrom puzzle

    First attempt at modeling and analysing a puzzle from a game

"""

def setup_rings():
    """ Create the initial configuration 
    
        Ring 0 is the innermost platform and contains the (B)eginning Square
        Ring 1 is the first moving ring
        Ring 4 is the outermost moving ring
        Ring 5 contains the (T)arget square

        X is a square you can walk on
        . is a space that cannot be walked on
        ^ is a gateway to the next ring and moves with the current ring
    """

    rings = dict()

    rings[5] = "....T..........."
    rings[4] = "......^.XXX.X..."
    rings[3] = "....X...XX^....."
    rings[2] = "..^.....XXX....."
    rings[1] = "....XX^XX......."
    rings[0] = "........B......."

    return rings


def draw_puzzle(rings_to_draw):
    """ Draws the provided configuration """

    for ring_index in range(5,-1,-1):
        this_line = ""
        this_ring = rings_to_draw[ring_index]
        assert len(this_ring) == 16, f"Seem to have a bad ring at {ring_index}, length is {len(this_ring)}"
        for each_square in this_ring:
            this_line = f"{this_line}{each_square}"
        print(f"{ring_index} : {this_line}")


def turn_a_wheel(rings_now, wheel_to_move, direction_to_move):
    """ Rotates a wheel which moves two rings 

        For example wheel 4 turns both ring 1 and ring 4
    """

    wheel_moves = dict()
    wheel_moves[1] = (1, 2)
    wheel_moves[2] = (2, 3)
    wheel_moves[3] = (3, 4)
    wheel_moves[4] = (4, 1)

    for ring_index in wheel_moves[wheel_to_move]:

        print(f"Rotating ring {ring_index} {direction_to_move}")
        if direction_to_move == "CW": # Shifting to the right
            rings_now[ring_index] = f"{rings_now[ring_index][-1:]}{rings_now[ring_index][0:15]}"
        else:   # Shifting to the left
            rings_now[ring_index] = f"{rings_now[ring_index][1:]}{rings_now[ring_index][:1]}"

    return rings_now


def analyse_puzzle():
    """ The main part of the program """

    rings = setup_rings()   # Create and print the inital state for the rings
    print("Initial layout:")
    draw_puzzle(rings)

    # Some sample moves, defining the wheel to turn and direction in each case
    # Each wheel turns two rings
    some_moves = [ (1, "CW"), [2, "CCW"], (3, "CW")]

    move_count = 0
    for each_move in some_moves:
        move_count += 1
        rings = turn_a_wheel(rings, each_move[0], each_move[1])
        print(f"After move #{move_count} ({each_move}):")
        draw_puzzle(rings)


if __name__ == "__main__":
    analyse_puzzle()
