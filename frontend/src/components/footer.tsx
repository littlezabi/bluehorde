import {WEBSITE_NAME } from '../utils/constants'
function Footer(){
    return <footer>
            <div>
                &copy;{WEBSITE_NAME } {new Date().getFullYear()} All Right reserved. 
                created by Zohaib Jozvi(LittleZabi) and Blueterminal Lab.
            </div>
        </footer>
}
export default Footer