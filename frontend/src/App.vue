<script setup lang="ts">
import Button from './components/ButtonPrimary.vue'
import Navbar from './components/NavbarTop.vue'
import FooterBottom from './components/FooterCopyright.vue'
import LanguageSwitch from './components/LanguageSwitch.vue'
import ContainerContent from './components/ContainerContent.vue'
import { useI18n } from 'vue-i18n'
import { useRouter } from 'vue-router'

const { t } = useI18n()
const router = useRouter()
</script>

<template>
    <div class="grid-container">
        <Navbar class="navbar">
            <Button @click="router.push('/')">{{ t('home') }}</Button>
            <Button @click="router.push('/ai-chat')">{{ t('ai_chat') }}</Button>
            <LanguageSwitch />
        </Navbar>

        <ContainerContent class="container-content">
            <RouterView />
        </ContainerContent>

        <FooterBottom class="footer-bottom">
            <p>Copyright (c) 2025 LaffeyNyaa</p>
            <a href="https://beian.miit.gov.cn/" target="_blank">津ICP备2024026458号-1</a>
        </FooterBottom>
    </div>
</template>

<style scoped>
.grid-container {
    display: grid;
    grid-template-areas:
        'navbar'
        'content'
        'footer';
    grid-template-rows: auto 1fr auto;
    height: 98vh;
}

.navbar {
    grid-area: navbar;
}

.container-content {
    grid-area: content;
}

.footer-bottom {
    grid-area: footer;
}
</style>
