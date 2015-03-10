from django.shortcuts import render
from FischerRandom import fischerize
from FischerRandom import fulfills_criteria
from FischerRandom import htmlize
from django.http import HttpResponse

def position_generator(request):
    while True:
        positions = fischerize()
        if fulfills_criteria(positions):
            break

    html_positions  = htmlize(positions)
    white = html_positions[0]
    black  = html_positions[1]

    context_dict={}
    for idx, piece in enumerate(white):
        context_dict['w'+str(idx)] = piece
    for idx, piece in enumerate(black):
        context_dict['b'+str(idx)] = piece

    return render(request, 'position_generator/chess_board.html', context_dict)
