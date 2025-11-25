<template>
    <div>
        <slot></slot>
    </div>
</template>

<script setup lang="ts"></script>

<style scoped lang="scss">
@use '../assets/styles/variables.scss' as *;

div {
    margin-top: $margin-size;
    padding: $padding-size;
    background-color: $theme-background-color;
    border-radius: 10px;
}
</style>
