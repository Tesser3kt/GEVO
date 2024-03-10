import { defineStore } from 'pinia'
import type { OfficeData } from '@/types/OfficeData'

export const useOfficesStore = defineStore('offices', {
  state: () => ({
    offices: [
      {
        id: 1,
        name: 'Main Office',
        number: '123'
      },
      {
        id: 2,
        name: 'Secondary Office',
        number: '098'
      }
    ] as OfficeData[]
  })
})
