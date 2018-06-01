#Linked List Implementation of stack

## Things to keep in mind:

* No need to know maxsize.
* No need of top variable, Node head will be our top.
* add element in front of the list.

```java

public class Stack_ll {
Node head;
//define LL data structure	
	public class Node{
		Node next;
		int data;
	public Node(int d){
		data = d;
		next=null;
	}
}

public void push(int data){
	if(head == null){
		head = new Node(data);
	}
	else{
		Node newNode =  new Node(data);
		newNode.next= head;
		head = newNode;
	}
	
}

public int pop(){
	if(head == null)
		return -1;
	else{
		int result = head.data;
		head = head.next;
		return result;
	}
}

public boolean isEmpty(){
	if(head == null)
		return true;
	return false;
}

	
	

}

```
