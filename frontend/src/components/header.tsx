import {WEBSITE_NAME } from '../utils/constants'
import {HiHome} from 'react-icons/hi'
import {BsBellFill} from 'react-icons/bs'

function Header(){
    return  <header>
    <nav className='page-size'>
        <ul>
            <a href="#"><span>{WEBSITE_NAME}</span></a>
            <div>
                <ul>
                    <li><a href="#" title='just login'>SIGN IN</a></li>
                    <li><a href="#" title='create a new account'>SIGN UP</a></li>
                </ul>
            </div>
        </ul>
        <ul>
            <li><a href="/" className='active'><HiHome/></a></li>
            <li><a href="/">Products</a></li>
            <li><a href="/">Top Rated</a></li>
            <li><a href="/">Gadgets</a></li>
            <li><a href="/">Blueterminal</a></li>
            <li><a href="/" className='flex-center'><BsBellFill/><span>Say Hi</span></a></li>
        </ul>
    </nav>
  </header>
}

export default Header