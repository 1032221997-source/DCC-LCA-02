# Bully Election Algorithm 

A C implementation of the Bully Election Algorithm, a classical method in distributed systems for electing a coordinator or leader from a group of processes.Here the coordinator is the main orchestrator process that controls the resource allocation and other tasks.

## Objective
The goal is to ensure that the process with the highest ID (the "strongest" or "bully") is consistently chosen as the coordinator, even if the current coordinator fails.

## Description
In this implementation:
- Each process has a unique ID (0 to `n-1`).
- Processes can be in either an **Active (1)** or **Failed (0)** state.
- When an active process detects that the coordinator has failed, it initiates an election.
- The algorithm ensures that the active process with the highest ID wins and becomes the new coordinator.

## How it Works
1. A process initiates an election by sending an "Election" message to all processes with higher IDs.
2. If any higher process is active, it responds with an "OK" message and takes over the election.
3. If no higher processes respond, the current process declares itself the coordinator and notifies all lower-priority processes.

## File Structure
```bash
bully_election_algorithm/
├── bully_election.c    # Source code in C
├── bully_election      # Compiled executable 
└── README.md           # This documentation
```

## Compilation & Usage

### 1. Compile the code
Use `gcc` or any C compiler:
```bash
gcc bully_election.c -o bully_election
```

### 2. Run the executable
```bash
./bully_election
```

### 3. Example Input
- **Number of processes**: `5`
- **Statuses**: `1 1 1 1 0` (Process 4, the highest, is failed)
- **Detecting process**: `1` (Process 1 notices something is wrong)

The program will then simulate the messages being sent between processes until Process 3 (the highest active process) is elected as the coordinator.
