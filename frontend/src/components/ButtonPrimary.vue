<template>
    <button class="button-primary">
        <slot></slot>
    </button>
</template>

<script setup lang="ts"></script>

<style scoped lang="scss">
@use '@/assets/styles/variables.scss' as *;

.button-primary {
    border: none;
    background-color: $button-default-background-color;
    border-radius: 5px;
    box-shadow: 0 3px 10px $shadow-color;
    transition: background-color $transition-duration ease;
    padding: 10px 20px;
    font-size: 16px;
    width: 90px;

    &:hover {
        background-color: $button-hover-background-color;
    }

    &:active {
        background-color: $button-active-background-color;
    }
}
</style>
