# CCOPSYSL - Operating Systems Class Programs

Programs and implementations created during the Operating Systems (CCOPSYSL) course. This repository contains practical implementations of fundamental OS algorithms including disk scheduling, page replacement, and CPU scheduling, developed as coursework assignments.

## Table of Contents

- [About](#about)
- [Programs](#programs)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Disk Scheduling and Page Replacement GUI](#disk-scheduling-and-page-replacement-gui)
  - [Round Robin CPU Scheduling](#round-robin-cpu-scheduling)
- [Algorithms Implemented](#algorithms-implemented)
  - [Disk Scheduling](#disk-scheduling)
  - [Page Replacement](#page-replacement)
  - [CPU Scheduling](#cpu-scheduling)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Acknowledgments](#acknowledgments)

## About

This repository contains programming assignments and projects completed for the CCOPSYSL (Operating Systems) course. The programs demonstrate practical implementations of core operating system algorithms through interactive applications:

- **Python GUI Application**: Interactive visualizer for disk scheduling and page replacement algorithms
- **Java Console Application**: Round Robin CPU scheduler with performance analysis

These implementations were developed to demonstrate understanding of operating system concepts and algorithm behaviors in practical scenarios.

## Programs

### Python GUI Application
- **Interactive & Responsive Interface**: Dynamic window sizing adapts to screen resolution
- **Scrollable Input Areas**: Handle large input sequences with horizontal scrollbars
- **Disk Scheduling Algorithms**: FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK
- **Page Replacement Algorithms**: FIFO, LRU, Optimal
- **Visual Representation**: Real-time charts and graphs showing algorithm execution
- **Performance Metrics**: Total seek time, page faults, and hit rate calculations
- **Step-by-Step Display**: Detailed breakdown of each algorithm step
- **Input Validation**: Comprehensive error checking and user-friendly feedback
- **Cross-Platform**: Compatible with Windows, macOS, and Linux

### Java Console Application
- **Round Robin Scheduling**: CPU scheduling with configurable time quantum
- **Automatic Process Sorting**: Processes sorted by arrival time automatically
- **Input Validation**: Validates quantum time, process count, arrival/burst times
- **Performance Calculations**: Average waiting time and turnaround time
- **Detailed Output**: Process-by-process breakdown with timestamps

## Prerequisites

Before running this project, ensure you have the following installed:

**For Python GUI Application:**
- Python 3.x
- tkinter (usually comes pre-installed with Python)
- matplotlib
- numpy

**For Java Application:**
- Java Development Kit (JDK) 8 or higher

## Installation

### Clone the Repository

```bash
git clone https://github.com/rbodarve/CCOPSYSL.git
cd CCOPSYSL
```

### Python Dependencies

Install the required Python packages:

```bash
pip install matplotlib numpy
```

Note: tkinter is typically included with Python installations. If not available, install it using your system's package manager:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**macOS:**
```bash
brew install python-tk
```

### Java Setup

Ensure Java is installed and configured in your system PATH:

```bash
java --version
```

## Usage

### Disk Scheduling and Page Replacement GUI

Run the Python application:

```bash
python diskSchedPageAlgoOdarve.py
```

**GUI Features:**
1. Select between Disk Scheduling or Page Replacement algorithms
2. Enter the required inputs (queue size, reference string, etc.)
3. Choose the desired algorithm
4. View the visualization and results

**Disk Scheduling Steps:**
1. Enter the number of cylinders on the disk
2. Enter the initial head position
3. Specify the number of disk requests
4. Input each request value in the scrollable queue
5. Select an algorithm (FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK)
6. For SCAN/C-SCAN/LOOK/C-LOOK: Choose head movement direction
7. View the head movement visualization and total seek time

**Page Replacement Steps:**
1. Specify the number of page frames (memory capacity)
2. Enter the length of the reference string
3. Input each page number in the scrollable reference string
4. Choose an algorithm (FIFO, LRU, Optimal)
5. View detailed results including:
   - Step-by-step memory state
   - Page faults at each step
   - Total page faults
   - Hit rate percentage

### Round Robin CPU Scheduling

Compile and run the Java program:

```bash
javac RoundRobin_OdarveRenaire.java
java RoundRobin_OdarveRenaire
```

**Interactive Prompts:**
1. Enter the quantum time (time slice) - must be positive
2. Specify the number of processes - must be positive
3. For each process, input:
   - Arrival time - must be non-negative
   - Burst time - must be positive
4. The program automatically sorts processes by arrival time
5. View detailed results:
   - Process-by-process execution table
   - Wait time for each process
   - Turnaround time for each process
   - Average wait time
   - Average turnaround time

**Note:** The program includes comprehensive input validation and will display error messages for invalid inputs.

## Algorithms Implemented

### Disk Scheduling

- **FCFS (First-Come, First-Served)**: Services requests in the order they arrive
- **SSTF (Shortest Seek Time First)**: Selects the request with minimum seek time from current position
- **SCAN (Elevator Algorithm)**: Moves in one direction servicing requests until the end
- **C-SCAN (Circular SCAN)**: Similar to SCAN but returns to beginning after reaching the end
- **LOOK**: Like SCAN but reverses direction at the last request
- **C-LOOK**: Circular version of LOOK

### Page Replacement

- **FIFO (First-In, First-Out)**: Replaces the oldest page in memory
- **LRU (Least Recently Used)**: Replaces the page that hasn't been used for the longest time
- **Optimal**: Replaces the page that won't be used for the longest period (theoretical best)

### CPU Scheduling

- **Round Robin**: Cyclically assigns time slices to each process in the ready queue

## Project Structure

```
CCOPSYSL/
│
├── diskSchedPageAlgoOdarve.py    # Python GUI for disk scheduling and page replacement
├── RoundRobin_OdarveRenaire.java # Java implementation of Round Robin scheduling
├── .vscode/                       # VS Code workspace settings
├── .gitignore                     # Git ignore file for build artifacts
└── README.md                      # Project documentation
```

## Technologies Used

- **Python 3.x**: Primary language for GUI application
  - tkinter: GUI framework
  - matplotlib: Data visualization
  - numpy: Numerical computations
- **Java**: Implementation of Round Robin algorithm
- **Git**: Version control

## Acknowledgments

This README template is inspired by examples from the [Awesome README](https://github.com/matiassingers/awesome-readme) repository by Matias Singers, which provides curated examples of high-quality README files. The structure follows best practices for clear documentation including project description, installation instructions, usage examples, and comprehensive feature lists.