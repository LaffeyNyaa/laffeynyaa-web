<template>
    <div>
        <slot></slot>
    </div>
</template>

<script setup lang="ts"></script>

<style scoped lang="scss">
@use '../assets/styles/variables.scss' as *;

div {
    display: flex;
    margin-top: $margin-size;
    padding: $padding-size;
    justify-content: center;
    background-color: $theme-background-color;
    border-radius: 10px;
}
</style>
