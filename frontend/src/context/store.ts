import {configureStore} from '@reduxjs/toolkit'
import smartSlice from './smart-slice'
import productsSlice from './products-slice'
const store = configureStore({
    reducer:{
        smartSlice,
        productsSlice
    }
})

export default store