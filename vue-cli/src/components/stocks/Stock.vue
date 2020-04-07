<template>
    <div class="col-sm-4 col-md-6">
        <div class="card card-success m-2">
            <div class="card-body">
                <h5 class="card-title">{{ stock.name }}</h5>
                <h6 class="card-subtitle mb-2 text-muted">(Price: {{ stock.price }})</h6>

                <div class="input-group mb-3">
                    <input 
                    v-model="qty" 
                    type="number" 
                    class="form-control" 
                    placeholder="qty"
                    min="1">
                    <div class="input-group-append">
                        <button 
                        @click="buyStock" 
                        class="btn btn-success" 
                        type="button" 
                        :disabled="qty <= 0 || !Number.isInteger(qty)">Buy</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['stock'],
        data() {
            return {
                qty: 0
            }
        },
        methods: {
            buyStock() {
                const order = {
                    stockId: this.stock.id,
                    stockPrice: this.stock.price,
                    qtyy: this.qty,
                };
                console.log(order);
                this.qty = 0;
            }
        }
    }
</script>