#!/usr/bin/python3
"""
Module
"""


def find_peak(list_of_integers):
	""" function that finds the peak nummber in a list """
	if not list_of_integers:
		return None
	else:
		peak_num = 0
		my_list = list_of_integers[:]
		for num in my_list:
			if num > peak_num:
				peak_num = num
		return peak_num
