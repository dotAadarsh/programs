// Selectio sort

#include<stdio.h>

// Function to swap
void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

// Function to perform selection sort
void selectionSort(int arr[], int n) {
  
  for(int step = 0; step<n-1; step++) {
    int min_index = step;
    
    for(int i = step+1; i<n; i++) {
      // For decending order just change < to >
      if(arr[i] < arr[min_index]) {
        min_index = i;
      }
    }
    
    swap(&arr[min_index], &arr[step]);
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
  
  selectionSort(arr, n);
  printArr(arr, n);
  
  return 0;
}
