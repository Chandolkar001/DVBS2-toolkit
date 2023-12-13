import React from 'react';
import './Home.css'
import { Col, Row, Container, Button, Dropdown } from 'react-bootstrap';
import PcapUpload from '../components/pcap/PcapUpload';
import no_preview from '../assets/no-prev.png'
import sih_logo from '../assets/sih-logo.png'
function Home() {

    const sideOptions = [
        {
            name: "PCAP",
            function: "ddd"
        },
        {
            name: "HTTP Traffic",
            function: "handleHttp"
        },
        {
            name: "FTP Traffic",
            function: "handleFtp"
        },
        {
            name: "TCP Traffic",
            function: "handleTcp"
        }
        ,
        {
            name: "HTTP Traffic",
            function: "handleHttp"
        },
        {
            name: "FTP Traffic",
            function: "handleFtp"
        },
        {
            name: "FTP Traffic",
            function: "handleFtp"
        }

    ]
    return (
        <Container fluid style={{ height: '100vh' }}>
            <Row  style={{height: "80px", backgroundColor: "#282828", color: "#ffffff"}} >
                <Col xs={10}>
                <h1>DVB-S2 Parser</h1>
                </Col>
                <Col className='ms-auto'>
                <img src={sih_logo} alt="no preview" style={{height: '60px', width: 'auto'}} />
                </Col>
               
             
            </Row>

            <Row style={{ height: "50%" }}>
                <Col xs={2}>
                    <div className="button-container">
                        {sideOptions.map((option, index) => (
                            <div key={index} className="button" >
                                {option.name}
                            </div>
                        ))}
                    </div>
                </Col>
                <Col>
                    <PcapUpload />
                </Col>
            </Row>

            <Row style={{ height: "40%" }}>

                <Col xs={4} >

                    <Row className="position-relative">
                        <Dropdown style={{ position: "absolute", top: 0, left: 0 }}>
                            <Dropdown.Toggle variant="success" id="dropdown-basic">
                                Select Channel
                            </Dropdown.Toggle>

                            <Dropdown.Menu>
                                <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                                <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                                <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
                            </Dropdown.Menu>
                        </Dropdown>
                        <img src={no_preview} alt="no preview" style={{ width: "100%", height:"100%", objectFit: "cover" }} />
                    </Row>
                </Col>
                <Col>
                    <h1>Here some options</h1>
                </Col>
            </Row>

        </Container>
    );
}

export default Home;
