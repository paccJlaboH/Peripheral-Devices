import psutil
import platform

print(f"Система: {platform.system()} {platform.release()}")


partitions = psutil.disk_partitions()

for partition in partitions:
    if platform.system() == "Linux" and ("loop" in partition.device or "tmpfs" in partition.device):
        continue
        
    print(f"\nПристрій: {partition.device}")
    print(f"  Точка монтування: {partition.mountpoint}")
    
    try:
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"  Всього (bytes): {usage.total}")
        print(f"  Використано (bytes): {usage.used}")
        print(f"  Вільно (bytes): {usage.free}")
        print(f"  Відсоток: {usage.percent}%")
    except PermissionError:
        print("  Доступ обмежено")

io = psutil.disk_io_counters()
print(f"\nЗагальна активність читання: {io.read_bytes} bytes")
print(f"Загальна активність запису: {io.write_bytes} bytes")
