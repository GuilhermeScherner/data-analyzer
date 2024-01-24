<script setup lang="ts">
import Chart from 'chart.js/auto'
import { watch, ref } from 'vue'
import { useSelected } from '@/stores/selected'
import { storeToRefs } from 'pinia'
const { dataSelected } = storeToRefs(useSelected())
const chartMRR = ref<Chart>()
const chartChurn = ref<Chart>()

watch(dataSelected, () => {
  const canvasMRR = document.querySelector('#myChart') as HTMLCanvasElement
  const canvasChurn = document.querySelector('#myChart1') as HTMLCanvasElement
  if (!dataSelected) {
    console.error('Canvas element not found')
    return
  }
  if (!canvasMRR || !canvasChurn) {
    console.error('Canvas element not found')
    return
  }

  if (chartMRR.value) {
    chartMRR.value.destroy()
  }

  if (chartChurn.value) {
    chartChurn.value.destroy()
  }

  chartMRR.value = new Chart(canvasMRR, {
    type: 'bar',
    data: {
      labels: Object.keys(dataSelected.value.churn),
      datasets: [
        {
          label: 'MRR',
          data: Object.entries(dataSelected.value.churn).map(([_, value]) => value),
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  })

  chartChurn.value = new Chart(canvasChurn, {
    type: 'line',
    data: {
      labels: Object.keys(dataSelected.value.mrr),
      datasets: [
        {
          label: 'Churn',
          data: Object.entries(dataSelected.value.mrr).map(([_, value]) => value),
          borderWidth: 1
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  })
})
</script>
<template>
  <div class="about">
    <canvas id="myChart"></canvas>
    <canvas id="myChart1"></canvas>
  </div>
</template>
<style>
.about {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }

  #myChart {
    width: 100%;
  }
}
</style>
