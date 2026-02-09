<script setup lang="ts">
import AppNavbar from '@/components/AppNavbar.vue'
</script>

<template>
    <div class="app-layout">
        <AppNavbar />
        <main class="app-main">
            <router-view />
        </main>
    </div>
</template>

<style scoped>
.app-layout {
    min-height: 100vh;
    background: var(--p-surface-50);
}

.app-main {
    max-width: 1400px;
    margin: 0 auto;
    padding: 2rem;
}
</style>
