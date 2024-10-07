import time

my_time = int(input("what time are we counting down to (in seconds)?: "))

print(f"Count down from {time} seconds")


for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int((x / 60) % 60)
    hours = int((x / 3600) % 24)
    days = int(x / (24 * 60 * 60))
    print(f"{days}:{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's Up!.")

