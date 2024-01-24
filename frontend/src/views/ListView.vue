<script setup lang="ts">
import ListItem from '@/components/ListItem.vue'
import FileUpload from '@/components/FileUpload.vue'
import { useAnalytics } from '@/stores/list'
import { storeToRefs } from 'pinia'
import { useSelected } from '@/stores/selected'
import { ref, type Ref } from 'vue'

const { data } = storeToRefs(useAnalytics())
const { updateId } = useSelected()
const isLoading: Ref<boolean> = ref(false)
const update = (id: number) => {
  isLoading.value = true
  updateId(id)
  setTimeout(() => {
    isLoading.value = false
  }, 800)
}
</script>

<template>
  <div class="container-upload">
    <FileUpload />
  </div>
  <div>
    <div v-if="data.length === 0">No value!!</div>
    <div v-for="item in data" :key="item.id">
      <ListItem v-if="!isLoading" :date="item.date" :name="item.name" @click="update(item.id)" />
    </div>
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
