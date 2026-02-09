<script setup lang="ts">
import type { ShoppingListWithItems } from '@/stores/shopping-lists'
import { computed } from 'vue'
import {
    IconShoppingCart,
    IconTools,
    IconDeviceGamepad2,
    IconBriefcase,
    IconBox,
    IconDots,
} from '@tabler/icons-vue'
import ProgressBar from 'primevue/progressbar'
import Avatar from 'primevue/avatar'
import AvatarGroup from 'primevue/avatargroup'
import Button from 'primevue/button'

const props = defineProps<{
    list: ShoppingListWithItems
}>()

const categoryIcons = [IconShoppingCart, IconTools, IconDeviceGamepad2, IconBriefcase, IconBox]
const categoryColors = ['#6366f1', '#f97316', '#06b6d4', '#22c55e', '#8b5cf6']

const iconIndex = computed(() => {
    let hash = 0
    for (const ch of props.list.id) hash = (hash << 5) - hash + ch.charCodeAt(0)
    return Math.abs(hash) % categoryIcons.length
})

const IconComponent = computed(() => categoryIcons[iconIndex.value])
const iconBgColor = computed(() => categoryColors[iconIndex.value])

const progressColor = computed(() => {
    if (props.list.progress === 100) return '#22c55e'
    if (props.list.progress < 25) return '#f97316'
    return '#6366f1'
})

const itemPreview = computed(() => {
    const names = props.list.items.slice(0, 4).map((i) => i.name)
    return names.length > 0 ? names.join(', ') + (props.list.items.length > 4 ? '...' : '') : ''
})

const timeAgo = computed(() => {
    const updated = new Date(props.list.updated_at)
    const now = new Date()
    const diffMs = now.getTime() - updated.getTime()
    const diffMins = Math.floor(diffMs / 60000)
    if (diffMins < 1) return 'Just now'
    if (diffMins < 60) return `Edited ${diffMins}m ago`
    const diffHours = Math.floor(diffMins / 60)
    if (diffHours < 24) return `Edited ${diffHours}h ago`
    const diffDays = Math.floor(diffHours / 24)
    if (diffDays < 7) return `Edited ${diffDays}d ago`
    const diffWeeks = Math.floor(diffDays / 7)
    return `Edited ${diffWeeks}w ago`
})

const mockAvatars = computed(() => {
    const count = (Math.abs(iconIndex.value) % 3) + 1
    return Array.from(
        { length: count },
        (_, i) => `https://i.pravatar.cc/32?img=${iconIndex.value * 10 + i + 1}`,
    )
})
</script>

<template>
    <div class="shopping-list-card">
        <div class="card-header">
            <div
                class="category-icon"
                :style="{ backgroundColor: iconBgColor + '15', color: iconBgColor }"
            >
                <component :is="IconComponent" :size="24" />
            </div>
            <Button text rounded class="menu-btn">
                <IconDots :size="20" />
            </Button>
        </div>

        <h3 class="card-title">{{ list.name }}</h3>
        <p class="card-preview">{{ itemPreview || list.description || 'No items yet' }}</p>

        <div class="card-progress">
            <div class="progress-info">
                <span class="progress-count"
                    >{{ list.checkedItems }}/{{ list.totalItems }} items</span
                >
                <span class="progress-percent" :style="{ color: progressColor }"
                    >{{ list.progress }}%</span
                >
            </div>
            <ProgressBar
                :value="list.progress"
                :showValue="false"
                :style="{ height: '6px' }"
                :pt="{ value: { style: { backgroundColor: progressColor } } }"
            />
        </div>

        <div class="card-footer">
            <AvatarGroup>
                <Avatar
                    v-for="(src, i) in mockAvatars"
                    :key="i"
                    :image="src"
                    shape="circle"
                    size="small"
                />
            </AvatarGroup>
            <span class="time-ago">{{ timeAgo }}</span>
        </div>
    </div>
</template>

<style scoped>
.shopping-list-card {
    background: var(--p-surface-0);
    border: 1px solid var(--p-surface-200);
    border-radius: 12px;
    padding: 1.25rem;
    cursor: pointer;
    transition:
        box-shadow 0.2s,
        transform 0.2s;
}

.shopping-list-card:hover {
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    transform: translateY(-2px);
}

.card-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 1rem;
}

.category-icon {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.menu-btn {
    color: var(--p-surface-400);
}

.card-title {
    font-size: 1rem;
    font-weight: 600;
    color: var(--p-surface-900);
    margin: 0 0 0.25rem 0;
}

.card-preview {
    font-size: 0.8125rem;
    color: var(--p-surface-500);
    margin: 0 0 1rem 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.card-progress {
    margin-bottom: 1rem;
}

.progress-info {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.375rem;
}

.progress-count {
    font-size: 0.8125rem;
    color: var(--p-surface-700);
}

.progress-percent {
    font-size: 0.8125rem;
    font-weight: 600;
}

.card-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.time-ago {
    font-size: 0.75rem;
    color: var(--p-surface-400);
}
</style>
