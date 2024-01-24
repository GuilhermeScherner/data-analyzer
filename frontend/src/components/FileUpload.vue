<script setup lang="ts">
import { ref } from 'vue'
import { ApiService } from '@/services'
import { useAnalytics } from '@/stores/list'
const fileInput = ref<HTMLInputElement | null>(null)
const selectedFile = ref<File>()
const fileError = ref<string | null>(null)
const apiSetup = ApiService.setup()
const isLoading = ref(false)
const { updateData } = useAnalytics()

const handleFileChange = async (event: Event) => {
  isLoading.value = true
  const target = event.target as HTMLInputElement
  selectedFile.value = target.files?.[0]
  fileError.value = null
  if (selectedFile.value) {
    try {
      await apiSetup.uploadFile(selectedFile.value)
    } catch (error) {
      console.error('Error uploading file:', error)
    } finally {
      isLoading.value = false
      selectedFile.value = undefined
      updateData()
    }
  }
}
</script>

<template>
  <div v-if="isLoading" class="loading">Loading...</div>
  <div v-else class="upload-area">
    <input id="removed-input" type="file" @change="handleFileChange" ref="fileInput" />
    <p class="text-input" v-if="!selectedFile">Drop files here or click to select</p>
    <p class="text-input" v-else>{{ selectedFile.name }} selected</p>
  </div>
</template>

<style scoped>
#removed-input {
  cursor: pointer;
  opacity: 0;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 10;
}
.loading {
  width: 200px;
  height: 150px;
}
.upload-area {
  width: 200px;
  height: 150px;
  border: 1px solid #ddd;
  border-radius: 10px;
  text-align: center;
  cursor: pointer;
  position: relative;
  margin: 2rem 0;
}

.text-input {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
}
</style>
