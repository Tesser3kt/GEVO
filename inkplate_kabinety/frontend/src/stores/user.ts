import { defineStore } from 'pinia'
import type { UserData } from '@/types/UserData'

export const useUserStore = defineStore('user', {
  state: () => ({
    user: {
      id: 0,
      username: 'admin',
      email: 'admin@admin',
      is_admin: true
    } as UserData
  }),
  getters: {
    isAuthenticated: (state) => state.user !== null,
    isAdmin: (state) => state.user?.is_admin
  }
})
