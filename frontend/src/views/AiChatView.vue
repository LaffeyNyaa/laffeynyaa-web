<template>
    <ContainerCenter>
        <h1>{{ t('ai_chat') }}</h1>
    </ContainerCenter>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n'
import ContainerCenter from '../components/ContainerContent.vue'

const { t } = useI18n()
</script>
