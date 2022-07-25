// Write a program to accept an array of elements  and print it

#include<stdio.h>
int main() {
    int n, i;
    int arr[100];
    scanf("%d", &n);
    for(i=0;i<n;i++)
 {   scanf("%d", &arr[i]);
     printf("%d ", arr[i]);
}
    
}
