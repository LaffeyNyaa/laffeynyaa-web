import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AiChatView from '@/views/AiChatView.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeView,
    },
    {
        path: '/ai-chat',
        name: 'AiChat',
        component: AiChatView,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
