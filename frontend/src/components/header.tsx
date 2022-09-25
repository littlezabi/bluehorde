import {WEBSITE_NAME } from '../utils/constants'
import {HiHome} from 'react-icons/hi'
import {BsBellFill} from 'react-icons/bs'
import {Link} from 'react-router-dom'

function Header(){
    return  <header>
    <nav className='page-size'>
        <ul>
            <Link to="/"><span>{WEBSITE_NAME}</span></Link>
            <div>
                <ul>
                    <li><a href="#" title='just login'>SIGN IN</a></li>
                    <li><a href="#" title='create a new account'>SIGN UP</a></li>
                </ul>
            </div>
        </ul>
        <ul>
            <li><Link to="/" className='active'><HiHome/></Link></li>
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