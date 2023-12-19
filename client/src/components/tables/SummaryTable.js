import React from 'react'
import './ProtocolsTable.css'
import DataTable from 'react-data-table-component';
export default function SummaryTable(props) {

    

    const { pktsData, setPktsData, summData, setSummData, uploaded, setUploaded, isLoading, setIsLoading } = props;

    return (<>
            {/* <DataTable
            columns={summary_columns}
            data={summData}
        /> */}
            <div className='table-box'>
            <DataTable 
            columns={details_columns}
            data={pktsData}
            
        />
        </div>
    </>


    )
}
