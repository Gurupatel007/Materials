#include <stdio.h>
void main()
{
    int n1 = 0, n2 = 1, n3, i, n, count = 0;
    printf("Enter nth Fibonacci number: ");
    scanf("%d", &n);
    printf("The Fibonacci series is: ");
    printf("%d %d ", n1, n2);
    count++;
    for (i = 3; i <= n; i++)
    {
        count++;
        n3 = n1 + n2;
        printf("%d ", n3);
        count++;
        n1 = n2;
        count++;
        n2 = n3;
        count++;
    }
    count++;
    printf("\nCount= %d", count);
}
