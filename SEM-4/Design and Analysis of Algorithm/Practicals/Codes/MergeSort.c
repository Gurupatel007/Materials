#include <stdio.h>
#include <time.h>
int a[10000], b[10000];
void merge(int a[], int lb, int mid, int ub)
{
    int i, j, k;
    i = lb;
    j = mid + 1;
    k = lb;
    while (i <= mid && j <= ub)
    {
        if (a[i] <= a[j])
        {
            b[k] = a[i];
            i++;
            k++;
        }
        else
        {
            b[k] = a[j];
            j++;
            k++;
        }
    }
    if (i > mid)
    {
        while (j <= ub)
        {
            b[k] = a[j];
            j++;
            k++;
        }
    }
    else
    {
        while (i <= mid)
        {
            b[k] = a[i];
            i++;
            k++;
        }
    }
    for (i = lb; i <= ub; i++)
    {
        a[i] = b[i];
    }
}
void merge_sort(int a[], int lb, int ub)
{
    int mid;
    if (lb < ub)
    {
        mid = (lb + ub) / 2;
        merge_sort(a, lb, mid);
        merge_sort(a, mid + 1, ub);
        merge(a, lb, mid, ub);
    }
}
void main()
{
    int n, i, j;
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
    merge_sort(a, 0, n - 1);
    end = clock();
    printf("\nAfter merge sort, elements are: ");
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("\nTime taken by merge sort for random unsorted array: %lf", time_taken);
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
    merge_sort(a, 0, n - 1);
    end = clock();
    printf("\nAfter merge sort, elements are: ");
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("\nTime taken by merge sort for sorted array: %lf", time_taken);
}
