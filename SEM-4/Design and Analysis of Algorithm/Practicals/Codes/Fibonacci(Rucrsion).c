#include <stdio.h>
void Fibonacci(int);
int count = 0;
void main()
{
    int n;
    printf("Enter nth Fibonacci number: ");
    scanf("%d", &n);
    printf("The Fibonacci series is: ");
    printf("%d %d ", 0, 1);
    count++;
    Fibonacci(n - 2);
    printf("\nCount= %d", count);
}
void Fibonacci(int n)
{
    static int n1 = 0, n2 = 1, n3;
    count++;
    if (n > 0)
    {
        count++;
        n3 = n1 + n2;
        count++;
        n1 = n2;
        count++;
        n2 = n3;
        printf("%d ", n3);
        count++;
        Fibonacci(n - 1);
        count++;
    }
    count++;
}
