#include <stdio.h>
void BinarySearch(int[], int);
void bubble_sort(int[], int);
int count = 0;
void main()
{
    int n, a[100], i;
    printf("Enter a number of elements: ");
    scanf("%d", &n);
    printf("Enter %d elements: ", n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    BinarySearch(a, n);
    printf("\nCount= %d", count);
}
void BinarySearch(int a[], int n)
{
    int low, high, mid, i, j, temp, num;
    count++;
    bubble_sort(a, n);
    printf("Sorted array: ");
    count++;
    for (i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }
    count++;
    printf("\nEnter a number to search: ");
    scanf("%d", &num);
    low = 0, high = n - 1;
    count++;
    while (low <= high)
    {
        count++;
        mid = (low + high) / 2;
        count++;
        if (a[mid] == num)
        {
            printf("%d is present at index %d", num, mid);
            break;
        }
        else if (a[mid] < num)
        {
            count++;
            count++;
            low = mid + 1;
            count++;
        }
        else
        {
            count++;
            count++;
            high = mid - 1;
        }
        count++;
    }
    count++;
    count++;
    if (low > high)
    {
        printf("%d is not present in the array", num);
    }
    count++;
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
