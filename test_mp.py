import multiprocessing as mp
import DroneModels as dm
import time
if __name__=='__main__':
    q = mp.Queue()          # Defines our Queue
    drone = dm.CX10WD()     # Drone object

    command_process = mp.Process(target=drone.PerformAction, args=(q,))     # Control process Spawn
    drone.connect()
    command_process.start()                       # Start the process
    print("Test process started...")


    # Python command: [r, p, t, y, m]
    # r = roll [0,255]
    # p = pitch [0, 255]
    # t = throttle [0, 255]
    # y = yaw [0,255]
    # m = flight mode:
    #       0 = Do nothing
    #       1 = TakeOff
    #       2 = Land

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
            q.put([127, 127, 0, 127, 2])
            print("Done")

        time.sleep(0.1)

    command_process.join()          # Kill the process
    print("Test process ended, Disconnecting.")
    drone.disconnect()
