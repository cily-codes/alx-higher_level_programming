#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: the singly linked list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;
	int check = 0;

	while ((slow && fast) && fast->next)
	{		
		slow = slow->next;

		if (fast->next || fast->next->next)
		{	
			fast = fast->next->next;
		}
		else
		{
			break;
		}

		if (slow == fast)
		{
			check = 1;
			break;
		}
	}

	return (check);
}
