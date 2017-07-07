#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 18:00:23 2017

@author: Victor

Simulation based on this Decision Science Post:
http://www.decisionsciencenews.com/2017/06/19/counterintuitive-problem-everyone-room-keeps-giving-dollars-random-others-youll-never-guess-happens-next/
"""

import numpy as np

def RunSim(numIt, numPlayers=100, initAmount=100):
    initWealth = np.ones(numPlayers)*initAmount
    results = np.zeros([numIt+1, initWealth.size])
    results[0,:] = initWealth
    for i in xrange(numIt):
        results[i+1,:] = RedistWealth(results[i,:], 1./initAmount)
    
    return results

def RedistWealth(wealth, frac):
    # amount of wealth each person loses
    amount = wealth.mean() * frac
    amount = np.minimum(amount, wealth) # no negative wealth
    newWealth = wealth - amount
    
    # determine which person receives that amount
    target = np.int32(np.floor(np.random.random(wealth.size)*wealth.size))
    for i in xrange(wealth.size):
        newWealth[target[i]] += amount[i]
    
    return newWealth