<script setup lang="ts">
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const router = useRouter()

if (userStore.isAuthenticated && userStore.isAdmin) {
  router.push('/teachers')
}
</script>

<template>
  <main>
    <div><h2>This is a login page!</h2></div>
  </main>
</template>
