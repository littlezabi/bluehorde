import mongoose from "mongoose";

const smartSchema = new mongoose.Schema({
    name: {type: String, required: true},
    brief_scrap: {type: Object, required: true},
    mobile_specs: {type: Object, required: true},
    mobile_pricing: {type: Object, required: true},
    original: {type: String, required: false}
}, {
    timestamps: true,
    strict: false
});
const SmartDevices = mongoose.model("mobile_devices", smartSchema)
export default SmartDevices