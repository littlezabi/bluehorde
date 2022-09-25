import express, { Application, Request, Response } from 'express';
import bodyParser from 'body-parser';
import 'dotenv/config'
import smartDevicesRouter from './routers/mobile-devices-router'
import mongoose from 'mongoose';

const app: Application = express();
mongoose.connect("mongodb://localhost/bluehorde"); 
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));


app.use('/smart', smartDevicesRouter)

app.get('/', (req: Request, res: Response) => {
  res.send('Healthy')
})

const PORT = process.env.PORT || 8000;



app.listen(PORT, () => {
  console.log(`Server is running on PORT ${PORT}`)
}) 