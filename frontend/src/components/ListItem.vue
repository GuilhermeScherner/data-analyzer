<script setup lang="ts">
defineProps<{
  date: string,
  heading: string,
}>()
</script>

<template>
  <div class="item">
    <i>
      <slot name="icon"></slot>
    </i>
  </div>
</template>

<style scoped>
.item {
  margin-top: 2rem;
  display: flex;
  position: relative;
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
    margin-top: 0;
    margin-left: 1rem;
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
