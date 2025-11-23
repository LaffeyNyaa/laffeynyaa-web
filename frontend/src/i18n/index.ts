import { createI18n } from 'vue-i18n'
import zh from '../locales/zh.json'
import en from '../locales/en.json'

const messages = {
    zh: zh,
    en: en
}

const i18n = createI18n({
    legacy: false,
    locale: localStorage.getItem('locale') || 'zh',
    fallbackLocale: 'en',
    messages
})

export default i18n