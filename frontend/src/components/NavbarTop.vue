<template>
    <nav>
        <slot></slot>
    </nav>
</template>

<script setup lang="ts"></script>

<style scoped lang="scss">
@use '../assets/styles/variables.scss' as *;

nav {
    display: flex;
    gap: 10px;
    padding: 20px;
    justify-content: center;
    background-color: $navbar-top-background-color;
    border-radius: 10px;
}
</style>
