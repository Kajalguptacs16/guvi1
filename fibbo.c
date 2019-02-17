#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    int a=1,b=1,c;
    printf("%d",a);
    printf("%d",b);
    while((n-2)!=0)
    {
        c=a+b;
        a=b;
        b=c;
        printf("%d",c);
        n=n-1;
    }

    return 0;
}
