import { createRouter, createWebHistory } from 'vue-router'
import type { RouteLocationNormalized } from 'vue-router'
import { useUserStore } from '@/stores/user'

const requireAuth = async (
  to: RouteLocationNormalized,
  from: RouteLocationNormalized,
  next: Function
) => {
  const userStore = useUserStore()
  if (to.name !== 'login' && (!userStore.isAuthenticated || !userStore.isAdmin)) {
    next({ name: 'login' })
  } else {
    next()
  }
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/teachers'
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/teachers',
      name: 'teachers',
      component: () => import('../views/TeachersView.vue'),
      beforeEnter: requireAuth
    },
    {
      path: '/offices',
      name: 'offices',
      component: () => import('../views/OfficesView.vue'),
      beforeEnter: requireAuth
    },
    {
      path: '/subjects',
      name: 'subjects',
      component: () => import('../views/SubjectsView.vue'),
      beforeEnter: requireAuth
    }
  ]
})

export default router
