/*Addition Binary*/
#include<bits/stdc++.h>
using namespace std;
class Node
{
    public:
    Node* next;
    Node* prev;
    bool val;
    Node()
    {
        next=NULL;
        prev=NULL;
    }
    Node(bool data){
        next=NULL;
        prev=NULL;
        val=data;
    }
};
void getbinary(Node* &head,Node* &tail,bool data)
{
    Node* ptr=new Node(data);
    if(head==NULL){
        head=ptr;
        tail=ptr;
    }
    else
    {
        tail->next=ptr;
        ptr->prev=tail;
        tail=ptr;
    }
}

void display(Node* &head)
{
    cout<<"The binary number is:"<<endl;
    Node* temp=head;
        while(temp!=NULL)
        {
            cout<<temp->val;
            temp=temp->next;   
        }
        cout<<endl;
}
void AddBinary(Node* &head,Node* &head2,Node*&head3,Node* &tail3)
{
    Node* first=head;
    Node* second=head2;
    // bool x[15];
    while(first->next!=NULL)
    {
        first=first->next;
    }
    while(second->next!=NULL)
    {
        second=second->next;
    }
    int carry=0;
    int sum,r;
    while(first!=NULL and second!=NULL)
    {
        sum=carry+first->val+second->val;
        r=sum%2;
        carry=sum/2;
        getbinary(head3,tail3,r);
        first=first->prev;
        second=second->prev;
    }
    while(first!=NULL)
    {
        sum=carry+first->val;
        carry=sum/2;
        r=sum%2;
        getbinary(head3,tail3,r);
        first=first->prev;
    }
    while(second!=NULL)
    {
        sum=carry+first->val;
        carry=sum/2;
        r=sum%2;
        getbinary(head3,tail3,r);
        second=second->prev;
    }
    if(carry)
    {
        getbinary(head3,tail3,carry);
    }
}
int main()
{
    Node* head=NULL;
    Node* tail=NULL;
    Node* head2=NULL;
    Node* tail2=NULL;
    Node* head3=NULL;
    Node* tail3=NULL;
    int n1;
    cout<<"Enter length of first Binary Number:";
    cin>>n1;
    while(n1>0)
    {
        bool x;
        cout<<"Enter binary element:";
        cin>>x;
        getbinary(head,tail,x);
        n1--;
    }
    cout<<"FIRST BINARY NUMBER:"<<endl;
    display(head);

    int n2;
    cout<<"Enter length of second Binary Number:";
    cin>>n2;
    while(n2>0)
    {
        bool x;
        cout<<"Enter binary element:";
        cin>>x;
        getbinary(head2,tail2,x);
        n2--;
    }
    cout<<"First Binary Number:"<<endl;
    display(head);
    cout<<"Second Binary Number:"<<endl;
    display(head2);
    cout<<"After Addition: "<<endl;
    AddBinary(head,head2,head3,tail3);
    display(head3);
    return 0;
}