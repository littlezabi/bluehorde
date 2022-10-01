import {useEffect, useState} from 'react'
import {useDispatch, useSelector} from 'react-redux'
import ProductCategRender from '../components/product-category-render'
import { getProducts, productItems, productStatus } from '../context/products-slice'
import { compareCatItems } from '../utils/compare'
import { smartItemsRat } from '../utils/interfaces'

function Products(){
    const dispatch = useDispatch()
    const productState = useSelector(productStatus)
    const productData = useSelector(productItems)
    const [loading,setLoading] = useState(false)
    const [items, setItems] = useState<smartItemsRat>()
    
    useEffect(()=>{
        console.log('status: ', productState)
        if(productState === 'idle'){
            dispatch(getProducts())
            setLoading(true)
        }else if(productState === 'complete'){
            if(productData.error === false){
                let set = productData.items
                set = [...set]
                set = set.sort(compareCatItems)
                setItems(set)
            }
        }
        if(productData != 'pending'){
            setLoading(false)
        }
    }, [productState, productData, dispatch])
    return <div className="products">
        <div className="top-view">
            <img src="/media/assets/categ-view-top-layer.svg" alt="" />
            <img src="/media/assets/ellipses.svg" alt="" />
            <div className="xilcdk3e-ls5x">
                <section>
                    <h3>Be Cool</h3>
                    <h2>Pick Your</h2>
                    <h1>Brand</h1>
                    <h2>Now</h2>
                    <h5>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.</h5>
                    <a href="#" title="">Latest Devices</a>
                </section>
                <section>
                    <img src="/media/assets/catego.png" alt="" />
                </section>
            </div>

        </div>
        <div className="page-size items">
            <div className="container">
                {
                    items && items.map((item:any) =>  <ProductCategRender item={item}/>)
                }
            </div>
        </div>
    </div>
}
<div >asdfaa</div>
export default Products