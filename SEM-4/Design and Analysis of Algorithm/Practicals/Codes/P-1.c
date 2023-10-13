#include<stdio.h>
int count_loop=0;
int count_equ=0;
int count_rec=0;
void fun_loop(int n){
    int sum=0;
    count_loop++;
    for(int i=1;i<=n;i++){
        sum+=i;
        count_loop++;
    }
    printf("\nSum=%d",sum);
    printf("\nCount=%d",count_loop);
}
void fun_equ(int n){
    int sum=0;
    count_equ ++;
    sum=(n*(n+1))/2;
    count_equ ++;
    printf("\nSum=%d",sum);
    printf("\nCount=%d",count_equ);
}
int fun_rec(int n){
    int sum=0;
    if(n==1){
        count_rec ++;
        return 1;
    }
    else{
        count_rec ++;
        return (n+fun_rec(n-1));
    }
}
int main(){
    int n;
    scanf("%d",&n);
    fun_equ(n);
    fun_loop(n);
        int add=fun_rec(n);
    printf("\nSum=%d",add);
    printf("\nCount=%d",count_rec);
    return 0;
}