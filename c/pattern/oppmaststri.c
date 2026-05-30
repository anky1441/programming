#include<stdio.h>
int main()
{
    int n;
    printf("enter the number of rows");
    scanf("%d",&n);
    int nsp=0,nst=n;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=nsp;j++ ){
            printf(" ");
        }
        for(int k=1;k<=nst;k++){
            printf("*");
        }
        nsp++;
        nst--;
        printf("\n");
    }
    return 0;
}