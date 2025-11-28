<template>
    <div class="container-content">
        <slot></slot>
    </div>
</template>

<style scoped lang="scss">
@use '@/assets/styles/variables.scss' as *;

.container-content {
    margin-top: $margin-size;
    padding: $padding-size;
    background-color: $theme-background-color;
    border-radius: 10px;
}
</style>
