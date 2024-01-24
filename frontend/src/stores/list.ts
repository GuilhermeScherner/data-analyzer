import { onMounted, ref } from 'vue'
import type { Ref } from 'vue'
import { defineStore } from 'pinia'
import type { GetListAnalyticsResponse } from '@/services/interfaces'
import { ApiService } from '@/services'

export const useAnalytics = defineStore('analytics', () => {
  const data: Ref<GetListAnalyticsResponse[] | any[]> = ref([])
  const apiSetup = ApiService.setup()
  onMounted(async () => {
    updateData()
  })
  async function updateData() {
    const result = await apiSetup.getList()
    data.value = result.data
  }
  return { data, updateData }
})
