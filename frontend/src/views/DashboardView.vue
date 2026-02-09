<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useShoppingListsStore } from '@/stores/shopping-lists'
import ShoppingListCard from '@/components/ShoppingListCard.vue'
import CreateListCard from '@/components/CreateListCard.vue'
import CreateListDialog from '@/components/CreateListDialog.vue'

const store = useShoppingListsStore()
const showCreateDialog = ref(false)

onMounted(() => {
    store.fetchLists()
})
</script>

<template>
    <div class="dashboard">
        <div class="dashboard-header">
            <div>
                <h1 class="dashboard-title">Dashboard</h1>
                <p class="dashboard-subtitle">Manage your shopping needs and track progress.</p>
            </div>
        </div>

        <div class="cards-grid">
            <ShoppingListCard v-for="list in store.lists" :key="list.id" :list="list" />
            <CreateListCard @create="showCreateDialog = true" />
        </div>

        <CreateListDialog v-model:visible="showCreateDialog" />

        <button class="fab" aria-label="Create new list" @click="showCreateDialog = true">
            <IconPlus :size="28" />
        </button>
    </div>
</template>

<style scoped lang="scss" src="@/assets/styles/views/_dashboard.scss"></style>
