import {Link} from 'react-router-dom'
const ProductCategRender = ({item}:any)=>{
    return <Link to={`/category/${item.category}`} key={item._id}>
    <section>
        <div className="from-left">
            <span className="badge badge-success badge-round">New Arrivals</span>
        </div>
        <div className="center"><img src="/media/assets/catego.png" alt="" /></div>
        <div className="center">
            <h3>{item.items}+ Modals</h3>
            <h2>{item.category}</h2>
            <h4>Better normal for all</h4>
        </div>
    </section>
</Link>
}

export default ProductCategRender;