// Write a program to recieve an array and print it in reverse order.

#include<stdio.h>
int main() {
    int n,i;
    long int arr[100];
    scanf("%d", &n);
    for(i=0;i<n;i++)
    scanf("%ld", &arr[i]);
    for(i=n-1;i>=0;i--)
    printf("%ld ", arr[i]);
    return 0;
}