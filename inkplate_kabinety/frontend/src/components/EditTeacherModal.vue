<script setup lang="ts">
import { ref, toRefs, onMounted, nextTick, computed } from 'vue'
import { useTeachersStore } from '@/stores/teachers'
import type { TeacherData } from '@/types/TeacherData'
import type { OfficeData } from '@/types/OfficeData'
import type { SubjectData } from '@/types/SubjectData'
import TeacherForm from '@/components/forms/TeacherForm.vue'
import { sleep } from '@/utils/sleep'

const teachersStore = useTeachersStore()

// Props
const props = defineProps<{
  id?: number
  name?: string
  photo_file?: string
  office?: OfficeData
  subjects?: SubjectData[]
}>()

// Refs
const renderEditForm = ref<boolean>(true)

// Computed
const formHeading = computed(() => {
  return props.id ? 'Upravit učitele' : 'Přidat učitele'
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

  // Make deep copies of the values
  id.value = teacherId.value
  name.value = teacherName.value
  photo_file.value = teacherPhotoFile.value
  office.value = teacherOffice.value
  subjects.value = teacherSubjects.value.map((s) => ({ ...s }))
}
const resetForm = () => {
  // Resets the form to the initial state
  // (either empty or with the teacher's data).
  if (props.teacher) {
    loadTeacher(props.teacher)
  } else {
    id.value = 0
    name.value = ''
    photo_file.value = ''
    office.value = {
      id: 0,
      name: '',
      number: ''
    }
    subjects.value = []
  }
  rerenderForm()
}
const rerenderForm = async () => {
  // Rerenders the edit form to reset it. Waits 500ms for the fade out
  // animation to finish.
  await sleep(500)
  renderEditForm.value = false
  await nextTick()
  renderEditForm.value = true
}
const addSubject = (name: string, otherSubjects: SubjectData[]) => {
  const subject = otherSubjects.find((s) => s.name === name)
  if (subject) {
    subjects.value.push(subject)
  }
}
const removeSubject = (index: number) => {
  subjects.value.splice(index, 1)
}
const saveTeacher = () => {
  const teacher: TeacherData = {
    id: id.value,
    name: name.value,
    photo_file: photo_file.value,
    office: office.value,
    subjects: subjects.value
  }
  if (id.value) {
    teachersStore.updateTeacher(teacher)
  } else {
    teachersStore.addTeacher(teacher)
  }
}

// Lifecycle hooks
onMounted(() => {
  resetForm()
})
</script>

<template>
  <div
    class="modal fade"
    :id="`editModal-${id}`"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    :aria-labelledby="`editModalLabel-${id}`"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" :id="`editModalLabel-${id}`">{{ formHeading }}</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
            @click="resetForm"
          ></button>
        </div>
        <div class="modal-body">
          <TeacherForm
            v-if="renderEditForm"
            :id="id"
            :name="name"
            :photo_file="photo_file"
            :office="office"
            :subjects="subjects"
            @addsubject="(newSubject, otherSubjects) => addSubject(newSubject, otherSubjects)"
            @removesubject="(index) => removeSubject(index)"
          />
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
            @click="resetForm"
          >
            Zrušit
          </button>
          <button
            type="button"
            class="btn btn-success"
            data-bs-dismiss="modal"
            @click="saveTeacher"
          >
            Uložit
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
