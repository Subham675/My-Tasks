#include<iostream>
using namespace std;
class arr
{
    int a[10][10],b[10][10],c[10][10],d[10][10],i,j,k,r1,c1,r2,c2;
    public:
    void input();
    void output( int x[][10],int ,int);
    void matadd();
    void matmul();
};
void arr:: input()
{
    cout<<"\n enter the value for row of matrix1 ";
    cin>>r1;
    cout<<"\n enter the value for col of matrix1 ";
    cin>>c1;
    cout<<"\n enter the value for row of matrix2 ";
    cin>>r2;
    cout<<"\n enter the value for col of matrix2 ";
    cin>>c2;
    for(i=0;i<r1;i++)
    {
        for(j=0;j<c1;j++)
        {
            cout<<"\nenter the value for a["<<i<<"]["<<j<<"]";
            cin>>a[i][j];
        }
    }

for(i=0;i<r2;i++)
   {
    for(j=0;j<c2;j++)
    {
        cout<<"\nenter the value for b["<<i<<"]["<<j<<"]" ;
        cin>>b[i][j];
    }

   }
}
void arr:: output(int x[][10],int r,int c)
{
cout<<"\n the elements of matrix are follows: \n\n";
for(i=0;i<r;i++)
    {
        for(j=0;j<c;j++)
        cout<<" "<<x[i][j];
    cout<<"\n";
    }
}
void arr::matadd()
{
    if(r1==c1 && r1==c2)
    {
        for(i=0;i<r2;i++)
        {
            for(j=0;j<c2;j++)
            c[i][j]=a[i][j]+b[i][j];
        }
        output(c,r1,r2);
    }
    
    else
    cout<<"\n the addition is not possiblr due to different order b";
    
}
void arr::matmul()
{
    if(c2==r1)
    {
        for(i=0;i<r1;i++)
        {
            for(j=0;j<c2;j++)
            d[i][j]=0;
        }
            for(i=0;i<r1;i++)
            {
                for(j=0;j<c1;j++)
                {
                  for(k=0;k<c2;k++)
                  d[i][k]+=a[i][j]*b[j][k];
                }
            }
        
        output(d,r1,c2);
        
    }
        else
        cout<<"matrix multiplication is not possible due to different order";
}
    int main()
    {
        arr x;
        x.input();
        x.matadd();
        x.matmul();
        return 0;
    }