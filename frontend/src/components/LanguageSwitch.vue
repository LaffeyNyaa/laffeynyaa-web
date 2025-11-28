<template>
    <ButtonPrimary @click="switchLanguage">文/A</ButtonPrimary>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n'
import ButtonPrimary from './ButtonPrimary.vue'

const { locale } = useI18n()

const switchLanguage = () => {
    locale.value = locale.value === 'zh' ? 'en' : 'zh'
    localStorage.setItem('locale', locale.value)
}
</script>
