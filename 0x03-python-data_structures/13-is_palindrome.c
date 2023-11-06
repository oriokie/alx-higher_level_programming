#include "lists.h"
/**
 * reverse_list - function to reverse a linked list
 * @head: the pointer to the first node
 *
 * Return: the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *nxt = NULL;

	while (current != NULL)
	{
		nxt = current->next;
		current->next = prev;
		prev = current;
		current = nxt;
	}
	return (prev);
}
/**
 * is_palindrome - function to check if a linked list is a palindrome
 * @head: the pointer to the list
 *
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	slow = reverse_list(slow);

	while (slow != NULL)
	{
		if ((*head)->n != slow->n)
		{
			return (0);
		}

		*head = (*head)->next;
		slow = slow->next;
	}
	return (1);
}
