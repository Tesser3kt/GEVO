<script setup lang="ts">
import { useSubjectsStore } from '@/stores/subjects'
import { ref, toRefs, onMounted, computed } from 'vue'
import type { TeacherData } from '@/types/TeacherData'
import type { OfficeData } from '@/types/OfficeData'
import type { SubjectData } from '@/types/SubjectData'

// Props
const props = defineProps<{
  teacher?: TeacherData
}>()

// Store
const subjectsStore = useSubjectsStore()

// Refs
const id = ref<number>(0)
const name = ref<string>('')
const photo_file = ref<string>('')
const office = ref<OfficeData>({
  id: 0,
  name: '',
  number: ''
})
const subjects = ref<SubjectData[]>([])

const newSubject = ref<string>('')

// Computed
const otherSubjects = computed(() => {
  return subjectsStore.subjects.filter((subject) => {
    return !subjects.value.some((s) => s.id === subject.id)
  })
})

// Methods
const loadTeacher = (teacher: TeacherData) => {
  const {
    id: teacherId,
    name: teacherName,
    photo_file: teacherPhotoFile,
    office: teacherOffice,
    subjects: teacherSubjects
  } = toRefs(teacher)

  id.value = teacherId.value
  name.value = teacherName.value
  photo_file.value = teacherPhotoFile.value
  office.value = teacherOffice.value
  subjects.value = teacherSubjects.value
}

// Lifecycle hooks
onMounted(() => {
  if (props.teacher) {
    loadTeacher(props.teacher)
  }
})
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
          <button type="button" class="ms-1 btn-close btn-xs" aria-label="Close"></button>
        </div>
      </div>
    </div>
  </form>
</template>
