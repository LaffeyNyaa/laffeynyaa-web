<template>
    <div class="chat-user" :class="`align-${align}`" :style="{ opacity: isVisible ? 1 : 0 }">
        <img :src="avatarUrl" :alt="username" class="avatar" />

        <div class="content-container">
            <span class="username">{{ username }}</span>
            <span class="timestamp">{{ formatTime(timestamp) }}</span>
            <p class="message-content">{{ message }}</p>
        </div>
    </div>
</template>

<script setup lang="ts">
import defaultAvatar from '@/assets/images/default-avatar.webp'
import { nextTick, onMounted, ref } from 'vue'

interface Props {
    username: string
    avatarUrl: string
    message: string
    timestamp: Date
    align: 'left' | 'right'
}

withDefaults(defineProps<Props>(), {
    username: 'Anonymous',
    avatarUrl: defaultAvatar,
    message: '',
    timestamp: () => new Date(),
    align: 'left',
})

const isVisible = ref(false)

onMounted(() => {
    nextTick(() => {
        isVisible.value = true
    })
})

const formatTime = (time: Date): string => {
    if (!time) {
        return ''
    }

    const date = new Date(time)
    const now = new Date()

    if (date.toDateString() === now.toDateString()) {
        return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    }

    return date.toLocaleDateString([], { month: 'short', day: 'numeric' })
}
</script>

<style scoped lang="scss">
@use '@/assets/styles/variables.scss' as *;

.chat-user {
    display: flex;
    padding: $padding-size;
    gap: 10px;
    transition: all $transition-duration ease;

    &:hover {
        background-color: #e0e0e081;
    }

    &.align-left {
        margin-right: 20%;
    }

    &.align-right {
        flex-direction: row-reverse;
        margin-left: 20%;

        .content-container {
            align-items: flex-end;
        }
    }
}

.avatar {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    object-fit: cover;
    box-shadow: 0 3px 10px $shadow-color;
}

.username {
    font-weight: 600;
    color: #00ffff;
    margin-right: 8px;
}

.timestamp {
    font-size: 0.75rem;
    color: #494949;
}

.message-content {
    margin: 0;
}

.content-container {
    display: flex;
    flex-direction: column;
}
</style>
