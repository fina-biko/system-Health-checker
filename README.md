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
   

METRICS USED

The most important metrics to capture and their meanings are:
# 1. CPU Utilization (psutil.cpu_percent) 
What it is: A percentage showing how much of the CPU's total capacity is being used.
What it means:
0%: The CPU is doing nothing (idle).
100%: The CPU is completely maxed out.
Important Tip: Always use an interval (e.g., psutil.cpu_percent(interval=1)). If you don't, the first call will often return 0.0, which is meaningless because it hasn't had time to measure a change. 
# 2. CPU Times (psutil.cpu_times) 
This breaks down the "work" into specific categories so you know why the CPU is busy: 
User: Time spent running your actual programs (e.g., Python scripts, browser).
System: Time the CPU spent doing "office work" for the computer (e.g., managing files, talking to hardware).
I/O Wait (Linux): Time the CPU spent sitting around waiting for a slow disk or network to finish a task. If this is high, your disk is the bottleneck, not the CPU.
Idle: Time the CPU spent doing absolutely nothing. 
# 3. CPU Statistics (psutil.cpu_stats)
These measure how "noisy" or "stressed" the system is: 
Context Switches: How many times the CPU had to stop one task to start another. A very high number (thousands per second) can mean your system is "jittery" because too many programs are fighting for attention.
Interrupts: How many times hardware (like a keyboard or mouse) asked the CPU for an immediate response. 
# 4. Hardware Details
CPU Count (psutil.cpu_count): Tells you how many cores your machine has. Monitoring "Per CPU" (using percpu=True in other functions) helps you see if one core is doing all the work while others sit idle.
CPU Frequency (psutil.cpu_freq): Tells you the current speed in MHz. If this is very low, your computer might be "throttling" (slowing down) to save power or stay cool. 








cpu_usage = psutil.cpu_times()
Then printing 
say print(cpu_usage)
it gives:
scputimes(
    user=43011.17187499999,
    system=30398.28125,
    idle=192504.4375,
    interrupt=1549.609375,
    dpc=9288.515625
)

so scputimes is the class
it means there must be a helper function whose job was to initialsie the class ie
def helper():
   return scputimes(user=,dpc=,,,)

then somewhere we have the class defined
class scputimes:
   def __init__(self,user,dpc,):
      return  a result


 # Why Python prints it like that

                When you do:

                print(cpu_usage)


Python shows you:

            scputimes(user=..., system=..., idle=...)


This is just:

A string representation

Meant for humans

Showing: “this object is an instance of scputimes and these are its fields”


if an aobject is a named tuple ,If an object is a named tuple, you can convert all its fields into a dictionary using _asdict()