#include <stdio.h> 
 
int count_ite=0; 
int count_rec=0; 
 
void fib_ite(int ); 
int fib_rec(int n ); 
 
int main(){ 
int n; 
 printf("enter the fib no = "); 
scanf("%d",&n); 
fib_ite(n); int ans=fib_rec(n); 
 printf("%dth number is = %d\n",n,ans); 
printf("recursion step count = %d\n",count_rec); return 
0; 
} 
 
void fib_ite(int n ){ 
int n1=0; int 
n2=1; int n3,i; 
 if(n==0) 
{ 
count_ite++; 
n3=0; 
 } 
else { 
for(i=2;i<=n;i++){ count_ite++; 
n3=n1+n2; count_ite++; 
n1=n2; count_ite++; 
n2=n3; 
 } 
 } 
 printf("iteration step count = %d\n",count_ite); 
printf("%dth number is = %d\n",n,n3); 
} 
 
 
int fib_rec(int n){ if(n==0){ 
count_rec++; 
 return 0; 
 } 
 else if(n==1){ count_rec++; 
 return 1; 
 } 
 else{ 
count_rec++; 
 return fib_rec(n-1)+fib_rec(n-2); 
 } 
} 