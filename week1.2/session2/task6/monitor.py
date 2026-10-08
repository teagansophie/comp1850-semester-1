# Week 1.2, Session 2: Task 6
# Factory machine monitoring system

machine_temp = int(input("Enter the temperature of the machines in Celsius: "))
machine_pressure = int(input("Enter the pressure of the machines in PSI: "))
machine_status = int(input("Enter the status of the machine. 1 for operational, 0 for stopped: "))


# Checking temperature 
if machine_temp > 80:
    print("Temperature is too high. Recommend shutting down the machine.")
elif machine_temp<=80 and machine_temp>=50:
    print("Temperature is within safe limits")
elif machine_temp < 50:
    print("Temperature is too low. No action needed.")

# Checking pressure
if machine_pressure > 100:
    print("Pressure is too high. Recommend maintenance.")
elif machine_pressure<=100 and machine_pressure>=70:
    print("Pressure is stable")
elif machine_pressure < 70:
    print("Pressure is low but the system is operating normally.")

# Checking machine status
if machine_status == 1 and machine_temp>80 and machine_pressure>100:
    print("Machine is running in unsafe conditions.Recommend shutting down the system.")

elif machine_status == 1 and machine_temp<=80 and machine_temp>=50 and machine_pressure<=100 and machine_pressure>=70:
    print("Machine is running normally")

elif machine_status == 0:
    print("Machine is stopped. No immediate action needed.")

machine_file = open("machine_status.txt", "w")
machine_file.write(f"Machine Temperature: {machine_temp}C")
machine_file.write(f"Machine Pressure: {machine_pressure} PSI")
if machine_status == 1:
    machine_file.write("Machine Status: Operational")
else:
    machine_file.write("Machine Status: Stopped")

action = input("Enter any action taken (if any): ")
machine_file.write(f"Action Taken: {action}")
time = input("Enter the time of the action taken (if any): ")
machine_file.write(f"Time of Action: {time}")
machine_file.close()