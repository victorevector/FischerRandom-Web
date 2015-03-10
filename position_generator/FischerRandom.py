import random 
from copy import deepcopy
from copy import copy

def fischerize():
    pieces = ['r1','k1','b1','Q','K','b2','k2','r2']
    new_arrangement = []
    cycles = range(0,8)

    for cycle in cycles:
        random_piece = random.choice(pieces)
        new_arrangement.append(random_piece)
        pieces.remove(random_piece)

    return new_arrangement

def fulfills_criteria(fischer_arrangement):
    king_idx = fischer_arrangement.index('K')
    rook1_idx = fischer_arrangement.index('r1')
    rook2_idx = fischer_arrangement.index('r2')
    bishop1_idx = fischer_arrangement.index('b1')
    bishop2_idx = fischer_arrangement.index('b2')
    king_rook1_placement = rook1_idx < king_idx
    king_rook2_placement = king_idx < rook2_idx
    bishop1_placement = bishop1_idx % 2
    bishop2_placement = bishop2_idx % 2

    return (king_rook1_placement and king_rook2_placement and (bishop1_placement != bishop2_placement))

def htmlize(fischer_arrangement):
    white = deepcopy(fischer_arrangement)
    white[white.index('r1')] = '&#9814;'
    white[white.index('r2')] = '&#9814;'
    white[white.index('k1')] = '&#9816;'
    white[white.index('k2')] = '&#9816;'
    white[white.index('b1')] = '&#9815;'
    white[white.index('b2')] = '&#9815;'
    white[white.index('K')] = '&#9812;'
    white[white.index('Q')] = '&#9813;'

    black = deepcopy(fischer_arrangement)
    black[black.index('r1')] = '&#9814;'
    black[black.index('r2')] = '&#9814;'
    black[black.index('k1')] = '&#9816;'
    black[black.index('k2')] = '&#9816;'
    black[black.index('b1')] = '&#9815;'
    black[black.index('b2')] = '&#9815;'
    black[black.index('K')] = '&#9812;'
    black[black.index('Q')] = '&#9813;'

    return white, black

