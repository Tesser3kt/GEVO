<script setup lang="ts">
import { ref } from 'vue'

const navLinks = ref([
  { title: 'Učitelé', path: '/teachers', icon: 'bi-people-fill' },
  { title: 'Kabinety', path: '/offices', icon: 'bi-door-closed-fill' },
  { title: 'Předměty', path: '/subjects', icon: 'bi-book-fill' }
])
</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-body-secondary bg-opacity-80 px-4">
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div id="navbarSupportedContent" class="collapse navbar-collapse justify-content-center">
        <ul class="navbar-nav my-2 my-lg-0 py-lg-2">
          <li class="nav-item" v-for="(link, index) in navLinks" :key="link.title">
            <router-link
              :to="link.path"
              class="nav-link px-3 py-0 mt-3 mt-lg-0"
              :class="{
                'border-start border-dark-subtle': index !== 0,
                active: $route.path === link.path
              }"
            >
              <i class="bi" :class="link.icon"></i>
              {{ link.title }}
            </router-link>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>
