temperature = 35
cloudy = False
need_to_go_out = 60
wind_speed = 10
is_raining = True


result1 = temperature > 30 and not cloudy


result2 = need_to_go_out < 50 or wind_speed > 5


result3 = is_raining and cloudy


result4 = temperature < 40 and need_to_go_out < 70


result5 = wind_speed > 15 or is_raining and not cloudy


print(result1) 
print(result2)
print(result3)
print(result4)
print(result5)