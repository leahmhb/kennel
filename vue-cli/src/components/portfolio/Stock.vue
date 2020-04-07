<template>
    <div class="col-sm-4 col-md-6">
        <div class="card card-success m-2">
            <div class="card-body">
                <h5 class="card-title">{{ stock.name }}</h5>
                <h6 class="card-subtitle mb-2 text-muted">(Price: {{ stock.price }}) | Qty: {{ stock.qty }}</h6>

                <div class="input-group mb-3">
                    <input 
                    v-model="qty" 
                    type="number" 
                    class="form-control" 
                    placeholder="qty"
                    min="1">
                    <div class="input-group-append">
                        <button 
                        @click="sellStock" 
                        class="btn btn-success" 
                        type="button" 
                        :disabled="qty <= 0 || !Number.isInteger(qty)">Sell</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapActions} from 'vuex';
    export default {
        props: ['stock'],
        data() {
            return {
                qty: 0
            }
        },
        methods: {
            this.spreadify(mapActions({
               'sellStock'
           })),
            sellStock(){
                const order = {
                    stockId: this.stock.id,
                    stockPrice: this.stock.price,
                    qty: this.qty
                };
                this.sellStock();
            }
        }
    }
</script>