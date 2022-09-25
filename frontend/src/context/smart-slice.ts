import {createAsyncThunk, createSlice} from '@reduxjs/toolkit'
import axios from 'axios'
import { smartStateInter } from '../utils/interfaces'


const initialState:smartStateInter = {
    status: 'idle',
    items: [],
    error: ''
}
// vivo-watch-327
export const getSmartDevice:any  = createAsyncThunk('smart/get', async (slug:string) => {
    try{
        const { data } = await axios.get(`/smart/${slug}`)
        return {
            error: false,
            items: data,
            message: false
        }
    }catch(e:any){
        console.log(e.message)
        return {
            error: true,
            items: [],
            message: e.message
        }
    } 
})

const smartDevicesSlice = createSlice({
    name: 'smart',
    initialState,
    reducers: {
        resetState(state, action){
            state.status = 'idle'
            state.items = []
            state.error = ''
        }
    },
    extraReducers(builder){
        builder.addCase(getSmartDevice.pending, (state, action)=>{
            state.status = 'pending'
        }).addCase(getSmartDevice.fulfilled, (state, action)=>{
            state.status = 'complete'
            state.items = action.payload
        }).addCase(getSmartDevice.rejected, (state, action)=>{
            state.status = 'error'
            state.error = action.payload
        })
    } 
}) 

export const getSmartStatus = (state:any) => state.smartSlice.status
export const getSmartItems = (state:any) => state.smartSlice.items
export const getSmartError = (state:any) => state.smartSlice.error

export default smartDevicesSlice.reducer