import { CONFIG } from "@/config";
import { inject } from 'vue'

export const ApiService = {
  name: 'Comp',
  setup() {
    const axios: any = inject('axios')  // inject axios
    const getList = async (): Promise<void> => {
      await axios
        .get(CONFIG.API_URL)
        .then((response: { data: any }) => {
          console.log(response.data)
        });
    };

    const uploadFile = async (file: any): Promise<any> => {
      const formData = new FormData();
      formData.append('file', file);
      await axios
        .post(CONFIG.API_URL, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        .then((response: { data: any }) => {
          console.log(response.data)
          return response.data
        });
    }
    return { getList, uploadFile }
  }
}