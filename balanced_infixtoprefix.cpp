/*Write C++ program using stack to check whether given 
infix expression is well 
parenthesized or not.
Convert the entered infix expression to prefix*/
#include<bits/stdc++.h>
using namespace std;
bool isOperator(char c)
{
    if(c=='+' or c=='/' or c=='*' or c=='-')
    return true;
    else
    return false;
}
int precedence(char ch)
{
    if(ch=='/' or ch=='*')
    return 2;
    else if(ch=='+' or ch=='-')
    return 1;
    else
    return -1;
}
string infixtoprefix(string expression)
{
    stack<char> s;
    string str="";
    for(char& c: expression)
    {
        if(isalnum(c))
        {
            str+=c;
        }
        else if(c=='(')
        {
            s.push(c);
        }
        else if(c==')')
        {
            while(s.top()!='(')
            {
                str+=s.top();
                s.pop();
            }
            s.pop();
        }
        else
        {
            while(!s.empty() and precedence(s.top())>=precedence(c))
            {
                str+=s.top();
                s.pop();
            }
            s.push(c);
        }
    }
    while(!s.empty())
    {
        str+=s.top();
        s.pop();
    }
    reverse(str.begin(),str.end());
    return str;
}
int main()
{
    
}