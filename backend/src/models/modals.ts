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
export const SmartDevices = mongoose.model("mobile_devices", smartSchema)

const categoriesSchema = new mongoose.Schema({
    category: {type: String, required: true},
    items: {type: Number, required: true, default: 0},
    image: {type: String, required: true, default: ''},
}, {
    timestamps: true,
    strict: false
});
export const categoriesModal = mongoose.model("categories", categoriesSchema)
