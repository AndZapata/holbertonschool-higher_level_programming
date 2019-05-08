#include "lists.h"

/**
 * is_palindrome - Function that checks if a list is palindrome
 * @head: Head of the single list
 *
 * Return: 0 if failed, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux;
	int array[1000000];
	int i, j;

	if (!head)
		return (0);
	aux = *head;
	for (i = 0; aux != NULL; i++)
	{
		array[i] = aux->n;
		aux = aux->next;
	}
	i--;
	for (j = 0; j < i; j++, i--)
	{
		if (array[i] != array[j])
			return (0);
	}
	return (1);
}
