<script setup lang="ts">
import type { ShoppingListWithItems } from '@/stores/shopping-lists'
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
import {
    IconShoppingCart,
    IconTools,
    IconDeviceGamepad2,
    IconBriefcase,
    IconBox,
    IconDots,
} from '@tabler/icons-vue'
import ProgressBar from 'primevue/progressbar'
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
</script>

<template>
    <div
        class="shopping-list-card"
        style="cursor: pointer"
        @click="router.push({ name: 'list-detail', params: { id: list.id } })"
    >
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
            <span class="time-ago">{{ timeAgo }}</span>
        </div>
    </div>
</template>

<style scoped lang="scss" src="@/assets/styles/components/_shopping-list-card.scss"></style>
