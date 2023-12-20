import './App.css';
import { Routes, Route, BrowserRouter } from 'react-router-dom';
import Home from './pages/Home';
import GSE from './pages/GSE';


function App() {
  return (
    <>
    <BrowserRouter>
    <Routes>
      <Route path="/" exact element={<Home />}/>
      <Route path="/gse" exact element={<GSE/>}/>
      <Route path="/interfaces" exact element={<Home />}/>
    </Routes>
    </BrowserRouter>
    </>
  );
}

export default App;
