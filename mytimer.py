#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  22 09:11:05 2018

@author: michaelrossi
"""
from datetime import timedelta
from time import sleep
import numpy as np


def mytimer():
    print("Set your timer: ")
    timer = input()
    convert_timer = float(timer)
    convert_int = timedelta(minutes=convert_timer)
    convert_seconds = convert_int.seconds
    seconds_int = float(convert_seconds)
    try:

        for _ in np.arange(seconds_int, 0, -1):
            print("You have " + str(_) + " seconds left.")
            sleep(1)

        print("Your timer is now complete!")

    except KeyboardInterrupt:
        print("Okay, you've decided to stop your timer. Goodbye!")


mytimer()
