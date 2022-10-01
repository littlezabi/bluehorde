import {createSlice, createAsyncThunk} from '@reduxjs/toolkit'
import axios from 'axios'
import { smartStateInter } from '../utils/interfaces'
export const getProducts:any = createAsyncThunk('products/get', async () => {
    try {
        const {data} = await axios.get(`/products/`)
        return {
            error: false,
            items: data,
            message: false
        }
    } catch (error:any) {
        return {
            error: true,
            items: [],
            message: error.message
        }
    }
})

const initialState:smartStateInter = {
    status: 'idle',
    items: [],
    error: false,
}
const productsSlice = createSlice({
    name: 'products',
    initialState,
    reducers: {

    },
    extraReducers(builder){
        builder.addCase(getProducts.pending, (state, action) => {
            state.status = 'pending'
        }).addCase(getProducts.fulfilled, (state, action)=>{
            state.status = 'complete'
            state.items = action.payload
        }).addCase(getProducts.rejected, (state, action)=>{
            state.status = 'error'
            state.error = action.payload
        })
    }
})

export const productStatus = (state:any) => state.productsSlice.status
export const productItems = (state:any) => state.productsSlice.items
export default productsSlice.reducer