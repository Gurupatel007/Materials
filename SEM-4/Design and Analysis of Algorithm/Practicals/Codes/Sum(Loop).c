#include <stdio.h>
void add_loop(int);
int count = 0;
int main()
{
    int n;
    printf("Enter number:- ");
    scanf("%d", &n);
    add_loop(n);
    return 0;
}
void add_loop(int n)
{
    int i;
    int sum = 0;
    count++;
    for (i = 1; i <= n; i++)
    {
        count++;
        sum = sum + i;
        count++;
    }
    count++;
    printf("%d", count);
}
