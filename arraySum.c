#include <stdio.h>

int main()
{
    int n,k;
    scanf("%d%d",&n,&k);
    int a[n],sum=0;
    for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
    for(int i=0;i<k;i++)
        sum+=a[k];
    printf(sum);
    
    return 0;
}
