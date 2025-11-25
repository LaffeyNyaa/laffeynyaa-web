<template>
    <ContainerContent>
        <ChatUser
            username="千问"
            :avatar-url="defaultAvatar"
            message="你好喵"
            :timestamp="new Date()"
            align="left"
        />
        <ChatUser
            username="千问"
            :avatar-url="defaultAvatar"
            message="你好喵"
            :timestamp="new Date()"
            align="right"
        />
    </ContainerContent>
</template>

<script setup lang="ts">
import ContainerContent from '@/components/ContainerContent.vue'
import ChatUser from '@/components/ChatUser.vue'
import defaultAvatar from '@/assets/images/default-avatar.webp'
</script>
