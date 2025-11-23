<template>
    <button @click="switchLanguage">
        文/A
    </button>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n'

const { locale, t } = useI18n()

const switchLanguage = () => {
    locale.value = locale.value === 'zh' ? 'en' : 'zh'
    localStorage.setItem('locale', locale.value)
}
</script>

<style scoped lang="scss">
@use '../assets/styles/variables.scss' as *;

button {
    border: none;
    background-color: $button-primary-default-background-color;
    border-radius: 5px;
    box-shadow: 0 3px 10px lightgrey;
    transition: background-color 0.2s ease;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    width: 90px;
}

button:hover {
    background-color: $button-primary-hover-background-color;
}

button:active {
    background-color: $button-primary-active-background-color;
}
</style>