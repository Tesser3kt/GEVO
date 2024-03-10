<script setup lang="ts">
const props = defineProps<{
  id: number
  title: string
  message: string
  onDeleteClick: (id: number) => void
}>()
</script>

<template>
  <!-- Delete Modal -->
  <div
    class="modal fade"
    :id="`deleteModal-${props.id}`"
    tabindex="-1"
    :aria-labelledby="`deleteModalLabel-${props.id}`"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" :id="`deleteModalLabel-${props.id}`">{{ props.title }}</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">{{ props.message }}</div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Zrušit</button>
          <button
            type="button"
            class="btn btn-danger"
            data-bs-dismiss="modal"
            @click="onDeleteClick(id)"
          >
            Smazat
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
