<template>
    <div class="row">
        <app-stock v-for="stock in stocks" :stock="stock"></app-stock>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex';
    import Stock from './Stock.vue';

    export default {
        computed: {  
         this.spreadify(mapGetters({stocks: 'stockPortfolio'})
     },
     components: {
        appStock: Stock
    }
}
</script>