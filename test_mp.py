import multiprocessing as mp
import DroneModels as dm
import time

q = mp.Queue()
drone = dm.CX10WD()

command_process = mp.Process(target=drone.PerformAction, args=(q,))
drone.connect()
command_process.start()
print("Test process started...")

for i in range(500):

    if i == 0:
        q.put([127, 127, 60, 127, 1])
        print("New Command")

    if i == 100:
        q.put([127, 127, 200, 127, 1])
        print("New Command")

    if i == 300:
        q.put([10, 10, 200, 127, 1])
        print("New Command")

    if i == 499:
        q.put([127, 127, 0, 127, 0])
        print("Done")

    time.sleep(0.1)



command_process.join()
print("Test process ended, Disconnecting.")
drone.disconnect()