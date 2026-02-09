<script setup lang="ts">
import { IconShoppingBag, IconBell, IconSearch } from '@tabler/icons-vue'
import Avatar from 'primevue/avatar'
import InputText from 'primevue/inputtext'
import Badge from 'primevue/badge'
</script>

<template>
    <header class="app-navbar">
        <div class="navbar-left">
            <IconShoppingBag :size="24" class="navbar-logo" />
            <span class="navbar-title">Shopping Lists</span>
        </div>

        <div class="navbar-center">
            <span class="p-input-icon-left search-wrapper">
                <IconSearch :size="18" class="search-icon" />
                <InputText placeholder="Search your lists..." class="search-input" />
            </span>
        </div>

        <div class="navbar-right">
            <div class="notification-wrapper">
                <IconBell :size="22" />
                <Badge value="3" severity="danger" class="notification-badge" />
            </div>
            <div class="user-info">
                <Avatar image="https://i.pravatar.cc/40?img=47" shape="circle" size="large" />
                <div class="user-details">
                    <span class="user-name">Jane Doe</span>
                    <span class="user-plan">Free Plan</span>
                </div>
            </div>
        </div>
    </header>
</template>

<style scoped>
.app-navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.75rem 2rem;
    background: var(--p-surface-0);
    border-bottom: 1px solid var(--p-surface-200);
}

.navbar-left {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.navbar-logo {
    color: var(--p-primary-color);
}

.navbar-title {
    font-size: 1.125rem;
    font-weight: 600;
    color: var(--p-surface-900);
}

.navbar-center {
    flex: 0 1 400px;
}

.search-wrapper {
    position: relative;
    display: flex;
    align-items: center;
    width: 100%;
}

.search-icon {
    position: absolute;
    left: 0.75rem;
    color: var(--p-surface-400);
    z-index: 1;
}

.search-input {
    width: 100%;
    padding-left: 2.5rem;
    border-radius: 2rem;
    background: var(--p-surface-100);
    border-color: var(--p-surface-200);
}

.navbar-right {
    display: flex;
    align-items: center;
    gap: 1.5rem;
}

.notification-wrapper {
    position: relative;
    cursor: pointer;
    color: var(--p-surface-600);
}

.notification-badge {
    position: absolute;
    top: -4px;
    right: -4px;
    font-size: 0.625rem;
    min-width: 1rem;
    height: 1rem;
}

.user-info {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.user-details {
    display: flex;
    flex-direction: column;
}

.user-name {
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--p-surface-900);
}

.user-plan {
    font-size: 0.75rem;
    color: var(--p-surface-500);
}
</style>
