#include <stdio.h>
#include <time.h>
void bubble_sort(int[], int);
void main()
{
    int a[10000], n, i;
    time_t t;
    double time_taken;
    clock_t start, end;
    printf("Enter number of elements: ");
    scanf("%d", &n);
    srand((unsigned)time(&t));
    for (i = 0; i < n; i++)
    {
        a[i] = rand() % 1000;
    }
    printf("Random generated %d elements are: ", n);
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    start = clock();
    bubble_sort(a, n);
    end = clock();
    printf("\nAfter bubble sort, elements are: ");
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    time_taken = (double)(end - start) /
                 CLOCKS_PER_SEC;
 printf("\nTime taken by bubble sort for random 
unsorted array: %lf", time_taken);
 for (i = 0; i < n; i++)
 {
        a[i] = i + 1;
 }
 printf("\nSorted %d elements are: ", n);
 for (i = 0; i < n; i++)
 {
        printf("%d ", a[i]);
 }
 start = clock();
 bubble_sort(a, n);
 end = clock();
 printf("\nAfter bubble sort, elements are: ");
 for (i = 0; i < n; i++)
 {
        printf("%d ", a[i]);
 }
 time_taken = (double)(end - start) / 
CLOCKS_PER_SEC;
 printf("\nTime taken by bubble sort for sorted
array: %lf", time_taken);
}
void bubble_sort(int a[], int n)
{
 int i, j, temp, flag;
 for (i = 0; i < n - 1; i++)
 {
     flag = 0;
     for (j = 0; j < n - 1 - i; j++)
     {
         if (a[j] > a[j + 1])
         {
             temp = a[j];
             a[j] = a[j + 1];
             a[j + 1] = temp;
             flag = 1;
         }
     }
     if (flag == 0)
     {
         break;
     }
 }
}
