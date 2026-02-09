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

<style scoped lang="scss" src="@/assets/styles/layout.scss"></style>
