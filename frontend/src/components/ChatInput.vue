<template>
    <input
        class="chat-input"
        :placeholder="placeholder"
        @keyup.enter="sendMessage"
        v-model="inputText"
    />
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface Props {
    placeholder: string
}

withDefaults(defineProps<Props>(), {
    placeholder: '',
})

const inputText = ref('')
const emit = defineEmits(['message-sent'])
const item = ref({
    messages: [
        {
            role: 'system',
            content:
                '你是一个有帮助的助手，需要提供精准、高效且富有洞察力的回应，随时准备协助用户处理各种任务与问题。',
        },
    ],
})

const sendMessage = async () => {
    if (!inputText.value.trim()) {
        return
    }

    emit('message-sent', {
        message: inputText.value,
        timestamp: new Date(),
        align: 'right',
        is_start: true,
    })

    item.value.messages.push({
        role: 'user',
        content: inputText.value,
    })

    inputText.value = ''

    const response = await fetch('http://localhost:8000/api/chat/response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(item.value),
    })

    if (!response.body) {
        throw new Error('Network response was not ok')
    }

    const reader = response.body.getReader()
    const decoder = new TextDecoder('utf-8')

    let done = false

    const aiMessageData = {
        message: '',
        timestamp: new Date(),
        align: 'left',
        is_start: true,
    }

    emit('message-sent', aiMessageData)

    aiMessageData.is_start = false

    while (!done) {
        const { value, done: readerDone } = await reader.read()
        done = readerDone

        if (value) {
            const chunk = decoder.decode(value, { stream: true })
            aiMessageData.message = chunk
            emit('message-sent', aiMessageData)
        }
    }

    item.value.messages.push({
        role: 'assistant',
        content: aiMessageData.message,
    })
}
</script>

<style scoped lang="scss">
@use '@/assets/styles/variables.scss' as *;

.chat-input {
    display: flex;
    padding: $padding-size;
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    margin-top: $margin-size;
    transition: background-color $transition-duration ease;
    background-color: $input-background-color;
    box-shadow: 0 3px 10px $shadow-color;
    outline: none;

    &:focus {
        background-color: $input-active-color;
    }
}
</style>
