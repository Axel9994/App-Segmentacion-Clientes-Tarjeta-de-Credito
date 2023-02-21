<template>
    <div class="container">
      <h1>App Segmentación de Clientes Tarjeta de Crédito</h1>
      <br/>
      <br/>
      <form @submit.prevent="onSubmit">
        <div class="row mb-3">
          <label for="BALANCE">Balance:</label>
          <input type="text" class="form-control" id="BALANCE" name="BALANCE" v-model="BALANCE">
          
        </div>
        <div class="row mb-3">
          <label for="PURCHASES">Compras:</label>
          <input type="text" class="form-control" id="PURCHASES" name="PURCHASES" v-model="PURCHASES">
        </div>
        <div class="row mb-3">
          <label for="CASH_ADVANCE" >Adelanto en Efectivo:</label>
          <input type="text" class="form-control" id="CASH_ADVANCE" name="CASH_ADVANCE" v-model="CASH_ADVANCE">
        </div>
        <div class="row mb-3">
          <label for="PURCHASES_FREQUENCY">Frecuencia de Compras:</label>
          <input type="text" class="form-control" id="PURCHASES_FREQUENCY" name="PURCHASES_FREQUENCY" v-model="PURCHASES_FREQUENCY">
        </div>
        <div class="row mb-3">
          <label for="CASH_ADVANCE_FREQUENCY" >Frecuencia de Adelanto en Efectivo:</label>
          <input type="text" class="form-control" id="CASH_ADVANCE_FREQUENCY" name="CASH_ADVANCE_FREQUENCY" v-model="CASH_ADVANCE_FREQUENCY">
        </div>
        <div class="row mb-3">
          <label for="CREDIT_LIMIT" >Limite de Crédito:</label>
          <input type="text" class="form-control" id="CREDIT_LIMIT" name="CREDIT_LIMIT" v-model="CREDIT_LIMIT">
        </div>
        <div class="row mb-3">
          <label for="PAYMENTS">Pagos:</label>
          <input type="text" class="form-control" id="PAYMENTS" name="PAYMENTS" v-model="PAYMENTS">
        </div>
        <br/>
        <button type="submit" class="btn btn-primary">Realizar Predicción</button>
      </form>
      <br />
      <div v-if="prediccion" class="card">
        <div class="card-body">
          <h5 class="card-title">Clústers # {{ prediccion.num_cluster }}</h5>
          <p class="card-text">
            {{ prediccion.cluster_desc }}
          </p>
        </div>
      </div>
    </div>
  </template>
  
  <script>



  export default {
    name: 'Prediccion-item',
    data() {
      return {
        BALANCE: null,
        PURCHASES: null,
        CASH_ADVANCE: null,
        PURCHASES_FREQUENCY: null,
        CASH_ADVANCE_FREQUENCY: null,
        CREDIT_LIMIT: null,
        PAYMENTS: null,
        prediccion: null
      }
    },
    methods: {
      async onSubmit() {
        this.$http.post(
          '/api/predict', 
          { 
            BALANCE: this.BALANCE,
            PURCHASES: this.PURCHASES,
            CASH_ADVANCE: this.CASH_ADVANCE,
            PURCHASES_FREQUENCY: this.PURCHASES_FREQUENCY,
            CASH_ADVANCE_FREQUENCY: this.CASH_ADVANCE_FREQUENCY,
            CREDIT_LIMIT: this.CREDIT_LIMIT,
            PAYMENTS: this.PAYMENTS
          }
          )
          .then(response => this.prediccion = response.data)
          .catch(error => this.$swal({
            title: 'Error',
            text: error.response.data.message,
            icon: 'error',
            confirmButtonText: 'Aceptar'
          }))
        //this.prediccion = response.data.response
      },
    },
  }
  </script>
  