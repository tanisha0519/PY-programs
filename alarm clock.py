import time
print("===== ALARM CLOCK =====")
alarm_time = input("Enter Alarm Time (HH:MM:SS): ")
print("Alarm set for", alarm_time)
while True:
    current_time = time.strftime("%H:%M:%S")
    print("Current Time:", current_time, end="\r")
    if current_time == alarm_time:
        print("\n\n⏰ WAKE UP! ALARM IS RINGING! ⏰")
        try:
            import winsound
            for i in range(5):
                winsound.Beep(1000, 1000)
        except ImportError:
            # For Linux/macOS
            for i in range(5):
                print("\a")
                time.sleep(1)
        break
    time.sleep(1)