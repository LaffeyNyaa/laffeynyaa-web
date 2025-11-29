<template>
    <div class="chat-container">
        <div class="chat-user-container" ref="chatContainerRef">
            <ChatUser
                class="chat-user"
                :username="t('ai')"
                :avatar-url="defaultAvatar"
                :timestamp="new Date()"
                align="left"
                :message="t('welcome_message')"
            />
            <ChatUser
                v-for="(msg, index) in messages"
                :key="index"
                :username="msg.align === 'left' ? t('ai') : t('you')"
                :avatar-url="msg.align === 'left' ? defaultAvatar : defaultAvatar"
                :message="msg.message"
                :timestamp="msg.timestamp"
                :align="msg.align"
            />
        </div>
        <ChatInput
            class="chat-input"
            :placeholder="t('type_message')"
            @message-sent="addMessage"
            ref="chatInputRef"
        />
    </div>
</template>

<script setup lang="ts">
import ChatUser from '@/components/ChatUser.vue'
import defaultAvatar from '@/assets/images/default-avatar.webp'
import ChatInput from '@/components/ChatInput.vue'
import { useI18n } from 'vue-i18n'
import { nextTick, ref } from 'vue'

const { t } = useI18n()

interface Message {
    message: string
    timestamp: Date
    align: 'left' | 'right'
}

const messages = ref<Message[]>([])
const chatContainerRef = ref<HTMLDivElement>()

const scrollToBottom = () => {
    nextTick(() => {
        if (chatContainerRef.value) {
            chatContainerRef.value.scrollTop = chatContainerRef.value.scrollHeight
        }
    })
}

const addMessage = (messageData: {
    message: string
    timestamp: Date
    align: 'left' | 'right'
    is_start: boolean
}) => {
    if (messageData.align === 'right') {
        messages.value.push({ ...messageData })
    } else if (messageData.is_start) {
        messages.value.push({ ...messageData })
    } else {
        messages.value[messages.value.length - 1].message += messageData.message
    }

    scrollToBottom()
}
</script>

<style scoped lang="scss">
.chat-container {
    display: grid;
    grid-template-areas:
        'main'
        'input';
    grid-template-rows: 1fr auto;
    height: calc(100vh - 300px);
}

.chat-input {
    grid-area: input;
}

.chat-user-container {
    grid-area: main;
    overflow-y: auto;
}
</style>
