// Write a program to print the value of the respective given index for the given array.

#include<stdio.h>
int main() {
    
    int n, index, i;
    long int arr[100];
    scanf("%d", &n);
    for(i=0;i<n;i++){
        scanf("%ld", &arr[i]);
    }
    scanf("%d", &index);
    if(index<=n)
    printf("%ld", arr[index]);
    else
    printf("-1");
    
    return 0;
}