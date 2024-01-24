<script setup lang="ts">
import ListItem from '@/components/ListItem.vue'
import FileUpload from '@/components/FileUpload.vue'
import { onMounted } from 'vue'
import {ApiService} from '@/services'
const aa = ApiService.setup()
onMounted(() => {
  aa.getList()
})
</script>

<template>
  <div class="container-upload">
    <FileUpload />
  </div>
  <div>
    <ListItem date="2020/10/10" heading="teste1"  />
    <br />
    <ListItem date="2020/10/10" heading="teste1"  />
    <br />
    <ListItem date="2020/10/10" heading="teste1"  />
  </div>
</template>


<style scoped>
.container-upload {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 2rem;
}
</style>
