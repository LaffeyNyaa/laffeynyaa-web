<script setup lang="ts">
import Button from './components/ButtonPrimary.vue'
import Navbar from './components/NavbarTop.vue'
import ContainerCenter from './components/ContainerContent.vue'
import FooterBottom from './components/FooterCopyright.vue'
import LanguageSwitch from './components/LanguageSwitch.vue'
import {useI18n} from 'vue-i18n'

const {t} = useI18n()
</script>

<template>
    <Navbar>
        <Button>{{ t('home') }}</Button>
        <Button>{{ t('ai_chat') }}</Button>
        <LanguageSwitch />
    </Navbar>

    <ContainerCenter>
        <img src="./assets/images/miku-pay.gif" alt="" />
    </ContainerCenter>

    <FooterBottom>
        <p>Copyright (c) 2025 LaffeyNyaa</p>
        <a href="https://beian.miit.gov.cn/" target="_blank">津ICP备2024026458号-1</a>
    </FooterBottom>
</template>

<style scoped></style>
