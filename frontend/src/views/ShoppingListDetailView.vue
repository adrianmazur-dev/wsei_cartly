<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useShoppingListsStore } from '@/stores/shopping-lists'
import { useConfirm } from 'primevue/useconfirm'
import { IconArrowLeft, IconPlus, IconShare, IconTrash, IconChevronDown } from '@tabler/icons-vue'
import Checkbox from 'primevue/checkbox'
import ConfirmDialog from 'primevue/confirmdialog'

const route = useRoute()
const router = useRouter()
const store = useShoppingListsStore()
const confirm = useConfirm()

const listId = computed(() => route.params.id as string)
const newItemName = ref('')
const completedExpanded = ref(true)
const shareTooltip = ref(false)

onMounted(() => {
    store.fetchList(listId.value)
})

const activeItems = computed(() => store.currentList?.items.filter((i) => !i.is_checked) ?? [])
const completedItems = computed(() => store.currentList?.items.filter((i) => i.is_checked) ?? [])

const formattedDate = computed(() => {
    if (!store.currentList) return ''
    return new Date(store.currentList.created_at).toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
    })
})

async function handleAddItem() {
    const name = newItemName.value.trim()
    if (!name) return
    newItemName.value = ''
    await store.addItem(listId.value, name)
}

async function handleToggle(itemId: string) {
    const item = store.currentList?.items.find((i) => i.id === itemId)
    if (!item) return
    await store.toggleItem(listId.value, itemId, item)
}

async function handleDelete(itemId: string) {
    await store.deleteItem(listId.value, itemId)
}

async function handleDeleteList() {
    const hasItems = (store.currentList?.items?.length ?? 0) > 0

    if (hasItems) {
        confirm.require({
            message: 'This list contains items. Are you sure you want to delete it?',
            header: 'Delete list',
            rejectProps: {
                label: 'Cancel',
                severity: 'secondary',
                outlined: true,
            },
            acceptProps: {
                label: 'Delete',
                severity: 'danger',
            },
            accept: async () => {
                await store.deleteList(listId.value)
                router.push('/')
            },
        })
    } else {
        await store.deleteList(listId.value)
        router.push('/')
    }
}

async function handleShare() {
    await navigator.clipboard.writeText(window.location.href)
    shareTooltip.value = true
    setTimeout(() => (shareTooltip.value = false), 2000)
}
</script>

<template>
    <div class="list-detail" v-if="store.currentList">
        <header class="list-detail__header">
            <div class="list-detail__header-left">
                <router-link to="/" class="list-detail__back">
                    <IconArrowLeft :size="16" />
                    Back to Lists
                </router-link>
                <h1 class="list-detail__title">{{ store.currentList.name }}</h1>
                <p class="list-detail__meta">Created on {{ formattedDate }}</p>
            </div>
            <div class="list-detail__header-right">
                <button class="list-detail__share-btn" @click="handleShare">
                    <IconShare :size="18" />
                    <span>{{ shareTooltip ? 'Copied!' : 'Share' }}</span>
                </button>
                <button class="list-detail__delete-btn" @click="handleDeleteList">
                    <IconTrash :size="18" />
                    <span>Delete</span>
                </button>
            </div>
        </header>

        <div class="list-detail__card">
            <div class="list-detail__add-item">
                <IconPlus :size="24" class="list-detail__add-icon" />
                <input
                    v-model="newItemName"
                    type="text"
                    placeholder="Add a new item..."
                    class="list-detail__add-input"
                    @keydown.enter="handleAddItem"
                />
            </div>

            <div class="list-detail__items">
                <div v-for="item in activeItems" :key="item.id" class="list-detail__item">
                    <div class="list-detail__item-checkbox">
                        <Checkbox
                            :modelValue="item.is_checked"
                            :binary="true"
                            @update:modelValue="handleToggle(item.id)"
                        />
                    </div>
                    <div class="list-detail__item-info">
                        <p class="list-detail__item-name">{{ item.name }}</p>
                        <span class="list-detail__item-quantity">{{ item.quantity }} pcs</span>
                    </div>
                    <button class="list-detail__item-delete" @click="handleDelete(item.id)">
                        <IconTrash :size="20" />
                    </button>
                </div>
            </div>

            <div
                v-if="completedItems.length > 0"
                class="list-detail__completed-header"
                @click="completedExpanded = !completedExpanded"
            >
                <span>COMPLETED ITEMS ({{ completedItems.length }})</span>
                <IconChevronDown
                    :size="18"
                    :style="{
                        transform: completedExpanded ? 'rotate(0)' : 'rotate(-90deg)',
                        transition: 'transform 0.2s ease',
                    }"
                />
            </div>

            <div
                v-if="completedExpanded && completedItems.length > 0"
                class="list-detail__completed-items"
            >
                <div
                    v-for="item in completedItems"
                    :key="item.id"
                    class="list-detail__item list-detail__item--completed"
                >
                    <div class="list-detail__item-checkbox">
                        <Checkbox
                            :modelValue="item.is_checked"
                            :binary="true"
                            @update:modelValue="handleToggle(item.id)"
                        />
                    </div>
                    <div class="list-detail__item-info">
                        <p class="list-detail__item-name">{{ item.name }}</p>
                        <span class="list-detail__item-quantity">{{ item.quantity }} pcs</span>
                    </div>
                    <button class="list-detail__item-delete" @click="handleDelete(item.id)">
                        <IconTrash :size="20" />
                    </button>
                </div>
            </div>
        </div>
    </div>

    <div v-else-if="store.loading" class="list-detail__loading">Loading...</div>

    <ConfirmDialog />
</template>

<style scoped lang="scss" src="@/assets/styles/views/_shopping-list-detail.scss"></style>
