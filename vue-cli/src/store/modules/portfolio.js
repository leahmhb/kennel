const state = {
    funds: 1000,
    stocks: []
}

const mutations = {
    'BUY_STOCK' (state, {stockId, qty, stockPrice}) {
        const record = state.stocks.find(element => element.id == stockId);
        if(record) {
            record.qty += qty;
        } else {
            state.stocks.push({id: stockId, qty:  qty});
        }
        state.funds -= stockPrice * qty;
    },
    'SELL_STOCK' (state, {stockId, qty, stockPrice}){
        const record = state.stocks.find(element => element.id == stockId);
        if(record.qty > qty) {
            record.qty -= qty;
        } else {
            state.stocks.splice(state.stocks.indexOf(record), 1);
        }
        state.funds += stockPrice * qty;
    }
};

const actions = {
    sellStock({commit}, order) {
        commit('SELL_STOCK', order);
    }
};

const getters = {
    stockPortfolio (state, getters) {
        return state.stocks.map(stock => {
            const record = getters.stocks.find(element => element.id == stock.id);
            return {
                id: stock.id,
                qty: stock.qty,
                name: record.name,
                price: record.price
            }
        });
    },
    funds(state){
        return state.funds;
    }
};

export default {
    state,
    mutations,
    actions,
    getters
};