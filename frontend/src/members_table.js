import * as React from "react";
import { DataGrid } from "@material-ui/data-grid";

const columns = [
  { field: "name", headerName: "Player Name", width: 250 },
  { field: "id", headerName: "Player Tag", width: 200 },
  { field: "joined", headerName: "Date Joined", width: 250 },
];

class MembersTable extends React.Component {
  state = {
    members: [],
  };

  componentDidMount() {
    const apiURL =
      "http://backend-env.eba-w6ysmk2u.us-east-2.elasticbeanstalk.com/members";
    fetch(apiURL)
      .then((response) => response.json())
      .then((data) => this.setState({ members: data }));
  }

  render() {
    let rows = [];
    for (let i = 0; i < this.state.members.length; i++) {
      rows.push({
        name: this.state.members[i][1],
        id: this.state.members[i][0],
        joined: this.state.members[i][2],
      });
    }
    return (
      <div style={{ height: 920, width: 700 }}>
        <h4>Members</h4>
        <DataGrid rows={rows} columns={columns} pageSize={15} />
      </div>
    );
  }
}

export default MembersTable;
