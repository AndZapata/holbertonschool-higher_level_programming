#include "lists.h"
/**
 * insert_node - insert a new node in the position given
 * @head: elements to print
 * @number: data
 *
 * Return: The numbers of nodes
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node, *idx;

	idx = *head;
	while (idx->next != NULL && idx->next->n < number)
		idx = idx->next;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (idx == NULL)
		return (new_node);
	if (idx == 0)
	{
		new_node->next = idx;
		idx = new_node;
		return (new_node);
	}
	current_node = idx;
	while (number < idx->n)
	{
		if (current_node == NULL)
		{
			free(new_node);
			return (NULL);
		}
		current_node = current_node->next;
		idx--;
	}
	new_node->next = current_node->next;
	current_node->next = new_node;
	return (new_node);
}
