#Stack Array Implementation

# Stack implementation in array. Things to keep in mind:

* Maximum Size of the array(to calculate isFull funciton)
* Element to insert in stack
* An Array with size maxElement
* Top of the stack

```java
public class Stack {
	int maxSize;
	long[] stackArray;
	int top;
	
	public Stack(int size){
			maxSize=size;
			stackArray = new long[maxSize];
			top =-1;
	}
	
	public void push(long num){
		stackArray[++top]=num;
	}
	
	public long pop(){
	return stackArray[top--];	
		
	}
	
	public boolean isEmpty(){
		if(top==-1)
			return true;
		return false;
		}
	
	public boolean isFull(){
		if(top==maxSize-1)
			return true;
		return false;
	}

}


```
