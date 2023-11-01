#include "lists.h"
/**
 * insert_node - function that inserts a number into a sorted singly
 * linked list
 * @head: start point
 * @number: the number to be addded
 *
 * Return: address of the new node or NULL for failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL || number < current_node->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (current_node->next && number >= current_node->next->n)
	{
		current_node = current_node->next;
	}

	new_node->next = current_node->next;
	current_node->next = new_node;

	return (new_node);
}
