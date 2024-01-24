<script setup lang="ts">
import { ref } from 'vue'
import { ApiService } from '@/services'
const fileInput = ref<HTMLInputElement| null>(null);
const selectedFile = ref<File>();
const fileError = ref<string | null>(null);
const apiSetup = ApiService.setup()

const handleFileChange = async (event: Event) => {
  const target = event.target as HTMLInputElement;
  selectedFile.value = target.files?.[0];
  fileError.value = null;
  if (selectedFile.value){
    const formData = new FormData();
    formData.append("file", selectedFile);
    try {
      const response = await apiSetup.uploadFile(formData)
      console.log("File uploaded successfully:", response.data);
    } catch (error) {
      console.error("Error uploading file:", error);
    }
  }
};

</script>

<template>
  <div class="upload-area">
    <input id="removed-input" type="file" @change="handleFileChange" ref="fileInput" />
    <p class="text-input" v-if="!selectedFile" >Drop files here or click to select</p>
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
.upload-area {
  width: 200px;
  height: 150px;
  border: 1px solid #DDD;
  border-radius: 10px;
  text-align: center;
  cursor: pointer;
  position: relative;
  margin: 2rem 0;
}

.text-input{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
}
</style>