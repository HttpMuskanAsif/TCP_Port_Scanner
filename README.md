# TCP Port Scanner

## Project Overview

This project is a Python-based TCP Port Scanner that scans a target host to identify open TCP ports. It uses Python's built-in socket library to establish TCP connections and determine whether specific ports are open or closed.
The project was developed to strengthen my understanding of networking, socket programming, TCP communication, and basic cybersecurity concepts.

---

## Features

- Scan a target IP address or hostname
- Scan a custom range of TCP ports
- Detect open and closed ports
- Handle connection timeouts
- Save scan results to a text file
- Simple and beginner-friendly command-line interface
- Error handling for invalid input and network issues

---

## Technologies Used

- Python 3
- Socket Module
- VS Code
- Git
- GitHub

---

## Project Structure

```
TCP-Port-Scanner/
│── scanner.py
│── results.txt
│── README.md
```

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/HttpMuskanAsif/TCP-Port-Scanner.git
```

2. Open the project folder

3. Run the program

```bash
python scanner.py
```

4. Enter:
- Target IP Address
- Starting Port
- Ending Port

5. View the scan results in the terminal and in **results.txt**.

---

## Example

Input

```
Target IP: scanme.nmap.org
Start Port: 20
End Port: 100
```

Output

```
Open Port: 22
Open Port: 80
Open Port: 53

Results saved in results.txt
```

---

## Learning Outcomes

Through this project, I learned:

- TCP Networking Basics
- Socket Programming in Python
- Port Scanning Fundamentals
- File Handling
- Error Handling
- Git & GitHub Workflow

---

## Future Improvements

- Multi-threaded scanning
- Service and Version Detection
- Banner Grabbing
- Command-line Arguments
- Scan Progress Bar
- Export Results to CSV
- GUI Version using Tkinter

---

## Disclaimer

This project is intended for educational purposes only. Scan only systems that you own or have explicit permission to test.

---

## Author

**Muskan Asif**

Cybersecurity Student

