<script setup lang="ts">
import { IconBell, IconSearch } from '@tabler/icons-vue'
import Avatar from 'primevue/avatar'
import InputText from 'primevue/inputtext'
import Badge from 'primevue/badge'
import CartlyLogo from '@/assets/images/logo.svg'
</script>

<template>
    <header class="app-navbar">
        <div class="navbar-left">
            <CartlyLogo class="navbar-logo" />
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

<style scoped lang="scss" src="@/assets/styles/components/_navbar.scss"></style>
