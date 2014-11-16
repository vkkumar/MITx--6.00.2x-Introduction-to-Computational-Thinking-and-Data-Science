# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 20:36:43 2014

@author: vkkumar
"""
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
            
    matches = 0

    for i in range(numTrials):
         trial = draw()
         if trial == 1:
             matches += 1
            
    return matches/float(numTrials)
    
def draw():
    '''
    Helper function
    r - red; g - green
    '''
    ballColors = ['r', 'r', 'r', 'g', 'g', 'g']
    ballSet = []
    
    for i in range(3):
        ball = random.choice(ballColors)
        ballSet.append(ball)
        ballColors.pop(ballColors.index(ball))

    if ballSet[0] == ballSet[1] == ballSet[2]:
        return 1
    else:
        return 0
        


        
        