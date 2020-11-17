#include "LinkedList.h"

LinkedList::LinkedList(const LinkedList& list)
{
	tail = head = nullptr;
	count = 0;
	Node* temp = list.head;
	while (temp != nullptr)
	{
		addToTail(temp->data);
		temp = temp->next;
	}
}

LinkedList::~LinkedList()
{
	Node* temp = head;
	while (temp != nullptr)
	{
		Node* node = temp;
		temp = temp->next;
		delete node;
	}
}

bool LinkedList::indexValid(int index)
{
	return (index >= 0 && index < count);
}

int LinkedList::length()
{
	return count;
}

bool LinkedList::addToTail(int element)
{
	if (tail == nullptr)
	{
		head = tail = new Node(element);
	}
	else
	{
		tail->next = new Node(element);
		tail = tail->next;
	}
	++count;
	return true;
}

bool LinkedList::addToHead(int element)
{
	if (head == nullptr)
	{
		head = tail = new Node(element);
	}
	else
	{
		head = new Node(element, head);
	}
	++count;
	return true;
}

bool LinkedList::add(int element, int index)
{
	if (!indexValid(index))
	{
		return false;
	}
	if (index == 0)
	{
		addToHead(element);
	}
	if (index == count)
	{
		addToTail(element);
	}

	Node* temp = head;
	for (int i = 0; i < index - 1; ++i)
	{
		temp = temp->next;
	}
	temp->next = new Node(element, temp->next);
	++count;
	return true;
}

int LinkedList::get(int index)
{
	if (!indexValid(index))
	{
		return -1;
	}
	if (index == 0)
	{
		return head->data;
	}
	if (index == count - 1)
	{
		return tail->data;
	}

	Node* temp = head;
	for (int i = 0; i < index; ++i)
	{
		temp = temp->next;
	}
	return temp->data;
}

bool LinkedList::set(int index, int element)
{
	if (!indexValid(index))
	{
		return false;
	}
	if (index == 0)
	{
		head->data = element;
	}
	else if (index == count - 1)
	{
		tail->data = element;
	}
	else
	{	
		Node* temp = head;
		for (int i = 0; i < index; ++i)
		{
			temp = temp->next;
		}
		temp->data = element;
	}
	return true;
}

int& LinkedList::operator[](int index)
{
	if (head == nullptr)
	{
		addToHead(0);
		return head->data;
	}
	if (index <= 0)
	{
		return head->data;
	}
	if (index >= count)
	{
		addToTail(0);
		return tail->data;
	}
	if (index == count - 1)
	{
		return tail->data;
	}
	Node* temp = head;
	for (int i = 0; i < index; ++i)
	{
		temp = temp->next;
	}
	return temp->data;
}

std::ostream& operator<<(std::ostream& stream, const LinkedList list)
{
	stream << "[" << list.count << "]{";
	if (list.head == nullptr)
	{
		stream << "EMPTY";
	}
	else
	{
		Node* temp = list.head;
		while (temp != nullptr)
		{
			stream << temp->data;
			if (temp->next != nullptr)
			{
				stream << ", ";
			}
			temp = temp->next; //ïåðåõîäèì íà ñëåäóþùèé ýëåìåíò
		}
	}
	stream << "}";
	return stream;
}

void LinkedList::operator+=(int element)
{
	addToTail(element);
}

int LinkedList::extractHead()
{
	if (head == nullptr)
	{
		return -1;
	}
	int element = head->data;
	Node* temp = head->next;
	delete head;
	head = temp;
	--count;
	return element;
}

int LinkedList::extractTail()
{
	if(tail == nullptr)
	{
		return -1;
	}
	int element = tail->data;
	Node* temp = head;
	for (int i = 0; i < count - 2; ++i)
	{
		temp = temp->next;
	}
	delete tail;
	tail = temp;
	tail->next = nullptr;
	--count;
	return element;
}

int LinkedList::extract(int index)
{
	if (!indexValid(index))
	{
		return -1;
	}
	if (index == 0)
	{
		extractHead();
	}
	if (index == count - 1)
	{
		extractTail();
	}
	Node* temp1 = head;
	for (int i = 0; i < index - 1; ++i)
	{
		temp1 = temp1->next;
	}
	Node* temp2 = temp1->next;
	int element = temp2->data;
	temp1->next = temp2->next;
	delete temp2;
	--count;
	return element;
}

void LinkedList::operator-=(int index)
{
	if(indexValid(index))
	{
		extract(index);
	}
}

LinkedList& LinkedList::operator=(LinkedList list)
{
	for (int i = 0; i < count; ++i)
	{
		extractHead();
	}
	Node* temp = list.head;
	for (Node* temp = list.head; temp != nullptr; temp = temp->next)
	{
		addToTail(temp->data);
	}
	return *this;
}

int LinkedList::indexOf(int element)
{
	Node* temp = head;
	for (int i = 0; i < count; ++i)
	{
		if(temp->data == element)
		{
			return i;
		}
		temp = temp->next;
	}
	return -1;
}

bool LinkedList::contains(int element)
{
	return indexOf(element);
}

/*
bool LinkedList::swap(int index1, int index2)
{
	if (!indexValid(index1) || !indexValid(index2))
	{
		return false;
	}
	Node* temp1 = head;
	Node* temp2 = head;
	for(int i = 0; i < index1; ++i)
	{
		temp1 = temp1->next;
	}
	for(int i = 0; i < index2; ++i)
	{
		temp2 = temp2->next;
	}
	


	return true;
}
*/
























