"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Teagan Liddle
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)

state = "red"

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14

for t in range(1, maxtime + 1):
    if t <= states["red"]:
        state = "red"
    elif t < states["red"] + states["red_amber"]:
        state = "red_amber"
    elif t < states["red"] + states["red_amber"] + states["green"]:
        state = "green"
    else:
        state = "amber"
    print(f"Time {t:03} State {state}")
    
    
    


# while systime <= 3:
#         state = "red"
#         print(f"Time {systime:03} State {state}")
#         systime += 1
# else:
#     while systime >3 and systime <=6:
#         state = "red_amber"
#         print(f"Time {systime:03} State {state}")
#         systime += 1
# else:
#     while systime >6 and systime <=11:
#         state = "green"
#         print(f"Time {systime:03} State {state}")
#         systime += 1
# else:
#     while systime >11 and systime <=14:
#         state = "amber"
#         print(f"Time {systime:03} State {state}")
#         systime += 1
# systime = 0
