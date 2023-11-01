#include "lists.h"
/**
 * check_cycle - a functin that checks if a singly linked list has a cycle
 * @list: the list to be checked
 *
 * Return: 1 if there is a cycle 0 if none exists
 */
int check_cycle(listint_t *list)
{
	listint_t *leopard;
	listint_t *tortoise;

	if (list == NULL)
		return (0);
	tortoise = list;
	leopard = list->next;
	while (toroise && leopard && leopard->next)
	{
		if (tortoise == leopard)
			return (1);
		tortoise = tortoise->next;
		leopard = leopard->next->next;
	}
	return (0);
}
