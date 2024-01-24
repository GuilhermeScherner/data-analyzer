import { CONFIG } from '@/config'
import { inject } from 'vue'
import type {
  GetAnalyticsResponse,
  GetListAnalyticsResponse,
  UploadFileResponse
} from '@/services/interfaces'

export const ApiService = {
  name: 'Comp',
  setup() {
    const axios: any = inject('axios') // inject axios
    const getList = async (): Promise<{ data: GetListAnalyticsResponse[] }> => {
      return await axios.get(CONFIG.API_URL + '/')
    }

    const getById = async (id: number): Promise<{ data: GetAnalyticsResponse }> => {
      return await axios.get(`${CONFIG.API_URL}/${id}`)
    }

    const uploadFile = async (file: any): Promise<{ data: UploadFileResponse }> => {
      const formData = new FormData()
      formData.append('file', file)
      return await axios.post(CONFIG.API_URL + '/upload-file/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
    }
    return { getList, uploadFile, getById }
  }
}
