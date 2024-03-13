<script setup lang="ts">
import { ref, toRefs } from 'vue'
import { useTeachersStore } from '@/stores/teachers'
import type { TeacherData } from '@/types/TeacherData'
import TeacherForm from '@/components/forms/TeacherForm.vue'

const store = useTeachersStore()

// Props
const props = defineProps<{
  teacher: TeacherData
}>()
</script>

<template>
  <div
    class="modal fade"
    :id="`editModal-${teacher.id}`"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    :aria-labelledby="`editModalLabel-${teacher.id}`"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" :id="`editModalLabel-${teacher.id}`">Upravit učitele</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
            @click="$emit('rerender')"
          ></button>
        </div>
        <div class="modal-body">
          <TeacherForm :teacher="props.teacher" />
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
            @click="$emit('rerender')"
          >
            Zrušit
          </button>
          <button type="button" class="btn btn-success" data-bs-dismiss="modal">Uložit</button>
        </div>
      </div>
    </div>
  </div>
</template>
