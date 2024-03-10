import { defineStore } from 'pinia'
import type { SubjectData } from '@/types/SubjectData'

export const useSubjectsStore = defineStore('subjects', {
  state: () => ({
    subjects: [
      {
        id: 1,
        name: 'Math'
      },
      {
        id: 2,
        name: 'Science'
      },
      {
        id: 3,
        name: 'English'
      },
      {
        id: 4,
        name: 'History'
      }
    ] as SubjectData[]
  })
})
