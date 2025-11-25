<template>
    <ContainerContent>
        <h1>{{ t('ai_chat') }}</h1>
    </ContainerContent>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n'
import ContainerContent from '../components/ContainerContent.vue'

const { t } = useI18n()
</script>
