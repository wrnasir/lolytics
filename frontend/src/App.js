import './App.css'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import ListStatsComponent from './components/ListStatsComponent'
import HeaderComponent from './components/HeaderComponent'
import FooterComponent from './components/FooterComponent'

function App() {
  return (
    <>
    <BrowserRouter>
      <HeaderComponent />
      <Routes>
        <Route path='/' element = { <ListStatsComponent /> }></Route>
      </Routes>
      <FooterComponent />
    </BrowserRouter>
    </>
  )
}

export default App;
