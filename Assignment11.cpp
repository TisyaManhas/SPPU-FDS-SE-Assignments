/* Implement C++ program for expression conversion as infix to postfix and its evaluation using stack based on given conditions 
i. Operands and operator, both must be single character. 
ii. Input Postfix expression must be in a desired format. 
iii. Only '+', '-', '*' and '/ ' operators are expected  */

#include<bits/stdc++.h>
using namespace std;

// Function to check if a character is an operator
bool isOperator(char c)
{
    return(c=='+' or c== '-' or c=='/' or c=='*');
}
// Function to get precedence of an operator
int getPrecedence(char op){
    if(op=='+' or op=='-') return 1;
    else if(op == '*' || op == '/') return 2;
    return 0;
}
// Function to convert infix expression to postfix
string infixToPostfix(string infix) {
    stack<char> s;
    string postfix = "";
    for (char& c : infix) {
        if (isalnum(c)) {
            postfix += c;
        }else if (c == '(') {
            s.push(c);
        }else if(c==')'){
           while (!s.empty() && s.top() != '(') {
                postfix += s.top();
                s.pop();
            }
            if (!s.empty() && s.top() == '(') {
                s.pop();
            } 
        }else{
            while (!s.empty() && getPrecedence(c) <= getPrecedence(s.top())) {
                postfix += s.top();
                s.pop();
            }
            s.push(c);
        }
}
while (!s.empty()) {
        postfix += s.top();
        s.pop();
    }
return postfix;
}
int main() {
    string infixExpression = "a+b*c-(d/e+f*g*h)";
    string postfixExpression = infixToPostfix(infixExpression);

    cout << "Infix Expression: " << infixExpression << endl;
    cout << "Postfix Expression: " << postfixExpression << endl;

    return 0;
}