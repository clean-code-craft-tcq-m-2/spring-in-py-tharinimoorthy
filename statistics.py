
import math

def cal_min_max_avg(num_list):
  numbers_dict = {}
  numbers_dict["avg"] = sum(num_list)/len(num_list)
  numbers_dict["max"] = max(num_list)
  numbers_dict["min"] = min(num_list)
  return numbers_dict

def calculateStats(numbers):
  if len(numbers) != 0:
    report_ = report_min_max_avg(numbers)
  else:
    report_ = avg_is_nan_for_empty_input(numbers)
  return report_

def report_min_max_avg(numbers):
  # To remove float('nan') values
  clean_numbers = []
  for value in numbers:
    if not math.isnan(value): clean_numbers.append(value)
  
  if len(clean_numbers) != 0:
    # Getting the avg, max, min values
    numbers_dict_val = cal_min_max_avg(clean_numbers)
  else:
    # Getting empty list after cleaning nan values
    numbers_dict_val = avg_is_nan_for_empty_input(clean_numbers)
  
  return numbers_dict_val

def avg_is_nan_for_empty_input(numbers):
  numbers.append(float('NaN'))
  # Getting the avg, max, min values of nan data
  return cal_min_max_avg(numbers)
