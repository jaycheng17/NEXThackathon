import "../css/Home.css"
import { Container, Row, Col } from 'react-bootstrap';

const Home = () => {
  return (
    // <Container fluid className="d-flex justify-content-center align-items-center vh-100 px-0">
    //   <div className="text-center">
    //     <Row>
    //       <Col className="Head">Forever & Always</Col>
    //     </Row>
    //     <Row>
    //       <Col className="Desc">Bespoke Wedding Styling & Planning</Col>
    //     </Row>
    //   </div>
    // </Container>
    <div className="Homediv">
      <div className="home-content">
        <p className="Head">Forever & Always</p>
        <p className="Desc">Bespoke Wedding Styling &amp; Planning</p>
      </div>
    </div>
  );
};

export default Home;
