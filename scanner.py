import socket

print("=" * 40)
print("      TCP PORT SCANNER")
print("=" * 40)

host = input("Enter Target IP Address: ")

start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))

print("\nScanning Target:", host)
print("-" * 40)

results = []

try:

    for port in range(start_port, end_port + 1):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(0.5)

        result = s.connect_ex((host, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            results.append(port)

        s.close()

except KeyboardInterrupt:
    print("\nScan Stopped")

except socket.gaierror:
    print("Hostname could not be resolved.")

except Exception as e:
    print("Error:", e)

print("\nScan Completed")

with open("results.txt", "w") as file:

    file.write("Open Ports\n")
    file.write("=================\n")

    for port in results:
        file.write(f"{port}\n")

print("Results saved in results.txt")