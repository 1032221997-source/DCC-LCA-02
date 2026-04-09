#include <stdio.h>

int processes[10], n; // processes array stores the status of the process that
                      // is active or failed
// n is the number of processes
int coordinator;   // stores the coordinator process id

// request function.. to stimulate actual bully algorithm
int request(int i) {
  if (processes[i] == 1)
    return 1; // OK response
  else
    return 0; // No response
}
// Main election function..recursion function..

void election(int initiator) {
  int i;
  int responded = 0;

  printf("\nProcess %d is initiating election...\n", initiator);

  for (i = initiator + 1; i < n; i++) {
    if (request(i) == 1) {
      printf("Process %d sends election message to Process %d\n", initiator, i);
      printf("Process %d sends OK to Process %d\n", i, initiator);

      responded = 1;
      election(i);
    }
  }

  if (responded == 0) {
    coordinator = initiator;
    printf("Process %d becomes coordinator\n", coordinator);
  }
}
// Simple print function for displaying the coordinator /election leader..
void displayCoordinator() {

  printf("\nCurrent Coordinator is Process %d\n", coordinator);
}

// Main function...
int main() {
  int i, failed;
  printf("Enter number of processes: ");
  scanf("%d", &n);
  printf("Enter status of each process (1 = Active, 0 = Failed):\n");
  for (i = 0; i < n; i++) {
    printf("Process %d: ", i);
    scanf("%d", &processes[i]);
  }
  printf("\nEnter the process which detects failure: "); //this is the initiator process that detects that the coordinator has failed
  scanf("%d", &failed);
  if(processes[failed]==0){
    //since the election function does not check if the first initiator is failed process or not..
    printf("Process %d is failed\n", failed);
    return 0;
  }
  election(failed);
  displayCoordinator();
  return 0;
}