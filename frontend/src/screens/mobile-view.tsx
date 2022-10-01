import { useEffect,useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import {getSmartDevice, getSmartError, getSmartItems, getSmartStatus} from '../context/smart-slice'
import { smartItemsRat } from '../utils/interfaces'

function MobileView(){
    const _getSmartStatus = useSelector(getSmartStatus)
    const _getSmartError = useSelector(getSmartError)
    const _getSmartItem = useSelector(getSmartItems)
    const [items, setItem] = useState<smartItemsRat>()
    const dispatch = useDispatch()
    useEffect(()=>{
        console.log('status: ', _getSmartStatus)
        if(_getSmartStatus === 'idle'){
            dispatch(getSmartDevice('motorola-edge-s-891'))
        }else if(_getSmartStatus === 'complete'){
            console.log('complete: ', _getSmartItem.items[0])
            setItem(_getSmartItem.items[0])
        }else if(_getSmartStatus === 'error'){
            console.log('error: ', _getSmartError, _getSmartItem)
        }
    }, [_getSmartStatus, dispatch, _getSmartError, _getSmartItem]) 
    return <>       
    <div className="mobile-view">
            <div className="page-size mobile-top-view">
            <img src="/media/assets/top-bg-layer.svg" alt="" />
            <img src="/media/assets/top-bottom-layer.svg" alt="" />
            </div>
            <div className="page-size mobile-top-taxc-view">
                <div>
                    <img src="/media/phones/sam.jpg" alt="" className="layer" />
                </div>
                <div>
                    <h2>{items && items.name}</h2>
                    <h3>{items && items?.short_detail['subtitle']}</h3>
                    <h5>50MP AI quad camera | 90Hz FHD+ display</h5>
                    <h5>Exynos 850 (8nm) fast processor</h5>
                </div>
            </div>
            <div className="mobile-middle">
                <div className="page-size">
                    <div className="mobile-middle-top">
                        <div className="mobile-keolxl">
                            <section>
                                <img src="/media/assets/calendar.png" alt="" />
                                <p>Release date</p>
                                <span>22 March 2023</span>
                            </section>
                            <span className="line-v"></span>
                            <section>
                                <img src="/media/assets/phone.png" alt="" />
                                <p>Phone Body</p>
                                <span>195g, 8.8mm thickness</span>
                            </section>
                            <span className="line-v"></span>
                            <section>
                                <img src="/media/assets/terminal.png" alt="" />
                                <p>System Information</p>
                                <span>Android 12, One UI 4.1</span>
                            </section>
                            <span className="line-v"></span>
                            <section>
                                <img src="/media/assets/chip.png" alt="" />
                                <p>Phone Storage</p>
                                <span>32GB/64GB/128GB storage, microSDXC</span>
                            </section>
                        </div>
                        <h2>Samsung A13 Pro</h2>
                        <h4>Level Up!</h4>
                    </div>
                    <div className="specifications">
                        <div className="mobile-title">
                            <span className="line-h"></span>
                            <span>SPECIFICATIONS</span>
                            <span className="line-h"></span>
                        </div>
                        <div className="uaweluef">
                            <div className="iiillxla">
                                <section>
                                    <div>
                                        <span className="title">NETWORK</span>
                                        <img src="/media/assets/network.png" alt="" />
                                    </div>
                                    <div className="ckek3lxhwed">
                                        <span className="mobile-sub">Technology</span>
                                        <span className="mobile-text">GSM / HSPA / LTE</span>
                                        <span className="mobile-text">GSM / HSPA / LTE</span>
                                        <span className="mobile-text">GSM / HSPA / LTE</span>
                                        <span className="line-h"></span>
                                        <span className="mobile-sub">2G Bands</span>
                                        <span className="mobile-text">GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (dual-SIM only)</span>
                                        <span className="mobile-text">GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (dual-SIM only)</span>
                                        <span className="mobile-text">GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (dual-SIM only)</span>
                                        <span className="line-h"></span>
                                        <span className="mobile-sub">3G Bands</span>
                                        <span className="mobile-text">HSDPA 850 / 900 / 2100</span>
                                        <span className="mobile-text">HSDPA 850 / 900 / 2100</span>
                                    </div>
                                </section>
                                <section>
                                    <div className="flex-h">
                                        <span className="title">MEMORY/STORAGE</span>
                                        <img src="/media/assets/chip.png" alt="" />
                                    </div>
                                    <div className="ckek3lxhwed">
                                        <span className="mobile-sub">Technology</span>
                                        <span className="mobile-text">GSM / HSPA / LTE</span>
                                        <span className="line-h"></span>
                                        <span className="mobile-sub">2G Bands</span>
                                        <span className="mobile-text">GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (dual-SIM only)</span>
                                        <span className="line-h"></span>
                                        <span className="mobile-sub">3G Bands</span>
                                        <span className="mobile-text">HSDPA 850 / 900 / 2100</span>
                                    </div>
                                </section>
                                <section>
                                    <div className="flex-h">
                                        <span className="title">MEMORY/STORAGE</span>
                                        <img src="/media/assets/chip.png" alt="" />
                                    </div>
                                    <div className="ckek3lxhwed">
                                        <span className="mobile-sub">Technology</span>
                                        <span className="mobile-text">GSM / HSPA / LTE</span>
                                        <span className="line-h"></span>
                                        <span className="mobile-sub">2G Bands</span>
                                        <span className="mobile-text">GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (dual-SIM only)</span>
                                        <span className="line-h"></span>
                                        <span className="mobile-sub">3G Bands</span>
                                        <span className="mobile-text">HSDPA 850 / 900 / 2100</span>
                                    </div>
                                </section>
                            </div>
                            
                            <div className="iiillxla">
                                <section>
                                    <div className="flex-h">
                                        <span className="title">abc</span>
                                        <img src="/media/assets/chip.png" alt="" />
                                    </div>
                                    <div className="ckek3lxhwed">
                                        <span className="mobile-sub">Technology</span>
                                        <span className="mobile-text">GSM / HSPA / LTE</span>
                                        
                                    </div>
                                </section>
                                <section>
                                    <div className="flex-h">
                                        <span className="title">MEMORY/STORAGE</span>
                                        <img src="/media/assets/chip.png" alt="" />
                                    </div>
                                    <div className="ckek3lxhwed">
                                        <span className="mobile-sub">Technology</span>
                                        <span className="mobile-text">GSM / HSPA / LTE</span>
                                        <span className="line-h"></span>
                                        <span className="mobile-sub">2G Bands</span>
                                        <span className="mobile-text">GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (dual-SIM only)</span>
                                        
                                    </div>
                                </section>
                                <section>
                                    <div className="flex-h">
                                        <span className="title">MEMORY/STORAGE</span>
                                        <img src="/media/assets/chip.png" alt="" />
                                    </div>
                                    <div className="ckek3lxhwed">
                                        <span className="mobile-sub">Technology</span>
                                        <span className="mobile-text">GSM / HSPA / LTE</span>
                                        <span className="line-h"></span>
                                        <span className="mobile-sub">2G Bands</span>
                                        <span className="mobile-text">GSM 850 / 900 / 1800 / 1900 - SIM 1 & SIM 2 (dual-SIM only)</span>
                                        <span className="line-h"></span>
                                        <span className="mobile-sub">3G Bands</span>
                                        <span className="mobile-text">HSDPA 850 / 900 / 2100</span>
                                    </div>
                                </section>
                            </div>
                        </div>
                        <svg className="klciwemx" xmlns="http://www.w3.org/2000/svg" width="1281.12" height="453.813" viewBox="0 0 1281.12 453.813">
                            <path id="pricing-layer" d="M1675,3521.748H393.88v453.813s52.493-155.146,208.525-174.333c104.7-12.875,345.537,0,345.537,0h440s52.135-1.234,95.8-9.463c42.238-7.961,75.575-22.655,112.058-44.116,73.852-43.443,79.208-137.568,79.208-137.568Z" transform="translate(-393.88 -3521.748)"/>
                        </svg>
                    </div>
                    <div className="mobile-pricing"> 
                        <div className="mobile-title">
                                <span className="line-h"></span>
                                <span>PRICING</span>
                                <span className="line-h"></span>
                        </div>
                    <div className="pricing-cksax">
                        <section>
                            <span className="title">32GB 3GB RAM</span>
                            <a href="">
                                <div>
                                    <span className="small">$</span>
                                    <div>
                                        <span className="price">147.00</span>
                                        <img src="/media/assets/amazon.png" alt="" />
                                    </div>
                                </div>
                            </a>
                            <a href="">
                                <div>
                                    <span className="small">$</span>
                                    <div>
                                        <span className="price">147.00</span>
                                        <img src="/media/assets/amazon.png" alt="" />
                                    </div>
                                </div>
                            </a>

                        </section>
                        <section>
                            <span className="title">32GB 3GB RAM</span>
                            <a href="">
                                <div>
                                <span className="small">$</span>
                                    <div>
                                        <span className="price">147.00</span>
                                        <img src="/media/assets/amazon.png" alt="" />
                                    </div>
                                </div>
                            </a>
                            <a href="">
                                <div>
                                    <span className="small">$</span>
                                    <div>
                                        <span className="price">147.00</span>
                                        <img src="/media/assets/amazon.png" alt="" />
                                    </div>
                                </div>
                            </a>

                        </section>
                    </div>
                </div>
                </div>
            </div>
        </div>
    </>
}

export default MobileView