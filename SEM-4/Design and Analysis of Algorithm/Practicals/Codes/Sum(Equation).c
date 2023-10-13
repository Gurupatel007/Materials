#include <stdio.h>
int count = 0;
int main()
{
    int n;
    int sum = 0;
    printf("enter number:- ");
    scanf("%d", &n);
    count++;
    sum = (n * (n + 1)) / 2;
    printf("sum is:- %d", sum);
    printf("\ncount is:- %d", count);
    return 0;
}