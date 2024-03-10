<script setup lang="ts">
import TeacherCard from '@/components/TeacherCard.vue'
import { useTeachersStore } from '@/stores/teachers'

const store = useTeachersStore()

// Methods
const onDeleteTeacherClick = (id: number) => {
  store.deleteTeacher(id)
}
</script>

<template>
  <section class="main-container container mt-4">
    <div class="title-container container mx-auto text-center border-bottom border-tertiary">
      <h1 class="fs-2 mb-2 text-primary">Učitelé</h1>
    </div>
    <div class="teacher-cards-container container mt-4">
      <div class="teacher-cards-grid row row-cols-1 row-cols-lg-2 row-cols-xl-3 g-3 g-lg-4">
        <TeacherCard
          v-for="teacher in store.teachers"
          :key="teacher.id"
          :teacher="teacher"
          :onDeleteClick="onDeleteTeacherClick"
        />
      </div>
    </div>
  </section>
</template>
