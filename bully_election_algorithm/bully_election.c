#include <stdio.h>
int processes[10], n; 
int coordinator;   

int request(int i) {
  if (processes[i] == 1)
    return 1; 
  else
    return 0; 
}
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
void displayCoordinator() {

  printf("\nCurrent Coordinator is Process %d\n", coordinator);
}


int main() {
  int i, failed;
  printf("Enter number of processes: ");
  scanf("%d", &n);
  printf("Enter status of each process (1 = Active, 0 = Failed):\n");
  for (i = 0; i < n; i++) {
    printf("Process %d: ", i);
    scanf("%d", &processes[i]);
  }
  printf("\nEnter the process which detects failure: "); 
  scanf("%d", &failed);
  if(processes[failed]==0){
    
    printf("Process %d is failed\n", failed);
    return 0;
  }
  election(failed);
  displayCoordinator();
  return 0;
}