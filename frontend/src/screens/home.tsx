import MiddleView from "../components/middle"

function Home(){
    return <><MiddleView />
    <div className="home-view">
        <div className="page-size blue-trpwx">
            <div className="ieotax">
                <section className="flex-center">
                    <div className="blue-xls">
                        <img src="/media/images/smart-watch.jpg" alt="" />
                    </div>
                    <div className="blue-xls">
                        <img src="/media/images/shoes-1.jpg" alt="" />
                    </div>
                </section>
              <div className="blue-xls blue-kkrds">
                    <img src="/media/images/phone-1.jpg" alt="" />
              </div>
            </div>
            <div>
                <div className="blue-xls blue-tts-full">
                    
                    <img src="/media/images/laptop-1.png" alt="" />
                </div>
            </div>
        </div>
    </div></>
}
export default Home

