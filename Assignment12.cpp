/*
In any language program mostly syntax error occurs due to
unbalancing delimiter such as (),{},[].Write C++ program using stack
to check whether given expression is well parenthesized or not.
*/
#include<bits/stdc++.h>
using namespace std;

bool iswellparen(string expression)
{
    stack<char> s;
    for(char& c:expression){
        if(c=='(' or c=='[' or c=='{')
        {
            s.push(c);
        }
        else if(c==')' or c=='}' or c==']')
        {
            if(s.empty()){
                return false;
            }
            else if((c==')' and s.top()=='(') or(c=='}' and s.top()=='{') or (c==']' and s.top()=='['))
            {
                s.pop();
            }
        else{
            return false;
        }
    }
}
return s.empty();
}
int main()
{
    string expression="{(a+b)-(a-c)*[(a+b+c)-(a+b)]}";
    if(iswellparen(expression)){
        cout<<"Expression is well parenthesized"<<endl;
    }else
    {
        cout << "Expression is not well-parenthesized." << endl;
    }
    return 0;
}
