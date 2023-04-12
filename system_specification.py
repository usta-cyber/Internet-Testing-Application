import platform
import psutil

# Get the total number of CPU cores
cores = psutil.cpu_count(logical=False)

print("Operating System: ", platform.system())
print("OS Release: ", platform.release())
print("Processor Architecture: ", platform.machine())
print("Python Version: ", platform.python_version())
print("RAM (bytes): ", psutil.virtual_memory().total)
print("CPU: ", cores, "x", psutil.cpu_freq().max, "MHz")
print("Disk Usage: ")
for part in psutil.disk_partitions():
    print("  ", part.device, " - ", part.mountpoint)
    print("     Total: ", psutil.disk_usage(part.mountpoint).total, "bytes")
    print("     Used: ", psutil.disk_usage(part.mountpoint).used, "bytes")
    print("     Free: ", psutil.disk_usage(part.mountpoint).free, "bytes")
