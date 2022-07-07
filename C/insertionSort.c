// Inserion sort 
/* It's a simple sorting algorithm that works similarly to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
used when:
- the array is has a small number of elements
- there are only a few elements left to be sorted
 */

#include<stdio.h>

void insertion_sort(int arr[], int n) {
  int i,j,key;
  
  for(i=1;i<n;i++) {
    key = arr[i];
    j=i-1;

    while(j>=0 && arr[j]>key) {
      arr[j+1] = arr[j];
      --j;
    }
    
    arr[j+1] = key;
  }
}

void print_array(int arr[], int n) {
  for(int i=0;i<n;i++) {
    printf("%d ", arr[i]);
  }
}

int main() {
  int arr[] = {6,4,1,8,3};
  int n = sizeof(arr)/ sizeof(arr[0]);
  
  insertion_sort(arr,n);
  print_array(arr,n);

  return 0;
}


/* 
  Worst Case Complexity: O(n2)
  Best Case Complexity: O(n)
  Average Case Complexity: O(n2)
*/
