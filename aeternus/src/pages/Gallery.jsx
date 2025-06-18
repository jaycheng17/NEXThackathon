import Card from '../Card/Card.jsx'
import "../css/Gallery.css"
import wx from "../img/wx.jpg";
import jk from "../img/jeryl.png";
import matt from "../img/matt.jpg";
import jay from "../img/jay.png";

const Gallery = () => {
  return (

      <div className="cardDiv" align="center" >
        <Card name="Wei Xiang" test="I LOVE AWS LAMBDA" imgs={wx} />
        <Card name="Matthew" test="sentence_transformers LOL" imgs={matt}/>
        <Card name="Jeryl" test="You want a Bride? I'll give you a Bribe :D" imgs={jk}/>
        <Card name="Jay" test="This app helped me get married in 2 days" imgs={jay}/>
      </div>  
  );
};

export default Gallery;