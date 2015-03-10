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
    return HttpResponse(html_positions)

