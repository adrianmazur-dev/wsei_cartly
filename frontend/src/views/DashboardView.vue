<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useShoppingListsStore } from '@/stores/shopping-lists'
import ShoppingListCard from '@/components/ShoppingListCard.vue'
import CreateListCard from '@/components/CreateListCard.vue'
import CreateListDialog from '@/components/CreateListDialog.vue'
import Button from 'primevue/button'
import { IconLayoutGrid, IconList, IconAdjustmentsHorizontal } from '@tabler/icons-vue'

const store = useShoppingListsStore()
const showCreateDialog = ref(false)
const viewMode = ref<'grid' | 'list'>('grid')

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
            <div class="dashboard-actions">
                <div class="view-toggle">
                    <Button
                        text
                        rounded
                        :class="{ active: viewMode === 'grid' }"
                        @click="viewMode = 'grid'"
                    >
                        <IconLayoutGrid :size="20" />
                    </Button>
                    <Button
                        text
                        rounded
                        :class="{ active: viewMode === 'list' }"
                        @click="viewMode = 'list'"
                    >
                        <IconList :size="20" />
                    </Button>
                </div>
                <Button outlined>
                    <IconAdjustmentsHorizontal :size="18" />
                    <span style="margin-left: 0.5rem">Filter</span>
                </Button>
            </div>
        </div>

        <div class="cards-grid">
            <ShoppingListCard v-for="list in store.lists" :key="list.id" :list="list" />
            <CreateListCard @create="showCreateDialog = true" />
        </div>

        <CreateListDialog v-model:visible="showCreateDialog" />
    </div>
</template>

<style scoped>
.dashboard-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 1.5rem;
}

.dashboard-title {
    font-size: 1.75rem;
    font-weight: 700;
    color: var(--p-surface-900);
    margin: 0;
}

.dashboard-subtitle {
    font-size: 0.875rem;
    color: var(--p-surface-500);
    margin: 0.25rem 0 0 0;
}

.dashboard-actions {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.view-toggle {
    display: flex;
    background: var(--p-surface-100);
    border-radius: 8px;
    padding: 2px;
}

.view-toggle :deep(.p-button) {
    color: var(--p-surface-400);
}

.view-toggle :deep(.p-button.active) {
    color: var(--p-surface-900);
    background: var(--p-surface-0);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.cards-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.25rem;
}

@media (max-width: 1200px) {
    .cards-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}

@media (max-width: 900px) {
    .cards-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 600px) {
    .cards-grid {
        grid-template-columns: 1fr;
    }
}
</style>
