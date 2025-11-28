<template>
    <footer class="footer-copyright">
        <slot></slot>
    </footer>
</template>

<style scoped lang="scss">
@use '@/assets/styles/variables.scss' as *;

.footer-copyright {
    display: flex;
    margin-top: $margin-size;
    padding: $padding-size;
    align-items: center;
    flex-direction: column;
    background-color: $theme-background-color;
    border-radius: 10px;
}
</style>
