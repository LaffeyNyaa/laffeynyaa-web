<script setup lang="ts">
import Button from './components/ButtonPrimary.vue'
import Navbar from './components/NavbarTop.vue'
import FooterBottom from './components/FooterCopyright.vue'
import LanguageSwitch from './components/LanguageSwitch.vue'
import { useI18n } from 'vue-i18n'
import { useRouter } from 'vue-router'

const { t } = useI18n()
const router = useRouter()
</script>

<template>
    <Navbar>
        <Button @click="router.push('/')">{{ t('home') }}</Button>
        <Button @click="router.push('/ai-chat')">{{ t('ai_chat') }}</Button>
        <LanguageSwitch />
    </Navbar>

    <RouterView />

    <FooterBottom>
        <p>Copyright (c) 2025 LaffeyNyaa</p>
        <a href="https://beian.miit.gov.cn/" target="_blank">津ICP备2024026458号-1</a>
    </FooterBottom>
</template>

<style scoped></style>
