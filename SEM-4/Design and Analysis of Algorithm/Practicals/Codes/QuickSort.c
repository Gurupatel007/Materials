#include <stdio.h>
#include <time.h>
void quick_sort(int a[], int lb, int ub)
{
    int pivot, start, end, temp;
    if (lb < ub)
    {
        pivot = lb;
        start = lb;
        end = ub;
        while (start < end)
        {
            while (a[pivot] >= a[start])
            {
                start++;
            }
            while (a[pivot] < a[end])
            {
                end--;
            }
            if (start < end)
            {
                temp = a[start];
                a[start] = a[end];
                a[end] = temp;
            }
        }
        temp = a[pivot];
        a[pivot] = a[end];
        a[end] = temp;
        quick_sort(a, lb, end - 1);
        quick_sort(a, end + 1, ub);
    }
}
int main()
{
    int a[100], i, n;
    time_t t;
    double time_taken;
    clock_t start, end; // lb-lower bound ub-upper bound printf("Enter number of elements: ");
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
    quick_sort(a, 0, n - 1);
    end = clock();
    printf("\nAfter quick sort, elements are: ");
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("\nTime taken by quick sort for random unsorted array: %lf", time_taken);
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
    quick_sort(a, 0, n - 1);
    end = clock();
    printf("\nAfter quick sort, elements are: ");
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("\nTime taken by quick sort for sorted array: %lf", time_taken);
    return 0;
}
