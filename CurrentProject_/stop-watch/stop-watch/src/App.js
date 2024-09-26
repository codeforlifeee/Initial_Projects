//import logo from './logo.svg';
//import './App.css';
import Header from "./component/Header";
import Product from "./component/Product"
function App() {
  const productDetail={
    title:"laptop",
    price:"66000",
    brand:"msi"
  }
  return (
    <div>
      <Header></Header>
      
      <Product productData ={productDetail}/>
      
    </div>
  );
}

export default App;
