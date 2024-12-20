


<!-- Script Part -->
<script setup lang="ts">
import { ref, computed } from 'vue'


// Url for backend
const backendUrl = computed(() => {
  return import.meta.env.VITE_APP_BACKEND_URL
})

// Placeholder for supploer
const selectedSupplier = ref('') 

// Placeholder for warehouse
const selectedWarehouse = ref('')

// Placeholder for products
const selectedProduct = ref('')

// Placeholder for quarter
const selectedQuarter = ref('')

// Placeholder for holiday
const selectedHoliday = ref('')

// // Placeholder for days between order and delivery
// const selectedDays = ref('')

// Options for suppliers
const suppliers = ['Aromatico', 'Beans Inc.', 'Fair Trade AG', 'Farmers of Brazil', 'Handelskontor Hamburg'] 

// Placeholder for warehouse
const warehouses = ['Amsterdam - RR', 'Barcelona - RR', 'Hamburg - RR', 'Istanbul - RR', 'London - RR', 'Nairobi - RR', 'Naples - RR']

// Placeholder for products
const products = ['Arabica', 'Excelsa', 'Liberica', 'Maragogype', 'Maragogype Type B', 'Robusta']

// Placeholder for quarter
const quarters = ['Q1', 'Q2', 'Q3', 'Q4']

// Placeholder for holiday
const holidays = ['Yes', 'No']

// Placeholder for quantity
const quantity = ref(0) // Step 3: Add ref for quantity

// Placeholder for days between order and delivery
const days = ref(0) // Step 3: Add ref for days

// Placeholder for prediction
const prediction = ref('')

// Loading state
const loading = ref(false)



// Make a get request to the backend
const getPrediction = async () => {  
  window.console.log('fetching data')

  prediction.value = ''
  
  loading.value = true; // Set loading to true
      try {
        const response = await fetch(`${backendUrl.value}/score_model?supplier=${selectedSupplier.value}&quantity=${quantity.value}&warehouse=${selectedWarehouse.value}&product=${selectedProduct.value}&quarter=${selectedQuarter.value}&holiday=${selectedHoliday.value}&days=${days.value}`);
        const data = await response.json();        
        window.console.log(data)
        prediction.value = data.prediction.toFixed(2);
        
      } catch (error) {
        alert('could not fetch data')
        window.console.error('Error fetching data:', error);        
      }
      loading.value = false; 
    }
</script>



<!-- Template Part -->
<template>
  
 <!-- Dropdown for suppliers -->
  <div>
    <label for="supplier">Please select a supplier:</label>
    <select id="supplier" v-model="selectedSupplier">
      <option v-for="supplier in suppliers" :key="supplier" :value="supplier">{{ supplier }}</option>
    </select>
    <div class="hint">Please select a supplier: {{ selectedSupplier }}</div>
  </div>

  <!-- Features -->
  <div>
    <label for="quantity">Enter Quantity:</label>
    <input id="quantity" type="number" v-model="quantity" />
    <div class="hint">Please select the ordered quantity: {{ quantity }}</div>
  </div>

  <div>
    <label for="warehouse">Please select a Warehouse:</label>
    <select id="warehouse" v-model="selectedWarehouse">
      <option v-for="warehouse in warehouses" :key="warehouse" :value="warehouse">{{ warehouse }}</option>
    </select>
    <div class="hint">Please select the Warehouse: {{ selectedWarehouse }}</div>
  </div>

  <div>
    <label for="product">Please select a Product:</label>
    <select id="product" v-model="selectedProduct">
      <option v-for="product in products" :key="product" :value="product">{{ product }}</option>
    </select>
    <div class="hint">Please select the Product: {{ selectedProduct }}</div>
  </div>

  <div>
    <label for="quarter">Please select a Quarter:</label>
    <select id="quarter" v-model="selectedQuarter">
      <option v-for="quarter in quarters" :key="quarter" :value="quarter">{{ quarter }}</option>
    </select>
    <div class="hint">Please select the Quarter: {{ selectedQuarter }}</div>
  </div>

  <div>
    <label for="days">Enter Days between Order and Planned Delivery:</label>
    <input id="days" type="number" v-model="days">
    <div class="hint">Enter Days between Order and Delivery: {{ days }}</div>
  </div>

  <!-- Dropdown for holidays -->
  <div>
    
    <label for="holiday">Please select if it is a holiday on Delivery Date:</label>
    <select id="holiday" v-model="selectedHoliday">
      <option v-for="holiday in holidays" :key="holiday" :value="holiday">{{ holiday }}</option>
    </select>
    <div class="hint">Please select if it is a holiday: {{ selectedHoliday }}</div>
  </div>

  <div>
    <button v-if="!loading" type="button" @click="getPrediction()">Predict</button>
  </div>

  <div v-if="loading" class="spinner"></div>

  <div class="prediction"> Predicted number of days late: {{ prediction }}</div>
  <div> Backend URL: {{ backendUrl }}</div>
  

 
</template>

<style scoped>

div {  
  margin: 1em;
  text-align: right;
}

label {  
  margin-right: 1em;
}

button {
  font-size: 1em;
  padding: 0.5em 1em;
  background-color: cadetblue;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.hint {
  font-size: 0.8em;
  color: #888;
}

.prediction {
  font-size: 1.5em;
  margin: 1em;
  color: cadetblue;
  text-align: center;
}


.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border-left-color: #4CAF50;
  animation: spin 1s ease infinite;
  margin: auto;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }

}
</style>
