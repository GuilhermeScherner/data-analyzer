import { defineStore } from 'pinia'
import { ref, type Ref } from 'vue'
import { ApiService } from '@/services'
import type { GetAnalyticsResponse } from '@/services/interfaces'

export const useSelected = defineStore('selected', () => {
  const id: Ref<number> = ref(0)
  const dataSelected: Ref<GetAnalyticsResponse | any> = ref({})
  const apiSetup = ApiService.setup()
  async function updateId(idData?: number | null) {
    try {
      if (idData) {
        id.value = idData
        const result = await apiSetup.getById(idData)
        dataSelected.value = result.data
      } else {
        id.value = 0
      }
    } catch (e) {
      console.log(e)
    }
  }

  return {
    id,
    updateId,
    dataSelected
  }
})
