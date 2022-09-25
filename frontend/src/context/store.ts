import {configureStore} from '@reduxjs/toolkit'
import smartSlice from './smart-slice'
const store = configureStore({
    reducer:{
        smartSlice
    }
})

export default store