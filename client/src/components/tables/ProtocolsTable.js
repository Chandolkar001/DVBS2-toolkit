import React from 'react'
import './ProtocolsTable.css'
import DataTable from 'react-data-table-component';
export default function ProtocolsTable(props) {

    const summary_columns = [
        {
            name: 'Total Packets',
            selector: row => row.total,
        },
        {
            name: 'Total TS Packets.',
            selector: row => row.total_ts,
        },
        {
            name: 'Total GSE Packets.',
            selector: row => row.total_gse,
        },
    ];

    const details_columns = [
        {
            name: 'No.',
            selector: row => row.number,
        },
        {
            name: 'Time',
            selector: row => row.time_elapsed,
        },   
        {
            name: 'Source',
            selector: row => row.src,
        },
        {
            name: 'Destination',
            selector: row => row.dst,
        },
        {
            name: 'Protocol',
            selector: row => row.protocols.join(', '),
        },
        {
            name: 'Length',
            selector: row => row.length,
        },
        // {
        //     name: 'Info',
        //     selector: row => row.info,
        // },
    ];

    const summary_data = [
        {
            id: 1,
            total_packets: "2003",
            ts_packets: "23",
        }
    ];

    const details_data = [
        {
            id: 1,
            serial_number: '1',
            time: '0.00002234',
            source: '10.16.136,100',
            destination: '10.61.136.19',
            protocol: 'MPEG TS',
            length: '1358',
            info: 'NULL PACKET'
        },
        {
            id: 2,
            serial_number: '2',
            time: '0.00000034',
            source: '10.16.136,100',
            destination: '10.61.136.19',
            protocol: 'MPEG TS',
            length: '1358',
            info: 'NULL PACKET'
        }
    ]

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
