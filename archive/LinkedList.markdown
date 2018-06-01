#Linked List

##Some of the most common functions implementations in Linked List In Java

```Java
import java.awt.List;

//Linked list insert operation 
//push at the beginning of the list
//append at the end of the list
//insert at the perticular position
//print the link list

public class Linklist {
Node head;
public class Node{
	int data;
	Node next;
	
	Node(int item){
		data = item;
		next = null;
	}
}

public void push(int data){
	Node new_node = new Node(data);
	if(head==null){
		head = new_node;
		new_node.next=null;
	}
	else{
		new_node.next = head;
		head = new_node;
	}
	
}


public void append(int data){
	Node new_node = new Node(data);
	Node temp=head;
	if(head == null){
		head = new_node;
	}
	else{
		while(temp.next!=null){
			temp=temp.next;
		}
		temp.next=new_node;
		new_node.next=null;
	}
}


public void insert(Node given_node, int data ){
	Node new_node =  new Node(data);
	//if the list is empty
	if(head==null){
		System.out.println("Underflow error");
	}
	else{
		Node temp=head;
		while(temp.next!=given_node){
			temp = temp.next;
		}
		//insert at the last node
		if(temp.next.next==null){
			temp.next.next= new_node;
			new_node.next=null;
		}
		// insetion in between the nodes in the linked list
		else{
			new_node.next = temp.next.next;
			temp.next.next =  new_node;	
			//System.out.println("node inserted");
		}
						
	}
	
}



public void printlist(Node head){
	if(head==null){
		System.out.println("Empty list");
	}
	else{
		Node temp =head;
		while(temp!=null){
			System.out.print(temp.data + " ");
			temp=temp.next;
		}
	}
}

public void delete(Node given_node){
	
	Node temp = head;
	while(temp.next!=given_node){
		
	}
	
	
}

//printing the length of the linked list
public int lenghtll(Node head){
	int result=0;
	if(head==null){
		result= 0;
	}
	else{
		Node temp=head;
		while(temp!=null){
			temp=temp.next;
			result++;
		}
	}
	return result;
	
}

//recursive implementation to find the length of the linked list

public int reclength(Node head){
	if(head==null){
		return 0;
	}
	else{
	return 1 + reclength(head=head.next);	
	}
	
	
}

//function to search within a linked list and return true or false based on that
public boolean searchelement(Node head,int item){
	Node temp=head;
	boolean result=false;
	if(head==null){
		System.out.println("list is empty");
	}
	while(temp!=null){
		if(temp.data==item){
			result =true;
			break;
		}
		temp=temp.next;
	}
	return result;
}


//function to reverse a linked list using iteration method
public Node reverse(Node head){
	if(head==null||head.next==null)
		return head;
	Node first=head;
	Node rest=first.next;	
	Node new_head = reverse(rest);
	first.next.next=first;	
	first.next=null;
	head=rest;
	return new_head;
	
}


//Interative function to reverse the linked list
public Node reverse_iter(Node head){
	Node first,second,temp;
	first=head;
	second=first.next;
	temp=second;
	while(second!=null){
		second=second.next;
		temp.next=first;
		first=temp;
		temp=second;
		
	}
	head.next=null;
	head=first;
	return head;
	
}

//Function to detect a loop in a linked list
public boolean detectloop(Node head){
	Node first=head;
	Node second=head.next.next;
	boolean result=false;
	while(second.next!=null&&second.next.next!=null){
		if(first==second){
			result = true;
			return result;
		}
		else{
			second = second.next.next;
			first=first.next;
		}	
	}
	return result;
}



}





```
