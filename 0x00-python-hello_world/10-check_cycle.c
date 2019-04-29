#include "lists.h"

/**
 * check_cycle - function that checks if a single list has a cycle.
 * @list: List that cames to be checked
 *
 * Return: 0 if it is a simple list, 1 if it is not
 */

int check_cycle(listint_t *list)
{
	listint_t *x;
	listint_t *y;

	if (!list)
		return (0);
	x = list;
	y = list->next;
	while (x != y)
	{
		x = x->next;
		if (!x)
			return (0);
		y = y->next;
		if (!y)
			return (0);
		y = y->next;
		if (!y)
			return (0);

	}
	return (1);
}
