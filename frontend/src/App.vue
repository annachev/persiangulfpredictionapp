<script setup lang="ts">
import Prediction from './components/Prediction.vue'
</script>

<template>
  <div class="headline">
    Late purchase order prediction - Group Persian Gulf
  </div>

  <div class ="subtitle">
    Anna Chevychalova, Jack Wyett, George Lavas, Xiang Wang and Jette Anders
  </div>

  <div class ="subheadline">
    Please fill in the following fields to get a prediction
  </div>

  <Prediction/>
</template>



<style scoped>
.headline {
  font-size: 2em;
  margin: 1em;
  text-align: center;
}

.subtitle {
  font-size: 1.5em;
  margin: 1em;
  text-align: center;
  color: cadetblue;
}

.subheadline {
  font-size: 1.5em;
  margin: 1em;
  text-align: center;
  font-style: italic;
}
</style>
