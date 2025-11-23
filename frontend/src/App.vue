<script setup lang="ts">
import Button from './components/ButtonPrimary.vue'
import Navbar from './components/NavbarTop.vue'
import ContainerCenter from './components/ContainerCenter.vue'
</script>

<template>
    <Navbar>
        <Button>Home</Button>
        <Button>AI Chat</Button>
    </Navbar>

    <ContainerCenter>
        <img src="./assets/images/miku-pay.gif" alt="" />
    </ContainerCenter>
</template>

<style scoped></style>
