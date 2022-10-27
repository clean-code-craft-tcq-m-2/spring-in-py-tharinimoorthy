
import math
import statistics

def min_max_avg(numbers):
  d = {}
  d["avg"] = statistics.mean(numbers)
  d["max"] = max(numbers)
  d["min"] = min(numbers)
  return d

def calculateStats(numbers):
  if len(numbers) != 0:
    result = result_min_max_avg(numbers)
  else:
    result = nan(numbers)
  return result

def result_min_max_avg(numbers): 
  if len(numbers) != 0:    
    goto = min_max_avg(numbers)
  else:  
    goto = nan(numbers)  
  return goto

def nan(numbers):
  numbers.append(float('NaN'))
  return min_max_avg(numbers)
