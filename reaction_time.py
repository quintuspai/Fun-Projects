import time

input("Press Enter to start")
start_time = time.time()
time.sleep(2)
input("Press Enter to stop")
end_time = time.time()
print("Reaction time is : {}".format(end_time-start_time))