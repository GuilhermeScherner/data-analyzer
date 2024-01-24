<script setup lang="ts">
import ChartView from '@/views/ChartView.vue'
import ListView from '@/views/ListView.vue'
</script>

<template>
  <div class="container">
    <div class="wrapper">
      <ListView />
    </div>
    <div class="wrapper">
      <ChartView />
    </div>
  </div>

</template>

<style scoped>
.container {
  min-height: 100%;
  display: flex;
  width: 100%;
  gap: 1rem;
}

.container .wrapper {
  flex: 1;
  width: 100%;
  padding: 0 2rem;
}

@media (min-width: 1024px) {
  .container {
    min-height: 100%;
    display: flex;
    width: 100%;
  }

  .container .wrapper {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }
}
</style>
