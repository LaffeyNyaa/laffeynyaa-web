<template>
    <footer>
        <slot></slot>
    </footer>
</template>

<script setup lang="ts"></script>

<style scoped lang="scss">
@use '../assets/styles/variables.scss' as *;

footer {
    display: flex;
    margin-top: $margin-size;
    padding: $padding-size;
    align-items: center;
    flex-direction: column;
    background-color: $theme-background-color;
    border-radius: 10px;
}
</style>
