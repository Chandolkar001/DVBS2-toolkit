import React, { useState } from 'react';
import './Home.css'
import { Col, Row, Container, Button, Dropdown, Form, Spinner } from 'react-bootstrap';
import PcapUpload from '../components/pcap/PcapUpload';
import no_preview from '../assets/no-prev.png'
import sih_logo from '../assets/sih-logo.png'
import ProtocolsTable from '../components/tables/ProtocolsTable';
import ReactPlayer from 'react-player'
import axios from 'axios';
import { JSONTree } from 'react-json-tree'
import { Link } from 'react-router-dom';
function Home() {

    const [pktsData, setPktsData] = useState([]);
    const [summData, setSummData] = useState([]);
    const [uploaded, setUploaded] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    const [analysisReport, setAnalysisReport] = useState(null);

    const sideOptions = [
        {
            name: "Transport Stream",
            path: "/"
        },
        {
            name: "General Stream Encapsulation",
            path: "/gse"
        },
        {
            name: "Interfaces",
            path: "/interfaces"
        },

    ]
    const [selectedFile, setSelectedFile] = useState(null);
    const [isButtonDisabled, setIsButtonDisabled] = useState(false);
    const [fileUrl, setFileUrl] = useState(false)
    const [videoUrl, setVideoUrl] = useState(false)
    const [analysisIsLoading, setAnalysisIsLoading] = useState(false)
    const handleFileChange = (e) => {
        const file = e.target.files[0];
        setSelectedFile(file);
    }
    const handleUpload = async () => {
        if (!selectedFile) {
            console.error('No file selected.');
            return;
        }

        // Create FormData object to send the file
        const formData = new FormData();
        formData.append('file', selectedFile);

        console.log(formData)

        try {
            // Make Axios POST request
            setIsButtonDisabled(true)
            const response = await axios.post('http://localhost:8000/api/files/videostream/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setIsButtonDisabled(false)

            // Handle the response
            console.log('File upload successful:', response.data);
            let url = "http://localhost:8000" + response.data.video_file
            console.log(url)
            setFileUrl(url);

        } catch (error) {
            // Handle errors
            console.error('File upload failed:', error);
        }
    };

    const jsondata = {
        array: [1, 2, 3],
        bool: true,
        object: {
            foo: 'bar',
        }
    };

    const getAnalysisReport = async () => {
        try {
            // Make Axios POST request
            setAnalysisIsLoading(true)
            const response = await axios.get('http://localhost:8000/api/files/analysis/');
            setAnalysisIsLoading(false)

            // Handle the response
            console.log('File upload successful:', response.data);
            setAnalysisReport(response.data);
            // let url = "http://localhost:8000" + response.data.video_file
            // console.log(url)
            // setFileUrl(url);

        } catch (error) {
            // Handle errors
            console.error('File upload failed:', error);
        }
    }

    const handleSelect = (eventKey, event) => {
        // `eventKey` is the value associated with the selected item
        // You can perform actions or call functions based on the selected item here
        let x = fileUrl[eventKey]
        setVideoUrl(x)
        console.log(x);
    };
    return (
        <Container fluid style={{ height: '100vh' }}>
            <Row style={{ height: "80px", backgroundColor: "#282828", color: "#ffffff" }} >
                <Col xs={10}>
                    <h1>DVB-S2 Parser</h1>
                </Col>
                <Col className='ms-auto'>
                    <img src={sih_logo} alt="no preview" style={{ height: '60px', width: 'auto' }} />
                </Col>


            </Row>

            <Row style={{ height: "50%" }}>
                <Col xs={2}>
                    <div className="button-container">
                        {sideOptions.map((option, index) => (
                            <div key={index} className="button">
                                <Link to={option.path} style={{ textDecoration: 'none', color: 'inherit' }}>{option.name}</Link>
                            </div>
                        ))}
                    </div>
                </Col>
                <Col className='content-box'>

                    {!uploaded && <PcapUpload
                        pktsData={pktsData}
                        setPktsData={setPktsData}
                        summData={summData}
                        setSummData={setSummData}
                        uploaded={uploaded}
                        setUploaded={setUploaded}
                        isLoading={isLoading}
                        setIsLoading={setIsLoading}
                        isButtonDisabled={isButtonDisabled}
                        setIsButtonDisabled={setIsButtonDisabled}
                        fileUrl={fileUrl}
                        setFileUrl={setFileUrl}
                        setVideoUrl={setVideoUrl}
                    />}
                    {uploaded && <ProtocolsTable
                        pktsData={pktsData}
                        setPktsData={setPktsData}
                        summData={summData}
                        setSummData={setSummData}
                        uploaded={uploaded}
                        setUploaded={setUploaded}
                        isLoading={isLoading}
                        setIsLoading={setIsLoading}
                    />}


                </Col>
            </Row>

            <Row style={{ height: "40%" }}>

                <Col xs={4} >

                    <Row className="position-relative">
                        <Dropdown style={{ position: "absolute", top: 0, left: 0, zIndex: 9 }} onSelect={handleSelect}>
                            <Dropdown.Toggle variant="success" id="dropdown-basic">
                                Select Channel
                            </Dropdown.Toggle>

                            <Dropdown.Menu >
                                {/* <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                                <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                                <Dropdown.Item href="#/action-3">Something else</Dropdown.Item> */}
                                {fileUrl && fileUrl.map((url, index) => <Dropdown.Item key={index} eventKey={index}>Stream {index}</Dropdown.Item>)}
                            </Dropdown.Menu>
                        </Dropdown>
                        {/* <div class="selectFile">
                            <label for="file">Select file</label>
                            <input type="file" name="files[]" id="file" onChange={handleFileChange} />
                            <Button onClick={handleUpload}>Upload</Button><br />
                        </div> */}

                        {!isButtonDisabled && !fileUrl && <img src={no_preview} alt="no preview" style={{ width: "100%", height: "100%", objectFit: "cover" }} />}
                        {isButtonDisabled && <Spinner animation="border" role="status" variant='primary' />}
                        {fileUrl && <video width="640" height="360" controls loop autoPlay key={videoUrl}>
                            <source src={videoUrl} />
                            Your browser does not support the video tag.
                        </video>}
                    </Row>
                </Col>
                <Col >
                    <span style={{ fontSize: "2.5rem", marginRight: "15px" }}>Analysis Report</span>
                    {/* <ReactPlayer url='rtp://@:5004' /> */}
                    {uploaded && !analysisReport && !analysisIsLoading && <Button variant="primary" onClick={getAnalysisReport}>Get Analysis Report</Button>}
                    {analysisIsLoading && <Spinner animation="border" role="status" variant='primary' />}
                    {analysisReport && <div className='analysis'><JSONTree data={analysisReport} /></div>}

                </Col>
            </Row>

        </Container>
    );
}

export default Home;
