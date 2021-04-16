import React from 'react';
import ReactDOM from 'react-dom';
import Members from './members'
import MembersTable from './members_table';

ReactDOM.render(
    <Members />,
    document.getElementById('root')
);

ReactDOM.render(
    <MembersTable />,
    document.getElementById('members_table')
);

