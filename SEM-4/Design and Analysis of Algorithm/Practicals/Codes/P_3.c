#include<stdio.h> 
#include<time.h> 
#include <stdlib.h> 
 
 
void selection(int arr[], int n) ; 
void printArr(int arr[], int n); 
 
int main(){ int 
n=10; 
 int arr[n]; 
 
 for(int i=0;i<n;i++){ 
arr[i]=rand(); 
 } 
 
 for(int i=0;i<n;i++){ 
printf("%d\t",arr[i]); 
 } 
 
 clock_t t_start,t_end,t_mid; t_start = clock(); 
//starting time after initializing data 
printf("t_start=%lu\n",t_start); 
 
 selection( arr, n); 
 t_mid=clock(); //mid time after function call 
 printf("t_mid=%lu\n",t_mid); 
 
 t_end = t_mid - t_start; //ending time after mid - start 
printf("t_end=%lu\n",t_end); 

 double time_taken = ((double)t_end)/CLOCKS_PER_SEC; //clock per sec is a macro 1cps= 1 million micro sec ;
 printf("fun() took %f seconds to execute \n", time_taken); 
 
 printArr(arr, n); 
 
 return 0; 
 
} 
 
 
void selection(int arr[], int n) 
{ int i, j, 
small; 
 
 for (i = 0; i < n-1; i++) // One by one move boundary of unsorted subarray 
 { 
 small = i; //minimum element in unsorted array 
 for (j = i+1; j < 
n; j++) 
if (arr[j] < arr[small]) 
 small = j; 
// Swap the minimum element with the first element 
int temp = arr[small]; arr[small] = arr[i]; 
 arr[i] = temp; 
 } 
} 
 
void printArr(int arr[], int n) /* function to print the array */ 
{ int 
i; 
 for (i = 0; i < n; i++) 
printf("%d\t ", arr[i]); 
} 