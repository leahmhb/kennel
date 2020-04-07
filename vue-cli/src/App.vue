<template>
    <div class="container">
        <app-header></app-header>
        <div class="row">
            <div class="col-sm-12">
                <router-view></router-view>
            </div>
        </div>

    </div>
</template>

<script>
    import Header from './components/Header.vue'
    export default {
        components: {
            appHeader: Header
        },
        created() {
            this.$store.dispatch('initStocks');
        }, 
        methods: {
            spreadify (fn, fnThis) {
                return function () { /* accepts unlimited arguments */

        var spreadArgs = [ ];// Holds the processed arguments for use by `fn`

        var length = arguments.length; // Caching length

        var currentArg;

        for (var i = 0; i < length; i++) {
            currentArg = arguments[i];

            if (Array.isArray(currentArg)) {
                spreadArgs = spreadArgs.concat(currentArg);
            } else {
                spreadArgs.push(currentArg);
            }
        }

        fn.apply(fnThis, spreadArgs);
    };
}
}
}
</script>

<style>
body {
    padding: 30px
}
</style>