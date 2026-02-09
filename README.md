# Operating Systems Algorithm Visualizer

A comprehensive collection of Operating Systems scheduling and memory management algorithms implemented for educational purposes. This repository contains implementations of disk scheduling, page replacement, and CPU scheduling algorithms with an interactive GUI visualizer.

## Table of Contents

- [About](#about)
- [Features](#features)
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
- [Authors](#authors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## About

This project was developed as part of the CCOPSYSL (Operating Systems) course. It provides visual and practical implementations of core operating system algorithms, helping students understand how these algorithms work in real-world scenarios.

The repository includes:
- A Python-based GUI application for visualizing disk scheduling and page replacement algorithms
- A Java console application for Round Robin CPU scheduling with detailed performance metrics

## Features

- Interactive GUI for algorithm visualization
- Support for multiple disk scheduling algorithms (FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK)
- Implementation of page replacement algorithms (FIFO, LRU, Optimal)
- Round Robin CPU scheduling with configurable time quantum
- Real-time calculation of waiting time and turnaround time
- Visual representation of algorithm execution
- Step-by-step algorithm demonstration
- Performance metrics and statistics

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
- Enter the initial head position
- Input the disk queue requests
- Select an algorithm (FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK)
- View the head movement visualization and total seek time

**Page Replacement Steps:**
- Specify the number of page frames
- Enter the length of the reference string
- Input the page reference sequence
- Choose an algorithm (FIFO, LRU, Optimal)
- Analyze page hits, faults, and replacement steps

### Round Robin CPU Scheduling

Compile and run the Java program:

```bash
javac RoundRobin_OdarveRenaire.java
java RoundRobin_OdarveRenaire
```

**Interactive Prompts:**
1. Enter the quantum time (time slice)
2. Specify the number of processes
3. For each process, input:
   - Arrival time
   - Burst time
4. View the calculated waiting time and turnaround time for each process

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
└── README.md                      # Project documentation
```

## Technologies Used

- **Python 3.x**: Primary language for GUI application
  - tkinter: GUI framework
  - matplotlib: Data visualization
  - numpy: Numerical computations
- **Java**: Implementation of Round Robin algorithm
- **Git**: Version control

## License

This project is developed for educational purposes as part of the CCOPSYSL course.

## Acknowledgments

This README template is inspired by examples from the [Awesome README](https://github.com/matiassingers/awesome-readme) repository by Matias Singers, which provides curated examples of high-quality README files. The structure follows best practices for clear documentation including project description, installation instructions, usage examples, and comprehensive feature lists.