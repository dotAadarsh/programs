// Bubble sort

#include<stdio.h>

// Function to swap
void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

// Function to perform Bubble sort
void bubbleSort(int arr[], int n) {
  int i, j;
  int swapped = 0;
  
  for(i = 0;i<n-1;i++){
      for(j=0;j<n-i-1;j++) {
        if(arr[j]>arr[j+1]) {
          swap(&arr[j], &arr[j+1]);
          swapped = 1;
        }
      }
    
    if(swapped == 0)
      break;
  }
  }

// Function to print the array
void printArr(int arr[], int n) {
  for(int i = 0;i<n;i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

// Driver code
int main() {
  int arr[] = {10, 2, 15, 1, 7};
  int n = sizeof(arr)/sizeof(arr[0]);
  
  bubbleSort(arr, n);
  printArr(arr, n);
  
  return 0;
}
