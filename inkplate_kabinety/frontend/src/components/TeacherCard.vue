<script setup lang="ts">
import { ref, computed, nextTick } from 'vue'
import type { TeacherData } from '@/types/TeacherData'
import DeleteModal from '@/components/DeleteModal.vue'
import EditTeacherModal from '@/components/EditTeacherModal.vue'

// Props
const props = defineProps<{
  teacher: TeacherData
  onDeleteClick: (id: number) => void
}>()

// Refs
const renderEditForm = ref<boolean>(true)

// Computed
const teacherSubjects = computed(() => {
  let names = []
  for (let subject of props.teacher.subjects) {
    names.push(subject.name)
  }
  return names.join(', ')
})
const officeName = computed(() => {
  return props.teacher.office.name + ' (' + props.teacher.office.number + ')'
})
const imgSrc = computed(() => {
  return new URL(`../assets/imgs/${props.teacher.photo_file}.png`, import.meta.url).href
})

// Methods
const rerenderEditForm = async () => {
  await new Promise((resolve) => {
    setTimeout(resolve, 1000)
    renderEditForm.value = false
    nextTick(() => {
      renderEditForm.value = true
      resolve(true)
    })
  })
}
</script>

<template>
  <div class="col">
    <div class="teacher-card card border-primary border-2 border-opacity-25">
      <div class="row g-0">
        <div class="col-md-4">
          <div
            class="bg-image rounded-start w-100 h-100"
            :style="{
              'background-image': `url(${imgSrc})`,
              'background-position': 'center top',
              'background-size': 'cover'
            }"
          ></div>
        </div>
        <div class="col-md-8">
          <div class="card-body p-4">
            <h2
              class="card-title fs-4 mb-0 pb-2 border-tertiary-emphasis border-bottom text-primary-emphasis"
            >
              {{ teacher.name }}
            </h2>
            <p class="card-text mb-0 mt-2">{{ teacherSubjects }}</p>
            <p class="card-text">{{ officeName }}</p>
            <button
              class="btn btn-warning me-1"
              type="button"
              data-bs-toggle="modal"
              :data-bs-target="`#editModal-${props.teacher.id}`"
            >
              <i class="bi bi-pencil-fill"></i>
            </button>
            <button
              class="btn btn-danger ms-1"
              type="button"
              data-bs-toggle="modal"
              :data-bs-target="`#deleteModal-${props.teacher.id}`"
            >
              <i class="bi bi-x-circle-fill"></i>
            </button>

            <!-- Delete Modal -->
            <DeleteModal
              :id="props.teacher.id"
              title="Smazat učitele"
              :message="`Opravdu chcete smazat učitele ${teacher.name}?`"
              :onDeleteClick="onDeleteClick"
            />

            <!-- Edit Modal -->
            <EditTeacherModal
              v-if="renderEditForm"
              :teacher="props.teacher"
              @rerender="rerenderEditForm"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
