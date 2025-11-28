<template>
    <nav class="navbar-top">
        <slot></slot>
    </nav>
</template>

<style scoped lang="scss">
@use '@/assets/styles/variables.scss' as *;

.navbar-top {
    display: flex;
    gap: 10px;
    padding: $padding-size;
    justify-content: center;
    background-color: $theme-background-color;
    border-radius: 10px;
}
</style>
