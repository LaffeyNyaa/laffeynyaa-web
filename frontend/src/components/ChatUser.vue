<template>
    <div class="chat-user" :class="`align-${align}`">
        <img :src="avatarUrl" :alt="username" class="avatar" />

        <div>
            <span class="username">{{ username }}</span>
            <span class="timestamp">{{ formatTime(timestamp) }}</span>
            <p class="message-content">{{ message }}</p>
        </div>
    </div>
</template>

<script setup lang="ts">
import defaultAvatar from '@/assets/images/default-avatar.webp'

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
.chat-user {
    display: flex;
    gap: 12px;
    padding: 8px 16px;
    transition: background-color 0.2s ease;

    &:hover {
        background-color: #e0e0e081;
    }

    &.align-left {
        margin-right: 20%;
    }

    &.align-right {
        flex-direction: row-reverse;
        margin-left: 20%;
    }
}

.avatar {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    object-fit: cover;
}

.username {
    font-weight: 600;
    color: #00ffff;
    margin-right: 8px;
}

.timestamp {
    font-size: 0.75rem;
    color: #c0c0c0;
}

.message-content {
    margin: 0;
}
</style>
