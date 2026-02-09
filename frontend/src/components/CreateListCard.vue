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

<style scoped lang="scss" src="@/assets/styles/components/_create-list-card.scss"></style>
