import express,{ Request, Response } from "express";
import SmartDevices from '../models/smart-modal'
import expressAsyncHandler from "express-async-handler";
const smartDevicesRouter = express.Router()
smartDevicesRouter.get('/:slug', expressAsyncHandler(async (req: Request, res:Response)=>{
    const items = await SmartDevices.find({'slug': req.params.slug}).limit(10)
    res.status(200).send(items)
}))
smartDevicesRouter.get('/', expressAsyncHandler(async (req: Request, res:Response)=>{
    const items = await SmartDevices.find({}).limit(40)
    res.status(200).send(items)
}))
export default smartDevicesRouter