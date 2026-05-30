#include<stdio.h>
int main()
{
    int n;
    printf("enter the number of rows");
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        int c=64+i-1;
        for(int j=1;j<=n-i;j++){
            printf(" ");
        }
        for(int k=65;k<=64+i;k++){
            printf("%c",k);
        }
        for(int l=65;l<=64+i-1;l++){
            printf("%c",c);
            c--;
        }
        printf("\n");
    }
    return 0;
}