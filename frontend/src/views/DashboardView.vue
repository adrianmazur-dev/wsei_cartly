<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useShoppingListsStore } from '@/stores/shopping-lists'
import ShoppingListCard from '@/components/ShoppingListCard.vue'
import CreateListCard from '@/components/CreateListCard.vue'
import CreateListDialog from '@/components/CreateListDialog.vue'
import Button from 'primevue/button'
import { IconLayoutGrid, IconList, IconAdjustmentsHorizontal, IconPlus } from '@tabler/icons-vue'

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
                    <span class="filter-btn-label">Filter</span>
                </Button>
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
