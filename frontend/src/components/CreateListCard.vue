<script setup lang="ts">
import { IconPlus } from '@tabler/icons-vue'

defineEmits<{
    create: []
}>()
</script>

<template>
    <div class="create-list-card" @click="$emit('create')">
        <div class="create-icon">
            <IconPlus :size="32" />
        </div>
        <h3 class="create-title">Create New List</h3>
        <p class="create-subtitle">Start a new collection for your shopping needs</p>
    </div>
</template>

<style scoped>
.create-list-card {
    border: 2px dashed var(--p-surface-300);
    border-radius: 12px;
    padding: 1.25rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 220px;
    cursor: pointer;
    transition:
        border-color 0.2s,
        background 0.2s;
}

.create-list-card:hover {
    border-color: var(--p-primary-color);
    background: var(--p-primary-50);
}

.create-icon {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: var(--p-surface-100);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--p-surface-500);
    margin-bottom: 0.75rem;
}

.create-title {
    font-size: 1rem;
    font-weight: 600;
    color: var(--p-surface-900);
    margin: 0 0 0.25rem 0;
}

.create-subtitle {
    font-size: 0.8125rem;
    color: var(--p-surface-500);
    margin: 0;
    text-align: center;
}
</style>
