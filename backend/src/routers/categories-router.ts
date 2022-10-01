import express,{ Request, Response } from "express";
import {categoriesModal} from '../models/modals'
import expressAsyncHandler from "express-async-handler";
const categoriesRouter = express.Router()
// productsRouter.get('/:slug', expressAsyncHandler(async (req: Request, res:Response)=>{
//     const items = await SmartDevices.find({'slug': req.params.slug}).limit(10)
//     res.status(200).send(items)
// }))
categoriesRouter.get('/', expressAsyncHandler(async (req: Request, res:Response)=>{
    const items = await categoriesModal.find({})
    res.status(200).send(items)
}))
export default categoriesRouter