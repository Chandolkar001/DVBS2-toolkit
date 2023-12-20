import React, { useState } from 'react'
import './ProtocolsTable.css'
import axios from 'axios';
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
    const [expandedData, setExpandedData] = useState([[]]);
    const [expandedRows, setExpandedRows] = useState([3]);


    const handleRowClick = async (toggle, row) => {
        // Check if the row is already expanded
        console.log(toggle)
        const isRowExpanded = expandedRows.includes(row.number);

        // If not expanded, make an actual API call to fetch additional data
        if (!isRowExpanded) {
            try {
                // Make an API call to fetch additional data

                const response = await axios.post(`http://localhost:8000/api/files/extra_data/${row.number}/`);

                // Update the state with the expanded row ID
                setExpandedRows([row.number]);
                setExpandedData([response.data]);

                // Log or use the response.data as needed
                console.log('Additional data for row:', response.data);
            } catch (error) {
                console.error('Error fetching additional data:', error);
            }
        } else {
            // If already expanded, collapse the row
            setExpandedRows([]);
        }
    };



    const getDynamicColumns = (data) => {
        // Extract all unique keys from the data to create dynamic columns
        const allKeys = data.reduce((keys, row) => {
            Object.keys(row).forEach((key) => {
                if (!keys.includes(key)) {
                    keys.push(key);
                }
            });
            return keys;
        }, []);

        // Create columns with dynamic headers
        return allKeys.map((key) => ({
            name: key.toUpperCase(),
            selector: key,
            sortable: true,
            cell: (row) => (typeof row[key] === 'object' ? JSON.stringify(row[key]) : row[key] || '-'),
        }));
    };


    const groupedData = (data) => {
        // Define the order of categories
        const categoryOrder = ['pid', 'map_pid', 'Stream_id', 'desc_name'];
        console.log(data)
        // Initialize the grouped data with empty arrays
        const grp_data = {
            pid: [],
            map_pid: [],
            Stream_id: [],
            desc_name: []
        }

        // Group objects by type
        data.forEach(obj => {
            console.log(Object.keys(obj), "hehe")
            const type = Object.keys(obj)[0];
            if (categoryOrder.includes(type)) {
                grp_data[type].push(obj);
            }
        });

        console.log(grp_data)
        return grp_data


    }


    const ExpandedComponent = ({ x }) => <>

        <DataTable
        title="MPT2 Data"
            columns={[
                {
                    name: 'PID',
                    selector: row => row.pid,
                },
                {
                    name: 'Continuity Counter',
                    selector: row => row.cc,
                },
                {
                    name: 'Transport Scrambling Control',
                    selector: row => row.tsc,
                },
                {
                    name: 'Message',
                    selector: row => row.message,
                }
            ]}
            data={groupedData(expandedData[0]).pid}

        />
        <DataTable
        title="PAT Data"
            columns={[
                {
                    name: 'PAT PID',
                    selector: row => row.map_pid,
                },
                {
                    name: 'PAT Number',
                    selector: row => row.map_num,
                },
            ]}
            data={groupedData(expandedData[0]).map_pid}
            noDataComponent={<span>No PAT Found</span>}

        />
        <DataTable
        title="PMT Data"
            columns={[
                {
                    name: 'Stream Id',
                    selector: row => row.Stream_id,
                },
                {
                    name: 'Stream Type',
                    selector: row => row.Stream_type,
                },
            ]}
            data={groupedData(expandedData[0]).Stream_id}
            noDataComponent={<span>No PMT Found</span>}

        />

    </>;


    return (<>
        {/* <DataTable
            columns={summary_columns}
            data={summData}
        /> */}
        <div className='table-box'>
            <DataTable
                columns={details_columns}
                data={pktsData}
                expandableRows
                expandableRowsComponent={ExpandedComponent}
                onRowExpandToggled={handleRowClick}
            // expandedRows={expandedRows}
            // expandableRowExpanded={(row) => expandedData}

            />
        </div>
    </>


    )
}
