<script setup lang="ts">
import { ref, computed } from 'vue'
import type { OfficeData } from '@/types/OfficeData'
import type { SubjectData } from '@/types/SubjectData'
import { useSubjectsStore } from '@/stores/subjects'
import { useOfficesStore } from '@/stores/offices'

// Store
const subjectsStore = useSubjectsStore()
const officesStore = useOfficesStore()

// Props
const props = defineProps<{
  id: number
  name: string
  photo_file: string
  office: OfficeData
  subjects: SubjectData[]
}>()

const id = ref<number>(props.id)
const name = ref<string>(props.name)
const photo_file = ref<string>(props.photo_file)
const office = ref<OfficeData>(props.office)
const subjects = ref<SubjectData[]>(props.subjects)
const newSubject = ref<string>('')

// Computed
const otherSubjects = computed(() => {
  return subjectsStore.subjects.filter((subject) => {
    return !props.subjects.some((s) => s.id === subject.id)
  })
})

// Methods
const officeName = (office: OfficeData) => {
  return `${office.name} (${office.number})`
}
</script>

<template>
  <form>
    <div class="mb-3">
      <label for="teacherName" class="form-label">Jméno</label>
      <input type="text" class="form-control" id="teacherName" v-model="name" />
    </div>
    <div class="mb-3">
      <label for="subjectsDatalist" class="form-label">Předměty</label>
      <input
        class="form-control"
        list="datalistSubjects"
        id="subjectsDatalist"
        placeholder="Přidat předmět"
        v-model="newSubject"
        @change="$emit('addsubject', newSubject, otherSubjects)"
      />
      <datalist id="datalistSubjects">
        <option v-for="subject in otherSubjects" :key="subject.id" :value="subject.name" />
      </datalist>
      <div class="subject-list mt-2">
        <div
          v-for="(subject, index) in subjects"
          class="d-inline-flex align-items-center badge bg-body-secondary text-body"
          :class="index !== 0 && 'ms-2'"
          :key="subject.id"
        >
          {{ subject.name }}
          <button
            type="button"
            class="ms-1 btn-close"
            aria-label="Close"
            @click="$emit('removesubject', index)"
          ></button>
        </div>
      </div>
    </div>
    <div class="mb-3">
      <label for="teacherOffice" class="form-label">Kabinet</label>
      <select class="form-select" id="teacherOffice" v-model="office" aria-label="Kabinet">
        <option v-for="office in officesStore.offices" :key="office.id" :value="office">
          {{ officeName(office) }}
        </option>
      </select>
    </div>
  </form>
</template>
