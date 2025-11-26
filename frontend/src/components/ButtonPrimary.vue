<template>
    <button>
        <slot></slot>
    </button>
</template>

<script setup lang="ts"></script>

<style scoped lang="scss">
@use '@/assets/styles/variables.scss' as *;

button {
    border: none;
    background-color: $button-default-background-color;
    border-radius: 5px;
    box-shadow: 0 3px 10px $shadow-color;
    transition: background-color $transition-duration ease;
    padding: 10px 20px;
    font-size: 16px;
    width: 90px;
}

button:hover {
    background-color: $button-hover-background-color;
}

button:active {
    background-color: $button-active-background-color;
}
</style>
