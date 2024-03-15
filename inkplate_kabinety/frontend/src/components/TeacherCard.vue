<script setup lang="ts">
import { toRefs, computed, nextTick } from 'vue'
import { sleep } from '@/utils/sleep'
import type { TeacherData } from '@/types/TeacherData'
import DeleteModal from '@/components/DeleteModal.vue'
import EditTeacherModal from '@/components/EditTeacherModal.vue'

// Props
const props = defineProps<{
  teacher: TeacherData
  onDeleteClick: (id: number) => void
}>()

// Refs
const { id, name, photo_file, office, subjects } = toRefs(props.teacher)

// Computed
const teacherSubjects = computed(() => {
  let names = []
  for (let subject of subjects.value) {
    names.push(subject.name)
  }
  return names.join(', ')
})
const officeName = computed(() => {
  return office.value.name + ' (' + office.value.number + ')'
})
const imgSrc = computed(() => {
  return new URL(`../assets/imgs/${photo_file.value}.png`, import.meta.url).href
})
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
              {{ name }}
            </h2>
            <p class="card-text mb-0 mt-2">{{ teacherSubjects }}</p>
            <p class="card-text">{{ officeName }}</p>
            <button
              class="btn btn-warning me-1"
              type="button"
              data-bs-toggle="modal"
              :data-bs-target="`#editModal-${id}`"
            >
              <i class="bi bi-pencil-fill"></i>
            </button>
            <button
              class="btn btn-danger ms-1"
              type="button"
              data-bs-toggle="modal"
              :data-bs-target="`#deleteModal-${id}`"
            >
              <i class="bi bi-x-circle-fill"></i>
            </button>

            <!-- Delete Modal -->
            <DeleteModal
              :id="id"
              title="Smazat učitele"
              :message="`Opravdu chcete smazat učitele ${name}?`"
              :onDeleteClick="onDeleteClick"
            />

            <!-- Edit Modal -->
            <EditTeacherModal
              :id="id"
              :name="name"
              :photo_file="photo_file"
              :office="office"
              :subjects="subjects"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
