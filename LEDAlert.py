# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:02:42 2022

@author: TRO1COB
"""

class LEDAlert:

    def __init__(self):
        self.led_check = False

    # @property
    def ledGlows(self, val, max_th):
        if val > max_th:
            self.led_check = True
            print("LED : RED!!!")
        else:
            print("LED : GREEN")
        return self.led_check