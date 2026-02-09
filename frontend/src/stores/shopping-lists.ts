import { defineStore } from 'pinia'
import { ref } from 'vue'
import { cartlyClient } from '@/backend/cartly/client'
import type { components } from '@/backend/cartly/schema'

type ShoppingListResponse = components['schemas']['ShoppingListResponse']
type ItemResponse = components['schemas']['ItemResponse']

export interface ShoppingListWithItems extends ShoppingListResponse {
    items: ItemResponse[]
    totalItems: number
    checkedItems: number
    progress: number
}

export const useShoppingListsStore = defineStore('shopping-lists', () => {
    const lists = ref<ShoppingListWithItems[]>([])
    const loading = ref(false)
    const error = ref<string | null>(null)

    async function fetchLists() {
        loading.value = true
        error.value = null
        try {
            const { data } = await cartlyClient.GET('/shopping-lists/')
            if (!data) return

            const listsWithItems: ShoppingListWithItems[] = await Promise.all(
                data.map(async (list) => {
                    const { data: items } = await cartlyClient.GET(
                        '/shopping-lists/{list_id}/items/',
                        { params: { path: { list_id: list.id } } },
                    )
                    const listItems = items ?? []
                    const totalItems = listItems.length
                    const checkedItems = listItems.filter((i) => i.is_checked).length
                    return {
                        ...list,
                        items: listItems,
                        totalItems,
                        checkedItems,
                        progress:
                            totalItems > 0 ? Math.round((checkedItems / totalItems) * 100) : 0,
                    }
                }),
            )

            lists.value = listsWithItems
        } catch (e) {
            error.value = e instanceof Error ? e.message : 'Failed to fetch lists'
        } finally {
            loading.value = false
        }
    }

    async function createList(name: string, description?: string) {
        const { data } = await cartlyClient.POST('/shopping-lists/', {
            body: { name, description: description || null },
        })
        if (data) {
            await fetchLists()
        }
        return data
    }

    async function deleteList(id: string) {
        await cartlyClient.DELETE('/shopping-lists/{list_id}', {
            params: { path: { list_id: id } },
        })
        await fetchLists()
    }

    const currentList = ref<ShoppingListWithItems | null>(null)

    async function fetchList(id: string) {
        loading.value = true
        error.value = null
        try {
            const { data: list } = await cartlyClient.GET('/shopping-lists/{list_id}', {
                params: { path: { list_id: id } },
            })
            if (!list) return
            const { data: items } = await cartlyClient.GET('/shopping-lists/{list_id}/items/', {
                params: { path: { list_id: id } },
            })
            const listItems = items ?? []
            const totalItems = listItems.length
            const checkedItems = listItems.filter((i) => i.is_checked).length
            currentList.value = {
                ...list,
                items: listItems,
                totalItems,
                checkedItems,
                progress: totalItems > 0 ? Math.round((checkedItems / totalItems) * 100) : 0,
            }
        } catch (e) {
            error.value = e instanceof Error ? e.message : 'Failed to fetch list'
        } finally {
            loading.value = false
        }
    }

    async function addItem(listId: string, name: string, quantity: number = 1) {
        await cartlyClient.POST('/shopping-lists/{list_id}/items/', {
            params: { path: { list_id: listId } },
            body: { name, quantity },
        })
        await fetchList(listId)
    }

    async function toggleItem(listId: string, itemId: string, item: ItemResponse) {
        await cartlyClient.PUT('/shopping-lists/{list_id}/items/{item_id}', {
            params: { path: { item_id: itemId } },
            body: {
                name: item.name,
                quantity: item.quantity,
                is_checked: !item.is_checked,
                category_id: item.category_id,
            },
        })
        await fetchList(listId)
    }

    async function deleteItem(listId: string, itemId: string) {
        await cartlyClient.DELETE('/shopping-lists/{list_id}/items/{item_id}', {
            params: { path: { item_id: itemId } },
        })
        await fetchList(listId)
    }

    return {
        lists,
        loading,
        error,
        currentList,
        fetchLists,
        createList,
        deleteList,
        fetchList,
        addItem,
        toggleItem,
        deleteItem,
    }
})
