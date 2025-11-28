<template>
    <ChatUser
        v-for="(msg, index) in messages"
        :key="index"
        :username="msg.align === 'left' ? t('ai') : t('you')"
        :avatar-url="msg.align === 'left' ? defaultAvatar : defaultAvatar"
        :message="msg.message"
        :timestamp="msg.timestamp"
        :align="msg.align"
    />
    <ChatInput :placeholder="t('type_message')" @message-sent="addMessage" ref="chatInputRef" />
</template>

<script setup lang="ts">
import ChatUser from '@/components/ChatUser.vue'
import defaultAvatar from '@/assets/images/default-avatar.webp'
import ChatInput from '@/components/ChatInput.vue'
import { useI18n } from 'vue-i18n'
import { ref } from 'vue'

const { t } = useI18n()

interface Message {
    message: string
    timestamp: Date
    align: 'left' | 'right'
}

const messages = ref<Message[]>([])

const addMessage = (messageData: {
    message: string
    timestamp: Date
    align: 'left' | 'right'
    is_start: boolean
}) => {
    if (messageData.align === 'right') {
        messages.value.push({ ...messageData })
        return
    }

    if (messageData.is_start) {
        messages.value.push({ ...messageData })
        return
    }

    if (!messageData.is_start) {
        messages.value[messages.value.length - 1].message += messageData.message
    }
}
</script>
