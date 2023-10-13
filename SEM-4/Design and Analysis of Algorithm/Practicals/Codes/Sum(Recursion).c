#include <stdio.h>
int count = 0;
void main()
{
    int n;
    int sum = 0;
    printf("enter number:- ");
    scanf("%d", &n);
    sum = rec(n);
    printf("sum is:-%d", sum);
    printf("\ncount is:-%d", count);
}
int rec(int n)
{
    count++;
    if (n != 0)
    {
        count++;
        return n + rec(n - 1);
        count++;
    }
    else
    {
        count++;
        count++;
        return 0;
    }
}