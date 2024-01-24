import { ref, onMounted } from 'vue'
import type { Ref } from 'vue'
import { defineStore } from 'pinia'
import type { GetAnalyticsResponse } from '@/services/interfaces'
import { ApiService } from '@/services'

export const useAnalytics = defineStore('analytics', () => {
  const data = ref(null)

  const apiSetup = ApiService.setup()

  onMounted(() => {
    apiSetup.getList().then((res) => {
      data.value = res.data
    })
  })

  return { data }
})
