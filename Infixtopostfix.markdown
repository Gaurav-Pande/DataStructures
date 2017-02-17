# Conversion from infix expression to postfix expression

```java
import java.util.ArrayList;
import java.util.Stack;

public class infixtopostfix {
	
	
	public static int precedence(char ch){
		
		switch (ch){
		case '+':
		case '-':
			return 1;
		case '*':
		case '/':
			return 2;
		case '^':
			return 3;
		}
		
		return -1;	
	}
	
	public String infix2postfix(String exp){
		Stack<Character> s = new Stack<Character>();
		String result = "";
    //Run char by char for loop
    //if the char is operand add to result
    //if the chat is operator, look in the stack and check for precedence,i.e if the precedence of the top elem at stack is more
    //than the precedence of the current char than pop the element and add to the result untill all the higher precedence 
    //chars are not popped out.
    //or if the current char is ')' than also you need to pop out the elements and add to the result
		for(int i=0;i<exp.length();i++){
		if ((exp.charAt(i)>='a'&&exp.charAt(i)<='z')||(exp.charAt(i) >='A'&&exp.charAt(i)<='Z')){
			result= result + exp.charAt(i);
		}
		else if(isOperator(exp.charAt(i))){
			while(!s.isEmpty()&&isHigherPrecedence(s.peek(),exp.charAt(i)) && s.peek()!='('){
				result = result + s.pop();
			}
			s.push(exp.charAt(i));
		}
		else if(exp.charAt(i)=='('){
			s.push(exp.charAt(i));
		}
		else if(exp.charAt(i)==')'){
			while(!s.isEmpty() && s.peek()!='('){
				result= result + s.pop();
			}
			s.pop();
		}
			
		}
		while(!s.isEmpty()){
			result = result + s.pop();
		}
		return result.toString();
		
}
	
//Important to note that while calculating precedence associativity rule need to be keep in mind
//for char '^',if the precedence is same, than check for right to left associativity
//for the rest of the char if the precedence is same,check for left to write associativity.

	private boolean isHigherPrecedence(Character peek, char charAt) {
		// TODO Auto-generated method stub
		if(precedence(peek)==precedence(charAt)){
			if(peek!='^')
				return true;
			else
				return false;
		}
		if(precedence(peek)>precedence(charAt)){
			return true;
		}
		else{
			return false;
		}
		
	}

	private boolean isOperator(char C) {
		// TODO Auto-generated method stub
		if(C == '+' || C == '-' || C == '*' || C == '/' || C== '^')
			return true;

		return false;
	}

//Simple test function to test the functionality
	public static void main(String args[]){
		infixtopostfix i = new infixtopostfix();
		System.out.println(i.infix2postfix("a+b*(c^d-e)^(f+g*h)-i"));
		
	}
}


```
