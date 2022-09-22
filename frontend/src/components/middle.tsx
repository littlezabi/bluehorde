import {BsSearch} from 'react-icons/bs'
function MiddleView (){
    
    return <div className="middle">
        <div>
            <img src="/media/images/laptop.jpg" alt="middle view image" />
            <div></div>
        </div>
        <section >
            <div className="page-size">
                <h1>samsung a32 pro</h1>
                <h3>A Litle Too slow for 2022</h3>
                <h4>Flagship 4nm Snapdragon® 8 Gen 1</h4>
                <h4>Smart 120W HyperCharge</h4>
                <h4>120Hz flat AMOLED display</h4>
                <button>Learn More</button>
            </div>
        </section>
            <div className='blue-ii1sx'>
                <div>
                <input type="input" placeholder='Take easy to find! search here...' />
                <BsSearch/>
                </div>
            </div>
        </div>
}
export default MiddleView