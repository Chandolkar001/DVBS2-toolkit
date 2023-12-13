import React from 'react'
import './PcapUpload.css'
export default function PcapUpload() {
      return (
        <div class="zone">

        <div id="dropZ">
          <i class="fa fa-cloud-upload"></i>
          <div>Drag and drop your file here</div>                    
          <span>OR</span>
          <div class="selectFile">       
            <label for="file">Select file</label>                   
            <input type="file" name="files[]" id="file"/>
          </div>
          <p>File size limit : 10 MB</p>
        </div>
      
      </div>

      )
}
