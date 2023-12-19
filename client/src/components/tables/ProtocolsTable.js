import React from 'react'
import './ProtocolsTable.css'
import DataTable from 'react-data-table-component';
export default function ProtocolsTable() {

    const summary_columns = [
        {
            name: 'Total Packets',
            selector: row => row.total_packets,
        },
        {
            name: 'Total TS Packets.',
            selector: row => row.ts_packets,
        },
    ];

    const details_columns = [
        {
            name: 'No.',
            selector: row => row.serial_number,
        },
        {
            name: 'Time',
            selector: row => row.time,
        },   
        {
            name: 'Source',
            selector: row => row.source,
        },
        {
            name: 'Destination',
            selector: row => row.destination,
        },
        {
            name: 'Protocol',
            selector: row => row.protocol,
        },
        {
            name: 'Length',
            selector: row => row.length,
        },
        {
            name: 'Info',
            selector: row => row.info,
        },
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

    return (<>
            <DataTable
            columns={summary_columns}
            data={summary_data}
        />
            <DataTable
            columns={details_columns}
            data={details_data}
        />
    </>


    )
}
