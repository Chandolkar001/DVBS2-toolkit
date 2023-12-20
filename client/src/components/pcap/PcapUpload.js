import React from 'react'
import './PcapUpload.css'
import { useState } from 'react';
import axios from 'axios';
import {Button, Spinner} from 'react-bootstrap';
export default function PcapUpload(props) {
  const [file, setFile] = useState(null);

  // const [pkts_data, setPktsData] = useState([]);
  // const [summ_data, setSummData] = useState([]);
  // const [uploaded, setUploaded] = useState(false);
  // const [isLoading, setIsLoading] = useState(false);

  const { pktsData, setPktsData, summData, setSummData, uploaded, setUploaded, isLoading, setIsLoading,  isButtonDisabled, setIsButtonDisabled, fileUrl, setFileUrl, setVideoUrl} = props;

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };
 const processVideo = async () => {
    const formData = new FormData();
    formData.append('file', file);
    console.log(formData)
    try {
      // Make Axios POST request
      console.log("started")
      
      const response = await axios.post('http://localhost:8000/api/files/videostream/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      // Handle the response
      console.log('File upload successful:', response);
      let urls = response.data.video_files.map(element => "http://localhost:8000" + element)
      console.log(urls)
      setFileUrl(urls)
      setVideoUrl(urls[0])
    } catch (error) {
      // Handle errors
      console.error('File upload failed:', error);
    }
 }
  const handleUpload = async () => {
    if (!file) {
      console.error('No file selected.');
      return;
    }

    // Create FormData object to send the file
    const formData = new FormData();
    formData.append('file', file);

    console.log(formData)

    try {
      // Make Axios POST request
      setIsLoading(true)
      setIsButtonDisabled(true)
      const response = await axios.post('http://localhost:8000/api/files/process/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      // Handle the response
      
      console.log('File upload successful:', response.data);
      setPktsData(response.data.packets);
      setSummData(response.data.protocol_counts);
      setIsLoading(false);
      
      setUploaded(true);
      console.log(pktsData);
      console.log(summData);
      await processVideo();
      setIsButtonDisabled(false)

    } catch (error) {
      // Handle errors
      console.error('File upload failed:', error);
    }
  };
  return (
    <div class="zone">

      <div id="dropZ">
        <i class="fa fa-cloud-upload"></i>
        <div>Drag and drop your file here</div>
        <span>OR</span>
        <div class="selectFile">
          <label for="file">Select file</label>
          <input type="file" name="files[]" id="file" onChange={handleFileChange}/>
        </div>
        {/* <p>File size limit : 10 MB</p> */}
        <Button onClick={handleUpload}>Upload</Button><br />
        {isLoading &&
          <Spinner animation="border" role="status" variant='primary'>
            <span className="visually-hidden">Loading...</span>
          </Spinner>
        }
      </div>

    </div>

  )
}
