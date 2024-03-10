<script setup lang="ts">
import { ref, toRefs, onMounted } from 'vue'
import type { TeacherData } from '@/types/TeacherData'
import type { OfficeData } from '@/types/OfficeData'
import type { SubjectData } from '@/types/SubjectData'

// Props
const props = defineProps<{
  teacher?: TeacherData
}>()

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
  </form>
</template>
