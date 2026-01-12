# system-Health-checker
A script that automates the  health checking of cpu and Ram and disk
Project title:
SYSTEM HEALTH CHECKER

# Description:
Sometimes the computers gets slow and even unresponsive, and unfortunately the problem to that may not be known.
This script automates the manual checking of the cpu and ram usages>
It outputs the current uage of the cpu nd ram so that one can know if the computer is experiencing some bottle necks.
If the cpu and ramusage exceed a certain threshold, then  it could lead to the unresponsiveness of the computer.
This script enables one to identify with ease and so take the necessary actions which may include closing some applications, adding some ram if possible etc

# Tech stack
Python

# Prerequisite:
Python 3.14

# Repository structure
system-health-checker/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── system_health/
│   │   ├── __init__.py
│   │   ├── cpu.py
│   │   ├── memory.py
│   │   ├── disk.py
│   │   └── checker.py
│
├── tests/
│   ├── __init__.py
│   └── test_checker.py
│
├── logs/
│   └── app.log
│
└── .gitignore
   



