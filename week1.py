"""
File: L01 Prepare Checkpoint
Author: Gab Yanqui
Date: 01/05/2023
Purpose: Calculate the high and low heart rate.
"""
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input('Enter your age: '))
maximum_heart_rate = 220 - age
heart_rate_range_low = maximum_heart_rate * 0.65
heart_rate_range_high = maximum_heart_rate * 0.85

print(f'To strengthen your heart, maintain your heart rate between {heart_rate_range_low:.0f} and {heart_rate_range_high:.0f} beats per minute.')