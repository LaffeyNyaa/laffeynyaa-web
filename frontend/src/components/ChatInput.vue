<template>
    <input class="chat-input" :placeholder="placeholder" @keyup.enter="sendMessage" />
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n'
import axios from 'axios'

const { t } = useI18n()

interface Props {
    placeholder: string
}

withDefaults(defineProps<Props>(), {
    placeholder: '',
})

const sendMessage = async () => {
    console.log("sending")
    const item = {
        messages: [
            { "role": "system", "content": "你是一个有帮助的助手，需要提供精准、高效且富有洞察力的回应，随时准备协助用户处理各种任务与问题。" },
            { "role": "user", "content": "你是谁？" }
        ]
    }
    const response = await axios.post('http://localhost:8000/api/chat/response', item)

    console.log(response)
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
