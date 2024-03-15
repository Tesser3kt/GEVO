import { defineStore } from 'pinia'
import type { TeacherData } from '@/types/TeacherData'

export const useTeachersStore = defineStore('teachers', {
  state: () => ({
    teachers: [
      {
        id: 1,
        name: 'John Doe',
        photo_file: 'adam_klepac',
        office: {
          id: 1,
          name: 'Main Office',
          number: '123'
        },
        subjects: [
          {
            id: 1,
            name: 'Math'
          },
          {
            id: 2,
            name: 'Science'
          }
        ]
      },
      {
        id: 2,
        name: 'Jane Doe',
        photo_file: 'zofia_drevojankova',
        office: {
          id: 2,
          name: 'Secondary Office',
          number: '098'
        },
        subjects: [
          {
            id: 1,
            name: 'Math'
          },
          {
            id: 3,
            name: 'English'
          },
          {
            id: 4,
            name: 'History'
          }
        ]
      }
    ] as TeacherData[]
  }),
  getters: {
    getTeacherById: (state) => (id: number) => {
      return state.teachers.find((teacher) => teacher.id === id)
    }
  },
  actions: {
    async deleteTeacher(id: number) {
      /* TODO API call */
      this.teachers = this.teachers.filter((teacher) => teacher.id !== id)
    },
    async updateTeacher(teacher: TeacherData) {
      /* TODO API call */
      const index = this.teachers.findIndex((t) => t.id === teacher.id)
      this.teachers[index] = teacher
    },
    async addTeacher(teacher: TeacherData) {
      /* TODO API call */
      this.teachers.push(teacher)
    }
  }
})
