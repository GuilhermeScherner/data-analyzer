<script setup lang="ts">
import { format } from 'date-fns'
defineProps<{
  date: string
  name: string
}>()
</script>

<template>
  <div class="item">
    <i>
      {{ format(date, 'dd-MM-yy HH:mm') }}
      <br />
      <slot name="icon">{{ name }}</slot>
    </i>
  </div>
</template>

<style scoped>
.item {
  margin-top: 0.5rem;
  display: flex;
  position: relative;
  cursor: pointer;
}

i {
  display: flex;
  place-items: center;
  place-content: center;
  width: 500px;
  height: 70px;
  color: var(--color-text);
  border: 1px solid var(--color-border);
  background: var(--color-background);
  border-radius: 8px;
}

h3 {
  font-size: 1.2rem;
  font-weight: 500;
  margin-bottom: 0.1rem;
  color: var(--color-heading);
}

@media (min-width: 1024px) {
  .item {
    margin-top: 0.5rem;
    margin-left: 1rem;
    cursor: pointer;
  }

  i {
    border: 1px solid var(--color-border);
    background: var(--color-background);
    border-radius: 8px;
    width: 100%;
    height: 70px;
  }
}
</style>
