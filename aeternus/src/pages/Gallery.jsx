import Card from '../Card/Card.jsx'
import "../css/Gallery.css"

const Gallery = () => {
  return (

      <div className="cardDiv" align="center" >
        <Card name="Wei Xiang" test="I LOVE AWS LAMBDA" imgs="/src/img/wx.jpg" />
        <Card name="Matthew" test="" imgs="/src/img/matt.jpg"/>
        <Card name="Jeryl" test="" imgs="/src/img/jeryl.png"/>
        <Card name="Jay" test="This app helped me get married in 2 days" imgs="/src/img/jay.png"/>
      </div>  


  );
};

export default Gallery;