import multiprocessing as mp
import DroneModels as dm

drone = dm.CX10WD()

command_process = mp.Process(target=drone.testCommandProcess)
drone.connect()
command_process.start()
print("Test process started...")
command_process.join()
print("Test process ended, Disconnecting.")
drone.disconnect()