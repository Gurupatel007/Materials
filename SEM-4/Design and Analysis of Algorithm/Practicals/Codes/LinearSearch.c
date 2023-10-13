#include <stdio.h>
void SequentialSearch(int[], int);
int count = 0;
void main()
{
    int a[100], n, num, i;
    printf("Enter a number of elements: ");
    scanf("%d", &n);
    printf("Enter %d elements: ", n);
    count++;
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    count++;
    count++;
    SequentialSearch(a, n);
    printf("\nCount= %d", count);
}
void SequentialSearch(int a[], int n)
{
    int i, num;
    printf("Enter a number to search: ");
    scanf("%d", &num);
    count++;
    for (i = 0; i < n; i++)
    {
        count++;
        if (a[i] == num)
        {
            printf("%d is present at index %d", num, i);
            count++;
            break;
        }
    }
    count++;
    count++;
    if (i == n)
    {
        printf("%d is not present in the array", num);
    }
    count++;
}
