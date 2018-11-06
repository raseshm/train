#!/usr/bin/env python3

#A (100 to 90)
#B (89 to 80)
#C (79 to 70)
#D (69 to 60)
#F (59 and below)

print('Input number anywhere between 1 to 100 ')

degrees = float(input())
if degrees > 100:
  print('Invalid input')
elif degrees <= 100 and degrees >= 90:
  print('A')
elif degrees <= 89 and degrees >= 80:
  print('B')
elif degrees <= 79 and degrees >= 70:
  print('C')
elif degrees <= 69 and degrees >= 60:
  print('D')
elif degrees <= 59:
  print('F')
