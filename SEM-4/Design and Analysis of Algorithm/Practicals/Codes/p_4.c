#include<stdio.h>
int BinarySearch(int a[],int n,int key){
    int s=0;
    int e=n;
    while(s<=e){
        int mid=(s+e)/2;
        if(a[mid]==key){
            return mid;
        }
        else if(a[mid]>key){
            e=mid-1;
        }
        else{
            s=mid+1;
        }
    }
    return -1;
}
int linersearch(int a[],int n,int key){
    
}

int main(){
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    printf("Enter the values: ");
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int key;
    printf("\nEnter the Key :");
    scanf("%d",&key);

    int x=BinarySearch(arr,n,key);
    printf("index :%d",x);
}